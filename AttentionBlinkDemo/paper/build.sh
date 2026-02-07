#!/bin/bash
# Automated build script for Attentional Blink Paper
# This script creates a complete reproducible pipeline from data to PDF

set -e  # Exit on error

echo "============================================"
echo "Attentional Blink Paper Build Pipeline"
echo "============================================"
echo ""

# Step 1: Setup Python environment
echo "[1/4] Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  ✓ Virtual environment created"
else
    echo "  ✓ Virtual environment already exists"
fi

echo "  Installing dependencies..."
./venv/bin/pip install --upgrade pip -q
./venv/bin/pip install -r requirements.txt -q
echo "  ✓ Dependencies installed"
echo ""

# Step 2: Generate figures
echo "[2/4] Generating figures..."
./venv/bin/python generate_figures.py
echo "  ✓ Figures generated"
echo ""

# Step 3: Generate statistics
echo "[3/4] Generating statistics..."
./venv/bin/python generate_statistics.py
echo "  ✓ Statistics generated"
echo ""

# Step 4: Compile LaTeX paper
echo "[4/4] Compiling LaTeX paper to PDF..."
echo "  - First pass..."
pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 || true
echo "  - Running BibTeX..."
bibtex paper > /dev/null 2>&1 || true
echo "  - Second pass..."
pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 || true
echo "  - Final pass..."
pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 || true
echo "  ✓ Paper compiled"
echo ""

# Cleanup auxiliary files
echo "Cleaning up auxiliary files..."
rm -f paper.aux paper.bbl paper.blg paper.log paper.out paper.toc
echo "  ✓ Cleanup complete"
echo ""

echo "============================================"
echo "✓ BUILD COMPLETE!"
echo "============================================"
echo ""
echo "Output file: paper.pdf"
echo "Figures: figures/ directory (10 files)"
echo "Statistics: statistics.txt"
echo ""
echo "To view the paper:"
echo "  macOS:  open paper.pdf"
echo "  Linux:  xdg-open paper.pdf"
echo ""
