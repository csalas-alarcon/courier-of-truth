#!/usr/bin/env bash
# models.sh - Just downloads initial dummy models

set -e #Exit if Error

echo " --- Downloading Tiny Models --- "

mkdir -p models

# Downloading Model
if [ ! -f "models/qwen.gguf" ]; then
    echo "Installing Qwen Model"
    curl -L "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf?download=true" -o models/qwen.gguf
else
    echo "Qwen Model already installed"
fi