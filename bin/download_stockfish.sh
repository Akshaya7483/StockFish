#!/usr/bin/env bash

mkdir -p bin

# Download the working Stockfish zip
wget -O bin/stockfish.zip https://stockfishchess.org/files/stockfish_16_linux_x64_avx2.zip

# Unzip it
unzip -o bin/stockfish.zip -d bin

# The binary ends up inside a folder, e.g., stockfish_16_x64_avx2/stockfish_16_x64_avx2
# Move it to bin/stockfish
mv bin/stockfish_16_x64_avx2/stockfish_16_x64_avx2 bin/stockfish

# Make sure it's executable
chmod +x bin/stockfish

echo "Stockfish downloaded and ready."
