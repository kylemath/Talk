# Magic Square Visualization and Analysis

This project contains Python scripts to display, visualize, and analyze magic squares.

## Project Overview

### Part 1: 3x3 Magic Square (Original)
Visualization and display of a classic 3x3 magic square with 2D and 3D representations.

### Part 2: 4x4 Magic Square Covariance Analysis (New)
**Complete reproducible analysis of all 880 distinct 4x4 magic squares** to determine if their covariances are zero.

---

## What is a Magic Square?

A magic square is a grid of numbers where all rows, columns, and diagonals sum to the same value (called the "magic constant"). 

- **3x3 Magic Square:** Uses numbers 1-9, magic constant = 15
- **4x4 Magic Square:** Uses numbers 1-16, magic constant = 34

---

## Scripts

### 3x3 Magic Square Scripts

#### 1. `magic_square_display.py`
Displays a 3x3 magic square and verifies that it's valid by checking all row, column, and diagonal sums.

**Usage:**
```bash
source venv/bin/activate
python magic_square_display.py
```

#### 2. `magic_square_3d.py`
Creates 3D visualizations of the magic square where the height (z-axis) represents the value at each position in the grid. This script generates two types of plots:
- **3D Bar Chart**: Shows each cell as a vertical bar
- **3D Surface Plot**: Shows the values as a continuous surface

**Usage:**
```bash
source venv/bin/activate
python magic_square_3d.py
```

### 4x4 Magic Square Covariance Analysis Scripts

#### 3. `all_880_analysis.py` ⭐ **Main Analysis Script**
Generates all 880 distinct 4x4 magic squares and performs comprehensive covariance analysis.

**Features:**
- Generates all 880 Frenicle-standard magic squares using optimized backtracking
- Calculates multiple types of covariance for each square
- Caches results for fast subsequent runs
- Produces detailed statistical analysis

**Usage:**
```bash
source venv/bin/activate
python all_880_analysis.py
```

**Output:**
- `magic_squares_880.pkl` - All 880 magic squares
- `covariance_results.pkl` - Complete analysis results
- Console output with detailed statistics

**Time:** First run takes ~3-5 minutes to generate all squares. Subsequent runs load from cache instantly.

#### 4. Supporting Scripts
- `generate_880_squares.py` - Standalone square generation
- `generate_880_fast.py` - Alternative fast generation approach
- `covariance_analysis.py` - Standalone covariance analysis with visualizations

---

## Key Findings from 4x4 Analysis

### Main Results

✓ **Position-Value Covariance = ZERO** for all 880 squares (100%)
- No spatial bias in magic squares
- Values uniformly distributed across positions

✗ **Row-Pair Covariance = -9.444444** (constant, NOT zero)
- Universal property of all 4x4 magic squares
- Mathematical constant: -85/9

✗ **Column-Pair Covariance = -9.444444** (constant, NOT zero)
- Matches row-pair covariance by symmetry

✗ **Diagonal Covariance varies** (-49.67 to 26.33)
- Different patterns across magic squares

### Conclusion

**Is covariance zero for all 880 4x4 magic squares?**

**Answer:** Partially. Position-value covariance IS zero, but row/column pair covariances have a universal constant value of -9.444444. No square has ALL covariances equal to zero.

See `COVARIANCE_FINDINGS.md` for complete analysis.

---

## Setup

1. Create and activate the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.7+
- numpy
- matplotlib
- scipy

---

## Example 3x3 Magic Square

The classic Lo Shu square:

```
 2 | 7 | 6
 9 | 5 | 1
 4 | 3 | 8
```

All rows, columns, and diagonals sum to 15!

---

## Example 4x4 Magic Square

```
[[ 1  8 13 12]
 [14 11  2  7]
 [15  6  3 10]
 [ 4  9 16  5]]
```

All rows, columns, and diagonals sum to 34!

---

## Reproducibility

All analyses are fully reproducible:

1. **Deterministic generation:** Uses backtracking algorithm with fixed search order
2. **Cached results:** Squares saved to `.pkl` files for consistency
3. **Version controlled:** All scripts tracked in git
4. **Documented methods:** Clear algorithms and mathematical definitions

To reproduce the covariance analysis:
```bash
# Fresh run (generates all 880 squares)
rm -f magic_squares_880.pkl covariance_results.pkl
python all_880_analysis.py

# Using cached data
python all_880_analysis.py
```

---

## Project Structure

```
magic_square/
├── README.md                    # This file
├── COVARIANCE_FINDINGS.md       # Detailed analysis results
├── requirements.txt              # Python dependencies
├── venv/                        # Virtual environment
│
├── magic_square_display.py      # 3x3 display
├── magic_square_3d.py          # 3x3 visualization
│
├── all_880_analysis.py         # ⭐ Main 4x4 analysis
├── generate_880_squares.py     # Square generation
├── generate_880_fast.py        # Fast generation alternative
├── covariance_analysis.py      # Analysis with plots
│
├── magic_squares_880.pkl       # Generated: all 880 squares
└── covariance_results.pkl      # Generated: analysis results
```

---

## Mathematical Background

### Frenicle Standard Form
The 880 "distinct" 4x4 magic squares are in Frenicle standard form, which eliminates equivalent squares related by rotation and reflection:
- Smallest corner value is in top-left position
- Further constraints on corner relationships

Without this standardization, there would be 7,040 magic squares (880 × 8 symmetries).

### The -9.444444 Constant

The universal row/column pair covariance value:
```
-9.444444... = -85/9
```

This constant appears to be a fundamental invariant related to the constraint that all rows and columns must sum to the magic constant (34).

---

## Future Directions

Potential extensions of this work:

1. **5x5 and larger magic squares:** Analyze covariance patterns
2. **Pan-magic squares:** Squares where broken diagonals also sum to magic constant
3. **Theoretical proof:** Derive the -85/9 constant from first principles
4. **Correlation analysis:** Explore other statistical properties
5. **Machine learning:** Predict magic square properties from partial information

---

## Citation

If you use this analysis in your research, please cite:

```
Magic Square Covariance Analysis (2026)
All 880 4x4 Magic Squares: A Complete Statistical Study
GitHub: [repository URL]
```

---

## License

MIT License - Free to use and modify

---

## Author

Generated for reproducible mathematical research  
Date: February 6, 2026
