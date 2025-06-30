#!/usr/bin/env bash

mkdir -p bin

# Download Stockfish Linux binary zip from GitHub Releases
wget -O bin/stockfish.zip https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-20.04.zip

# Unzip it
unzip -o bin/stockfish.zip -d bin

# Make sure it's executable
chmod +x bin/stockfish/stockfish

# Copy to ./bin/stockfish
cp bin/stockfish/stockfish ./bin/stockfish

echo "Stockfish 16 downloaded and ready."
