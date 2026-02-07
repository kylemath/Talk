# Attentional Blink Research Project

This directory contains research materials and an automated paper pipeline for studying the Attentional Blink phenomenon.

## 📁 Folder Structure

```
.
├── references/          # Research papers and literature
│   ├── *.pdf           # Downloaded research papers (5 PDFs)
│   ├── attentional_blink_studies.md  # Literature review
│   └── readme.md       # Original readme
│
├── demo-app/           # Interactive web demo
│   ├── index.html      # Main HTML page
│   ├── script.js       # Interactive JavaScript
│   ├── styles.css      # Styling and layout
│   └── README.md       # Demo documentation
│
└── paper/              # Automated paper pipeline
    ├── paper.tex       # LaTeX manuscript
    ├── paper.pdf       # Compiled PDF output
    ├── references.bib  # Bibliography database
    ├── generate_figures.py     # Figure generation script
    ├── generate_statistics.py  # Statistics generation script
    ├── requirements.txt        # Python dependencies
    ├── Makefile        # Build automation
    ├── build.sh        # Shell build script
    ├── README_PIPELINE.md  # Detailed pipeline documentation
    ├── figures/        # Generated figures (PDF + PNG)
    ├── statistics.txt  # Generated statistics
    └── venv/           # Python virtual environment
```

## 🔬 References Folder

Contains all source materials for the research:

- **5 Research PDFs** (7.1 MB total):
  - Marti & Dehaene (2017) - Discrete and continuous mechanisms
  - Slagter et al. (2017) - Ventral striatum contributions
  - Tang et al. (2020) - Neural dynamics
  - Willems & Martens (2016) - Individual differences
  - Zivony & Lamy (2022) - ERP review

- **Literature Review** (`attentional_blink_studies.md`):
  - Comprehensive summary of 8 highly-cited studies
  - APA citations with summaries
  - PDF download links

## 🎮 Demo App Folder

Interactive web-based educational resource:

- **Full-featured web application** with:
  - 6 interactive tabs covering AB theory
  - Dynamic visualizations and charts
  - Mathematical equation rendering
  - Live RSVP demo you can try yourself
  
- **To run:**
  ```bash
  cd demo-app
  open index.html
  ```

## 📄 Paper Folder

Contains the complete automated paper pipeline. See `paper/README_PIPELINE.md` for full documentation.

### Quick Start

```bash
cd paper
./build.sh
```

This will:
1. Setup Python virtual environment
2. Generate all figures (5 figures, 10 files)
3. Compute statistics
4. Compile LaTeX paper to PDF

### Generated Output

- **paper.pdf** - 16-page manuscript (330 KB)
- **figures/** - 5 scientific figures in PDF and PNG
- **statistics.txt** - Statistical results

## 🚀 Usage

### To Rebuild the Paper

```bash
cd paper
./build.sh
```

Or using Make:
```bash
cd paper
make all
```

### To View the Paper

```bash
cd paper
open paper.pdf  # macOS
```

### To Modify Figures

```bash
cd paper
# Edit generate_figures.py
./venv/bin/python generate_figures.py
make quick  # Recompile without full bibliography rebuild
```

### To Modify Paper Content

```bash
cd paper
# Edit paper.tex
make quick  # Quick recompile
```

## 📚 Key References

The paper integrates research from these highly-cited studies:

1. **Goodbourn et al. (2016)** - Temporal selection reconsidered
2. **Willems & Martens (2016)** - Individual differences
3. **Slagter et al. (2017)** - Ventral striatum and consciousness
4. **Marti & Dehaene (2017)** - Discrete vs continuous mechanisms
5. **Tang et al. (2020)** - Neural dynamics and encoding
6. **Alef et al. (2020)** - Spatial attention vs conscious perception
7. **Becker et al. (2021)** - Relational account
8. **Zivony & Lamy (2022)** - ERP review and integration

## 🔄 Reproducibility

The paper pipeline is fully reproducible:

- ✅ Fixed random seeds (seed=42)
- ✅ Version-pinned dependencies
- ✅ Automated workflow
- ✅ No manual steps required

## 📖 Documentation

- **references/attentional_blink_studies.md** - Literature review
- **demo-app/README.md** - Interactive demo documentation
- **demo-app/index.html** - Interactive web app (open in browser)
- **paper/README_PIPELINE.md** - Detailed pipeline documentation

## 🛠️ Requirements

### For viewing references:
- PDF reader
- Web browser (for index.html)

### For building paper:
- Python 3.8+
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Make (optional)

---

**Last updated:** February 6, 2026  
**Project:** Attentional Blink Research  
**Author:** K. Mathewson
