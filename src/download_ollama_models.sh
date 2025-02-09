#!/bin/bash

# Array of model names to download
models=(
    	"smollm2:1.7b"
	"smollm2:360m"
	"smollm2:135m"
	"phi4:14b"
	"phi3.5:3.8b"
	"qwen2.5:0.5b"
	"qwen2.5:1.5b"
	"qwen2.5:3b"
	"qwen2.5:7b"
	"qwen2.5:14b"
	"qwen2.5:32b"
	"llama3.2:1b"
	"llama3.2:3b"
	"mistral-small:24b"
    	"deepseek-r1:1.5b"
    	"deepseek-r1:8b"
)

# Function to download a model
download_model() {
    local model=$1
    echo "Downloading model: $model"
    ollama pull "$model"
    
    # Check if download was successful
    if [ $? -eq 0 ]; then
        echo "Successfully downloaded $model"
    else
        echo "Failed to download $model"
    fi
    echo "-------------------"
}

# Main loop to download all models
for model in "${models[@]}"; do
    download_model "$model"
done

# List all downloaded models
echo "Downloaded models:"
ollama list

