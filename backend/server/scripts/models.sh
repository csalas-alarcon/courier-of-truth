#!/usr/bin/env bash
# models.sh - Just downloads initial dummy models

set -e #Exit if Error
+
echo " --- Downloading Tiny Models --- "

# 1. Phi2
if [ ! -f "models/phi2.gguf" ]; then
    echo "Downloading Phi2..."
    curl -L "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf?download=true" -o models/phi2.gguf
else
    echo "Phi2 already exists. Skipping."
fi

# 2. Qwen2.5
if [ ! -f "models/qwen.gguf" ]; then
    echo "Downloading Qwen..."
    curl -L "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf?download=true" -o models/qwen.gguf
else
    echo "Qwen already exists. Skipping."
fi

# 3. Danube
if [ ! -f "models/danube.gguf" ]; then
    echo "Downloading Danube..."
    curl -L "https://huggingface.co/h2oai/h2o-danube3-500m-chat-GGUF/resolve/main/h2o-danube3-500m-chat-Q8_0.gguf?download=true" -o models/danube.gguf
else
    echo "Danube already exists. Skipping."
fi