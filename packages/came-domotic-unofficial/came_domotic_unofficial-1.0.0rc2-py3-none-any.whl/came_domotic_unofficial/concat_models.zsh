#!/bin/zsh

# Set the directory containing the model files
MODEL_DIR="models"

# The output file
OUTPUT_FILE="models.py"

# Check if the output file already exists and remove it to start fresh
if [[ -f $OUTPUT_FILE ]]; then
    rm $OUTPUT_FILE
fi

# Loop through all Python files in the directory
for file in $MODEL_DIR/*.py; do
    # Skip __init__.py to prevent it from being added to the combined file
    if [[ $file == *"__init__.py" ]]; then
        continue
    fi

    # Append the contents of the file to the output file
    cat $file >> $OUTPUT_FILE
    
    # Append three blank lines after the contents of each file
    echo -e "\n\n\n" >> $OUTPUT_FILE
done

# Print a message when done
echo "All models have been concatenated into $OUTPUT_FILE"

