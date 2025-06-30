#!/usr/bin/env bash

mkdir -p bin

# Download Stockfish 16 Linux AVX2
wget -O bin/stockfish.zip https://stockfishchess.org/files/stockfish_16_linux_x64_avx2.zip

# Unzip
unzip -o bin/stockfish.zip -d bin

# Make sure it's executable
chmod +x bin/stockfish/stockfish

# Copy to ./bin/stockfish so your code can call ./bin/stockfish
cp bin/stockfish/stockfish ./bin/stockfish

echo "Stockfish 16 downloaded and ready."
