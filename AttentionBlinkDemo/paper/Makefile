# Makefile for Attentional Blink Paper Pipeline
# Fully automated paper generation from Python scripts to PDF

.PHONY: all clean setup figures statistics paper view

# Default target: build everything
all: setup figures statistics paper

# Setup virtual environment and install dependencies
setup:
	@echo "Setting up Python virtual environment..."
	python3 -m venv venv
	@echo "Installing dependencies..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@echo "Setup complete!"

# Generate all figures
figures:
	@echo "Generating figures..."
	./venv/bin/python generate_figures.py
	@echo "Figures generated!"

# Generate statistics
statistics:
	@echo "Generating statistics..."
	./venv/bin/python generate_statistics.py
	@echo "Statistics generated!"

# Compile LaTeX paper to PDF
paper: figures statistics
	@echo "Compiling LaTeX paper..."
	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex
	@echo "Paper compiled successfully! Output: paper.pdf"

# Quick compile (skip bibliography updates)
quick:
	@echo "Quick compiling paper..."
	pdflatex paper.tex
	@echo "Quick compile complete!"

# Open the PDF (macOS)
view: paper
	@echo "Opening PDF..."
	open paper.pdf

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -f paper.aux paper.bbl paper.blg paper.log paper.out paper.toc paper.pdf
	rm -rf figures
	rm -f statistics.txt
	@echo "Cleanup complete!"

# Deep clean (including virtual environment)
distclean: clean
	@echo "Deep cleaning..."
	rm -rf venv
	rm -rf __pycache__
	@echo "Deep clean complete!"

# Help target
help:
	@echo "Attentional Blink Paper Pipeline"
	@echo "================================"
	@echo ""
	@echo "Available targets:"
	@echo "  make all        - Complete pipeline: setup, figures, stats, compile"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make figures    - Generate all figures using Python"
	@echo "  make statistics - Generate statistical analyses using Python"
	@echo "  make paper      - Compile LaTeX paper to PDF"
	@echo "  make quick      - Quick compile (skip bibliography)"
	@echo "  make view       - Compile and open PDF (macOS)"
	@echo "  make clean      - Remove generated files"
	@echo "  make distclean  - Remove all generated files including venv"
	@echo "  make help       - Show this help message"
