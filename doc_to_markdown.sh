#!/bin/bash

for file in src/*; do
  if [ -f "$file" ]; then

    # Extraire le nom de fichier sans extension
    filename=$(basename "$file")
    filename_without_extension="${filename%.*}"

    output_file="documentation/${filename_without_extension}.md"
    > "documentation/${filename_without_extension}.md"

    doc_output=$(python -m pydoc "$file")

    while IFS= read -r line; do
       # no spaces
       if [[ "$line" =~ ^[^[:space:]] ]]; then
          echo "# ${line}" >> "$output_file"
       # 4 spaces
       elif [[ "$line" =~ ^[[:space:]]{4}[^[:space:]] && ! "$line" =~ ^[[:space:]]{5,} ]]; then
          echo "## ${line}" >> "$output_file"
       # 8 spaces
       elif [[ "$line" =~ ^[[:space:]]{8}[^[:space:]] && ! "$line" =~ ^[[:space:]]{9,} ]]; then
          echo "### ${line}" >> "$output_file"
       # others
       else
          echo "${line}" >> "$output_file"
       fi
    done <<< "$doc_output"

  fi
done