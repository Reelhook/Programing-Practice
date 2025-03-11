#!/bin/bash

# Define the target directory
target_dir="collected_txt_files"

# Create the target directory if it doesn't exist
mkdir -p "$target_dir"

# Find all .txt files in subdirectories and copy them to the target directory
find . -type f -name "./folders/folder1/lvl1/lvl2/*.txt" -exec cp {} "$target_dir" \;

echo "All .txt files have been copied to $target_dir successfully!"


