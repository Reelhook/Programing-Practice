#!/bin/bash

# Define the target directory
target_dir="target_txt_files"

# Create the target directory if it doesn't exist
mkdir -p "$target_dir"

# Find and copy all .txt files within lvl1/lvl2 subfolders
find . -type f -path "folders/*/lvl1/lvl2/*.txt" -exec cp {} "$target_dir" \;

echo "All .txt files from lvl1/lvl2 subfolders have been copied to $target_dir successfully!"

