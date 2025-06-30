
mkdir -p bin

wget -O bin/stockfish.zip https://stockfishchess.org/files/stockfish_16_linux_x64_avx2.zip

unzip -o bin/stockfish.zip -d bin

mv bin/stockfish_16_x64_avx2/stockfish_16_x64_avx2 bin/stockfish

chmod +x bin/download_stockfish

echo "Stockfish downloaded and ready."
