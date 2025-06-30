from fastapi import FastAPI
from fastapi.responses import JSONResponse
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stockfish API is running"}

@app.get("/analyze")
def analyze(fen: str, depth: int = 15):
    try:
        # Start Stockfish process
        process = subprocess.Popen(
            ["stockfish.exe"],   # If you get "file not found", give the full path here
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )

        # Send "uci" to initialize
        process.stdin.write("uci\n")
        process.stdin.flush()

        # Wait for "uciok"
        while True:
            line = process.stdout.readline()
            print(f"Engine output: {line.strip()}")
            if "uciok" in line:
                break

        # Set the position
        process.stdin.write(f"position fen {fen}\n")
        process.stdin.flush()

        # Start analyzing
        process.stdin.write(f"go depth {depth}\n")
        process.stdin.flush()

        bestmove = ""
        while True:
            line = process.stdout.readline()
            print(f"Engine output: {line.strip()}")
            if line.startswith("bestmove"):
                bestmove = line.strip()
                break

        # Clean up
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.kill()

        return JSONResponse({"bestmove": bestmove})

    except Exception as e:
        # If any error happens, return details
        return JSONResponse({"error": str(e)}, status_code=500)