# Automated Attentional Blink Paper Pipeline

A fully reproducible pipeline for generating an academic paper on the Attentional Blink, complete with Python-generated figures, statistics, and automated LaTeX compilation.

## Overview

This pipeline automatically:
1. ✅ Generates scientific figures using Python (matplotlib/seaborn)
2. ✅ Computes statistical analyses with simulated data
3. ✅ Compiles a complete LaTeX manuscript with references
4. ✅ Produces a publication-ready PDF

## Quick Start

### Option 1: Using Make (Recommended)

```bash
make all
```

This single command will:
- Create a Python virtual environment
- Install dependencies
- Generate all figures
- Compute statistics
- Compile the paper to PDF

### Option 2: Using Shell Script

```bash
chmod +x build.sh
./build.sh
```

### Option 3: Manual Steps

```bash
# 1. Setup environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Generate figures
python generate_figures.py

# 3. Generate statistics
python generate_statistics.py

# 4. Compile paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

## File Structure

```
.
├── README_PIPELINE.md          # This file
├── requirements.txt            # Python dependencies
├── Makefile                    # Automated build system
├── build.sh                    # Shell script alternative
│
├── generate_figures.py         # Figure generation script
├── generate_statistics.py      # Statistical analysis script
│
├── paper.tex                   # Main LaTeX manuscript
├── references.bib              # Bibliography database
│
├── attentional_blink_studies.md  # Literature review source
├── index.html                     # Background information source
│
├── figures/                    # Generated figures (auto-created)
│   ├── ab_curve.pdf
│   ├── ab_curve.png
│   ├── erp_timeline.pdf
│   ├── erp_timeline.png
│   ├── individual_differences.pdf
│   ├── individual_differences.png
│   ├── dual_process.pdf
│   ├── dual_process.png
│   ├── neural_oscillations.pdf
│   └── neural_oscillations.png
│
├── statistics.txt              # Generated statistics (auto-created)
└── paper.pdf                   # Final output (auto-created)
```

## Requirements

### System Requirements
- Python 3.8 or higher
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Make (optional, for Makefile)

### Python Packages (auto-installed)
- numpy 1.24.3
- matplotlib 3.7.1
- scipy 1.10.1
- pandas 2.0.2
- seaborn 0.12.2

### LaTeX Packages (usually included in distributions)
- natbib (citations)
- graphicx (figures)
- amsmath (equations)
- hyperref (links)
- booktabs (tables)

## Generated Outputs

### Figures (5 figures, 10 files total)

1. **ab_curve.pdf/png** - Classic attentional blink curve showing T2 accuracy by lag
2. **erp_timeline.pdf/png** - ERP component timeline (P1, N2pc, N400, P3b)
3. **individual_differences.pdf/png** - Working memory capacity vs AB magnitude correlation
4. **dual_process.pdf/png** - Continuous vs discrete processing stages
5. **neural_oscillations.pdf/png** - Alpha/beta oscillations for seen vs missed targets

### Statistics File

`statistics.txt` contains:
- Experiment 1: Basic AB magnitude analysis (t-tests, ANOVA)
- Experiment 2: Individual differences correlation
- Experiment 3: ERP component comparisons (N2pc, P3b)

### Final Paper

`paper.pdf` includes:
- Title page with author information
- Abstract (250 words)
- Table of contents
- Introduction (4 pages)
- Methods (3 pages)
- Results with embedded figures and statistics (4 pages)
- Discussion (4 pages)
- References (10 key citations)
- Total: ~16 pages

## Makefile Targets

```bash
make all        # Complete pipeline (recommended)
make setup      # Setup Python environment
make figures    # Generate figures only
make statistics # Generate statistics only
make paper      # Compile LaTeX to PDF
make quick      # Quick compile (skip bibliography)
make view       # Compile and open PDF (macOS)
make clean      # Remove generated files
make distclean  # Remove everything including venv
make help       # Show help message
```

## Reproducibility

This pipeline is **fully reproducible**:

- ✅ **Fixed random seed** (seed=42) in all Python scripts
- ✅ **Version-pinned dependencies** in requirements.txt
- ✅ **Documented parameters** in all analysis scripts
- ✅ **Automated workflow** via Makefile/shell script
- ✅ **No manual steps** required

To reproduce on any system:
```bash
git clone <repository>
cd <repository>
make all
```

## Customization

### Modify Figures
Edit `generate_figures.py`:
- Change color schemes (lines 11-13)
- Adjust figure dimensions (figsize parameters)
- Modify data parameters (e.g., lag values, noise levels)

### Modify Statistics
Edit `generate_statistics.py`:
- Change sample sizes (n_subjects)
- Adjust effect sizes
- Add new analyses

### Modify Paper Content
Edit `paper.tex`:
- Update title, authors, affiliations
- Modify text in any section
- Add/remove figures using `\includegraphics{}`

### Add References
Edit `references.bib`:
- Add new `@article{}` entries
- Cite in paper using `\citep{}` or `\citet{}`

## Troubleshooting

### LaTeX not found
**Error:** `pdflatex: command not found`

**Solution:** Install a LaTeX distribution:
- macOS: `brew install --cask mactex`
- Ubuntu: `sudo apt-get install texlive-full`
- Windows: Download MiKTeX from miktex.org

### Missing LaTeX packages
**Error:** `! LaTeX Error: File 'natbib.sty' not found`

**Solution:** Install missing packages:
- TeX Live: `tlmgr install natbib`
- MiKTeX: Packages auto-install on first use

### Python version issues
**Error:** `Python 3.8 or higher required`

**Solution:** Update Python:
- macOS: `brew install python@3.11`
- Ubuntu: `sudo apt-get install python3.11`
- Windows: Download from python.org

### Virtual environment activation
**On Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

## Paper Content

The generated paper covers:

### Introduction
- The attentional blink phenomenon
- Individual differences in AB magnitude
- Current theoretical debates
- Research questions

### Methods
- Experiment 1: Basic AB with 30 subjects, 8 lags
- Experiment 2: ERP recording with 24 subjects
- Experiment 3: Computational modeling

### Results
- Robust AB effect with lag-1 sparing
- Strong correlation (r=-.72) between WM capacity and AB
- ERP dissociations (N2pc delayed, P3b absent for missed targets)
- Dual-process model fits best

### Discussion
- Multi-stage model of temporal attention
- Subcortical contributions (ventral striatum)
- Discrete vs continuous processing reconciliation
- Implications for consciousness theories

## Citation

If you use this pipeline, please cite the key papers referenced:

- Goodbourn et al. (2016) - Temporal selection
- Willems & Martens (2016) - Individual differences
- Slagter et al. (2017) - Ventral striatum
- Marti & Dehaene (2017) - Discrete/continuous processing
- Tang et al. (2020) - Neural dynamics
- Zivony & Lamy (2022) - ERP review

## License

This pipeline is provided for educational and research purposes.

## Contact

For questions or issues with the pipeline, please refer to the documentation or open an issue.

---

**Last updated:** February 6, 2026  
**Pipeline version:** 1.0  
**Python version:** 3.8+  
**LaTeX engine:** pdflatex
