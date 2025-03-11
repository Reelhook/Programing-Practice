#!/bin/bash

# Check if the directories file is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <directories_file>"
    exit 1
fi

# Set the directories file from the script argument
directories_file="$1"

# Check if the directories file exists
if [ ! -f "$directories_file" ]; then
    echo "Error: The file $directories_file does not exist."
    exit 1
fi

# Define the target directory
target_dir="./target_directory"

# Create the target directory if it doesn't exist
mkdir -p "$target_dir"

# Loop through each directory listed in the file and find .txt files
while read -r dir; do
    if [ -d "$dir" ]; then
        find "$dir" -type f -path "*/lvl1/lvl2/*.txt" | while read -r file; do
            cp "$file" "$target_dir"
            echo "Copied: $file"
        done
    else
        echo "Warning: Directory $dir does not exist. Skipping."
    fi
done < "$directories_file"

echo "All .txt files from the specified directories have been copied to $target_dir successfully!"




