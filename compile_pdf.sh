#!/bin/bash

# Check if the 'main.tex' file exists
if [ ! -f "main.tex" ]; then
    echo "Error: 'main.tex' file not found!"
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p output

# Compile 'main.tex' to PDF using pdflatex (you can change the compiler if needed)
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=output main.tex


# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. PDF saved in 'output' directory."

    # # Clean up unnecessary files (log files, auxiliary files)
    # find . -type f -regex '.*\.\(aux\|log\|toc\|out\|gz\|bbl\|blg\|snm\|nav\|vrb\|fls\|fdb_latexmk\|synctex.gz\)' -exec rm {} \;
    # run py script to clean up unnecessary files
    python remove_aux.py
else
    echo "Compilation failed. Check for LaTeX errors."
    # clean everything except log files
    python remove_aux.py --debug
fi

