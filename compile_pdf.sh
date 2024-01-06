#!/bin/bash

# Check if the 'main.tex' file exists
if [ ! -f "main.tex" ]; then
    echo "Error: 'main.tex' file not found!"
    exit 1
fi

# first compile all other tex files
# find . -maxdepth 1 -name "*.tex" ! -name "main.tex" -print0 | while IFS= read -r -d $'\0' file; do
#     # Compile each .tex file with latexmk
#     latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf "$file"
# done

# Compile 'main.tex' to PDF using pdflatex (you can change the compiler if needed)
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf main.tex


# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. PDF saved."

    # # Clean up unnecessary files (log files, auxiliary files)
    # find . -type f -regex '.*\.\(aux\|log\|toc\|out\|gz\|bbl\|blg\|snm\|nav\|vrb\|fls\|fdb_latexmk\|synctex.gz\)' -exec rm {} \;
    # run py script to clean up unnecessary files
    # wait for 5 seconds
    sleep 5
    python remove_aux.py --not_remove_pdf
else
    echo "Compilation failed. Check for LaTeX errors."
    # clean everything except log files
    python remove_aux.py --debug --not_remove_pdf
fi

