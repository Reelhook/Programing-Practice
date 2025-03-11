#!/bin/bash

# Check if a target directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <target_directory>"
    exit 1
fi

# Set the target directory from the script argument
target_dir="$1"

# Create the target directory if it doesn't exist
mkdir -p "$target_dir"

# Find and copy all .txt files from lv2 subfolders into the target directory
find . -type f -path "*/lvl1/lvl2/*.txt" | while read file; do
    cp "$file" "$target_dir"
    echo "Copied: $file"
done

echo "All .txt files from lv2 subfolders have been copied to $target_dir successfully!"





