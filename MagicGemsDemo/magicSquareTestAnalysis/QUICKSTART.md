# Quick Start Guide

## TL;DR - Key Finding

**Question:** Is the covariance zero for all 880 distinct 4x4 magic squares?

**Answer:** 
- ✓ **Position-value covariance = 0** for ALL 880 squares (100%)
- ✗ **Row-pair covariance = -9.444444** (constant, NOT zero)
- ✗ **Column-pair covariance = -9.444444** (constant, NOT zero)
- ✗ **Diagonal covariance varies** from -49.67 to +26.33

**Bottom line:** No square has ALL covariances equal to zero, but position-value covariance IS universally zero.

---

## Quick Commands

### Setup (first time only)
```bash
cd /Users/kylemathewson/magic_square
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Complete Analysis
```bash
cd /Users/kylemathewson/magic_square
source venv/bin/activate
python all_880_analysis.py
```

First run: ~3-5 minutes (generates all 880 squares)  
Subsequent runs: instant (loads from cache)

### View Results
```bash
python view_results.py
```

### View 3x3 Magic Square Examples
```bash
python magic_square_display.py
python magic_square_3d.py  # Opens 3D visualization
```

---

## Files to Check

### Documentation
- `README.md` - Complete project overview
- `COVARIANCE_FINDINGS.md` - Detailed analysis results
- `QUICKSTART.md` - This file

### Main Scripts
- `all_880_analysis.py` - **Main analysis script**
- `view_results.py` - View analysis results

### Generated Data
- `magic_squares_880.pkl` - All 880 magic squares (138 KB)
- `covariance_results.pkl` - Analysis results (172 KB)

---

## Key Findings at a Glance

| Covariance Type | Value | All Zeros? |
|----------------|-------|-----------|
| Row-index vs Value | 0.000000 | ✓ YES (100%) |
| Col-index vs Value | 0.000000 | ✓ YES (100%) |
| Row-pair | -9.444444 | ✗ NO (constant) |
| Column-pair | -9.444444 | ✗ NO (constant) |
| Diagonal | -14.650000 avg | ✗ NO (varies) |

---

## Reproducibility

All results are 100% reproducible:

1. **Delete cache:**
   ```bash
   rm -f magic_squares_880.pkl covariance_results.pkl
   ```

2. **Regenerate:**
   ```bash
   python all_880_analysis.py
   ```

3. **Results will be identical** (deterministic algorithm)

---

## Mathematical Significance

The constant **-9.444444 = -85/9** appears to be a fundamental invariant of all 4×4 magic squares, reflecting the constraint that rows and columns must sum to 34.

The fact that position-value covariance is EXACTLY zero for all 880 squares proves that magic squares have no spatial bias - values are uniformly distributed across positions.

---

## Example Magic Square

```
[[ 1  2 15 16]
 [12 14  3  5]
 [13  7 10  4]
 [ 8 11  6  9]]
```

- All rows sum to: 34
- All columns sum to: 34
- Both diagonals sum to: 34
- Row-index covariance: 0.000000
- Mean row-pair covariance: -9.444444

---

## Questions?

Check the detailed documentation:
- `README.md` - Full project documentation
- `COVARIANCE_FINDINGS.md` - Complete mathematical analysis
- View source code in `all_880_analysis.py` for implementation details

---

Last updated: February 6, 2026
