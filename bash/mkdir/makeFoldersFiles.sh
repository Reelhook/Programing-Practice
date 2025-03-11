#!/bin/bash
path='/lvl1/lvl2/'
# Create folders and files
for i in {1..10}
do

    mkdir -p "folders/folder$i$path"          # Create a subfolder named folder1, folder2, ..., folder10
    touch "folders/folder$i$path$i.txt" 
    # Create a file named 1.txt in each respective folder
    touch "folders/folder$i$path$i.sh"    # Create a file named 1.txt in each respective folder
done

echo "Folders and files created successfully!"

