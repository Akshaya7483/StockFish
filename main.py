from fastapi import FastAPI, Query
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stockfish API is running"}

@app.get("/analyze")
def analyze(
    fen: str = Query(..., description="FEN string of the position"),
    depth: int = Query(10, description="Search depth (e.g., 10-20)")
):
    try:
        # Start Stockfish process
        process = subprocess.Popen(
            ["./bin/stockfish"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1,
        )

        # Initialize UCI
        process.stdin.write("uci\n")
        process.stdin.flush()

        while True:
            line = process.stdout.readline()
            if "uciok" in line:
                break

        # Set the position
        process.stdin.write(f"position fen {fen}\n")
        process.stdin.flush()

        # Start analysis
        process.stdin.write(f"go depth {depth}\n")
        process.stdin.flush()

        bestmove = None

        # Read output lines
        while True:
            line = process.stdout.readline()
            if line.startswith("bestmove"):
                bestmove = line.strip()
                break

        # Clean up
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.kill()

        if not bestmove:
            return {"error": "Failed to get best move."}

        return {"bestmove": bestmove}

    except Exception as e:
        return {"error": str(e)}
