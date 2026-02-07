"""
Quick viewer for magic square analysis results.

Displays example magic squares and their covariance properties.
"""

import numpy as np
import pickle
from pathlib import Path


def load_results():
    """Load the analysis results."""
    results_file = Path("covariance_results.pkl")
    if not results_file.exists():
        print("Error: Run all_880_analysis.py first to generate results.")
        return None
    
    with open(results_file, 'rb') as f:
        data = pickle.load(f)
    
    return data


def display_square_with_covariance(square, idx, cov_data):
    """Display a magic square with its covariance properties."""
    print(f"\n{'='*60}")
    print(f"Magic Square #{idx + 1}")
    print(f"{'='*60}")
    print("\nSquare:")
    print(square)
    
    print("\nVerification:")
    print(f"  Row sums: {[np.sum(square[i, :]) for i in range(4)]}")
    print(f"  Col sums: {[np.sum(square[:, j]) for j in range(4)]}")
    print(f"  Main diagonal sum: {np.sum(np.diag(square))}")
    print(f"  Anti-diagonal sum: {np.sum(np.diag(np.fliplr(square)))}")
    
    print("\nCovariances:")
    print(f"  Row-index vs value:    {cov_data['cov_row_idx'][idx]:10.6f}")
    print(f"  Col-index vs value:    {cov_data['cov_col_idx'][idx]:10.6f}")
    print(f"  Mean row-pair cov:     {cov_data['mean_row_cov'][idx]:10.6f}")
    print(f"  Mean col-pair cov:     {cov_data['mean_col_cov'][idx]:10.6f}")
    print(f"  Diagonal cov:          {cov_data['cov_diag'][idx]:10.6f}")


def main():
    """Main function to display results."""
    print("\n" + "="*60)
    print(" MAGIC SQUARE COVARIANCE ANALYSIS - RESULTS VIEWER")
    print("="*60)
    
    data = load_results()
    if data is None:
        return
    
    squares = data['squares']
    results = data['results']
    n_squares = data['n_squares']
    
    print(f"\nLoaded results for {n_squares} magic squares")
    
    # Display summary statistics
    print("\n" + "-"*60)
    print("SUMMARY STATISTICS")
    print("-"*60)
    
    print("\nPosition-Value Covariances:")
    print(f"  Row-index covariance: {np.mean(results['cov_row_idx']):.8f} "
          f"(all zeros: {np.all(results['cov_row_idx'] == 0)})")
    print(f"  Col-index covariance: {np.mean(results['cov_col_idx']):.8f} "
          f"(all zeros: {np.all(results['cov_col_idx'] == 0)})")
    
    print("\nRow/Column Pair Covariances:")
    print(f"  Mean row-pair cov: {np.mean(results['mean_row_cov']):.8f} "
          f"(constant: {np.std(results['mean_row_cov']) < 1e-10})")
    print(f"  Mean col-pair cov: {np.mean(results['mean_col_cov']):.8f} "
          f"(constant: {np.std(results['mean_col_cov']) < 1e-10})")
    
    print("\nDiagonal Covariance:")
    print(f"  Min:  {np.min(results['cov_diag']):10.6f}")
    print(f"  Max:  {np.max(results['cov_diag']):10.6f}")
    print(f"  Mean: {np.mean(results['cov_diag']):10.6f}")
    
    # Show example squares
    print("\n" + "="*60)
    print("EXAMPLE MAGIC SQUARES")
    print("="*60)
    
    # Square with minimum diagonal covariance
    min_diag_idx = np.argmin(results['cov_diag'])
    print("\n[1] Square with MINIMUM diagonal covariance:")
    display_square_with_covariance(squares[min_diag_idx], min_diag_idx, results)
    
    # Square with maximum diagonal covariance
    max_diag_idx = np.argmax(results['cov_diag'])
    print("\n[2] Square with MAXIMUM diagonal covariance:")
    display_square_with_covariance(squares[max_diag_idx], max_diag_idx, results)
    
    # First few squares
    print("\n[3] First magic square:")
    display_square_with_covariance(squares[0], 0, results)
    
    print("\n[4] 100th magic square:")
    display_square_with_covariance(squares[99], 99, results)
    
    print("\n[5] Last magic square:")
    display_square_with_covariance(squares[-1], len(squares)-1, results)
    
    print("\n" + "="*60)
    print("KEY FINDINGS")
    print("="*60)
    print("\n✓ Position-value covariance = 0 for ALL squares")
    print("✓ Row/column pair covariance = -9.444444 (constant) for ALL squares")
    print("✓ Diagonal covariance varies across squares")
    print("✗ NO square has ALL covariances equal to zero")
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
