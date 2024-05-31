#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status
set -o pipefail  # Return value of the last command to exit with a non-zero status

mkdir -p pretrained_models

# Download and extract 2stems model
mkdir -p pretrained_models/2stems
curl -o pretrained_models/2stems.tar.gz -L https://github.com/deezer/spleeter/releases/download/v1.4.0/2stems.tar.gz || { echo "Error downloading 2stems model"; exit 1; }
tar -xvzf pretrained_models/2stems.tar.gz -C pretrained_models/2stems || { echo "Error extracting 2stems model"; exit 1; }

# Download and extract 4stems model
mkdir -p pretrained_models/4stems
curl -o pretrained_models/4stems.tar.gz -L https://github.com/deezer/spleeter/releases/download/v1.4.0/4stems.tar.gz || { echo "Error downloading 4stems model"; exit 1; }
tar -xvzf pretrained_models/4stems.tar.gz -C pretrained_models/4stems || { echo "Error extracting 4stems model"; exit 1; }

# Download and extract 5stems model
mkdir -p pretrained_models/5stems
curl -o pretrained_models/5stems.tar.gz -L https://github.com/deezer/spleeter/releases/download/v1.4.0/5stems.tar.gz || { echo "Error downloading 5stems model"; exit 1; }
tar -xvzf pretrained_models/5stems.tar.gz -C pretrained_models/5stems || { echo "Error extracting 5stems model"; exit 1; }

echo "Pre-trained models downloaded and extracted successfully."
