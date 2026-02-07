"""
Covariance Analysis of All 880 4x4 Magic Squares

This script loads all 880 distinct 4x4 magic squares and analyzes
their covariance properties in various ways.
"""

import numpy as np
import pickle
from pathlib import Path
import matplotlib.pyplot as plt
from generate_880_squares import generate_880_magic_squares, load_magic_squares, save_magic_squares


def calculate_covariances(square):
    """
    Calculate various types of covariance for a magic square.
    
    Args:
        square: 4x4 numpy array
        
    Returns:
        dict: Dictionary containing different covariance measurements
    """
    # Method 1: Covariance between position and value
    positions_row = []
    positions_col = []
    values = []
    
    for i in range(4):
        for j in range(4):
            positions_row.append(i)
            positions_col.append(j)
            values.append(square[i, j])
    
    # Covariance between row position and value
    cov_row_value = np.cov(positions_row, values)[0, 1]
    
    # Covariance between column position and value  
    cov_col_value = np.cov(positions_col, values)[0, 1]
    
    # Method 2: Covariance matrix of the square itself
    # Treat each row as a random variable
    cov_matrix_rows = np.cov(square)
    
    # Method 3: Covariance between rows and columns as vectors
    rows_flat = square.flatten()
    cols_flat = square.T.flatten()
    cov_rows_cols = np.cov(rows_flat, cols_flat)[0, 1]
    
    # Method 4: Mean covariance between all pairs of rows
    row_covs = []
    for i in range(4):
        for j in range(i+1, 4):
            cov_ij = np.cov(square[i, :], square[j, :])[0, 1]
            row_covs.append(cov_ij)
    mean_row_cov = np.mean(row_covs)
    
    # Method 5: Mean covariance between all pairs of columns
    col_covs = []
    for i in range(4):
        for j in range(i+1, 4):
            cov_ij = np.cov(square[:, i], square[:, j])[0, 1]
            col_covs.append(cov_ij)
    mean_col_cov = np.mean(col_covs)
    
    # Method 6: Overall covariance of all values
    overall_cov = np.cov(square.flatten())
    
    return {
        'cov_row_position': cov_row_value,
        'cov_col_position': cov_col_value,
        'cov_rows_cols': cov_rows_cols,
        'mean_row_pair_cov': mean_row_cov,
        'mean_col_pair_cov': mean_col_cov,
        'cov_matrix_rows': cov_matrix_rows,
        'row_covs': row_covs,
        'col_covs': col_covs
    }


def analyze_all_880_squares():
    """
    Main analysis function for all 880 magic squares.
    """
    print("="*70)
    print(" COVARIANCE ANALYSIS OF ALL 880 DISTINCT 4x4 MAGIC SQUARES")
    print("="*70)
    print()
    
    # Load or generate magic squares
    cache_file = "magic_squares_880.pkl"
    squares = load_magic_squares(cache_file)
    
    if squares is None or len(squares) < 880:
        print("Generating magic squares (this may take a few minutes)...")
        squares = generate_880_magic_squares()
        save_magic_squares(squares, cache_file)
    
    print(f"\nAnalyzing {len(squares)} magic squares...")
    print()
    
    # Store results
    results = {
        'cov_row_pos': [],
        'cov_col_pos': [],
        'cov_rows_cols': [],
        'mean_row_cov': [],
        'mean_col_cov': [],
        'all_row_covs': [],
        'all_col_covs': []
    }
    
    # Analyze each square
    for idx, square in enumerate(squares):
        if (idx + 1) % 100 == 0:
            print(f"  Processed {idx + 1}/{len(squares)} squares...")
        
        covs = calculate_covariances(square)
        
        results['cov_row_pos'].append(covs['cov_row_position'])
        results['cov_col_pos'].append(covs['cov_col_position'])
        results['cov_rows_cols'].append(covs['cov_rows_cols'])
        results['mean_row_cov'].append(covs['mean_row_pair_cov'])
        results['mean_col_cov'].append(covs['mean_col_pair_cov'])
        results['all_row_covs'].extend(covs['row_covs'])
        results['all_col_covs'].extend(covs['col_covs'])
    
    print()
    print("="*70)
    print(" RESULTS")
    print("="*70)
    print()
    
    # Convert to numpy arrays
    for key in ['cov_row_pos', 'cov_col_pos', 'cov_rows_cols', 'mean_row_cov', 'mean_col_cov']:
        results[key] = np.array(results[key])
    
    # Check for zero covariances
    tolerance = 1e-10
    
    print("COVARIANCE BETWEEN POSITION AND VALUE:")
    print("-" * 70)
    
    zero_row_pos = np.sum(np.abs(results['cov_row_pos']) < tolerance)
    zero_col_pos = np.sum(np.abs(results['cov_col_pos']) < tolerance)
    
    print(f"Squares with zero row-position covariance: {zero_row_pos}/{len(squares)}")
    print(f"Squares with zero col-position covariance: {zero_col_pos}/{len(squares)}")
    print()
    print(f"Row-position covariance statistics:")
    print(f"  Min:  {np.min(results['cov_row_pos']):12.8f}")
    print(f"  Max:  {np.max(results['cov_row_pos']):12.8f}")
    print(f"  Mean: {np.mean(results['cov_row_pos']):12.8f}")
    print(f"  Std:  {np.std(results['cov_row_pos']):12.8f}")
    print()
    print(f"Column-position covariance statistics:")
    print(f"  Min:  {np.min(results['cov_col_pos']):12.8f}")
    print(f"  Max:  {np.max(results['cov_col_pos']):12.8f}")
    print(f"  Mean: {np.mean(results['cov_col_pos']):12.8f}")
    print(f"  Std:  {np.std(results['cov_col_pos']):12.8f}")
    print()
    
    print("="*70)
    print("COVARIANCE BETWEEN ROW PAIRS:")
    print("-" * 70)
    
    zero_row_pairs = np.sum(np.abs(results['mean_row_cov']) < tolerance)
    print(f"Squares with zero mean row-pair covariance: {zero_row_pairs}/{len(squares)}")
    print()
    print(f"Mean row-pair covariance statistics:")
    print(f"  Min:  {np.min(results['mean_row_cov']):12.8f}")
    print(f"  Max:  {np.max(results['mean_row_cov']):12.8f}")
    print(f"  Mean: {np.mean(results['mean_row_cov']):12.8f}")
    print(f"  Std:  {np.std(results['mean_row_cov']):12.8f}")
    print()
    
    print("="*70)
    print("COVARIANCE BETWEEN COLUMN PAIRS:")
    print("-" * 70)
    
    zero_col_pairs = np.sum(np.abs(results['mean_col_cov']) < tolerance)
    print(f"Squares with zero mean col-pair covariance: {zero_col_pairs}/{len(squares)}")
    print()
    print(f"Mean column-pair covariance statistics:")
    print(f"  Min:  {np.min(results['mean_col_cov']):12.8f}")
    print(f"  Max:  {np.max(results['mean_col_cov']):12.8f}")
    print(f"  Mean: {np.mean(results['mean_col_cov']):12.8f}")
    print(f"  Std:  {np.std(results['mean_col_cov']):12.8f}")
    print()
    
    print("="*70)
    print("OVERALL SUMMARY:")
    print("-" * 70)
    
    # Check which squares have ALL covariances near zero
    all_near_zero = (
        (np.abs(results['cov_row_pos']) < tolerance) &
        (np.abs(results['cov_col_pos']) < tolerance) &
        (np.abs(results['mean_row_cov']) < tolerance) &
        (np.abs(results['mean_col_cov']) < tolerance)
    )
    
    count_all_zero = np.sum(all_near_zero)
    print(f"Squares with ALL covariances ≈ 0: {count_all_zero}/{len(squares)}")
    
    if count_all_zero > 0:
        indices = np.where(all_near_zero)[0]
        print(f"\nIndices of squares with all covariances ≈ 0:")
        print(f"  {indices[:10]}{'...' if len(indices) > 10 else ''}")
        
        print(f"\nExample square with all covariances ≈ 0 (Square #{indices[0]}):")
        print(squares[indices[0]])
    
    # Are most covariances zero?
    print(f"\nPercentage of squares with near-zero row-position cov: {100*zero_row_pos/len(squares):.1f}%")
    print(f"Percentage of squares with near-zero col-position cov: {100*zero_col_pos/len(squares):.1f}%")
    print(f"Percentage of squares with near-zero mean row-pair cov: {100*zero_row_pairs/len(squares):.1f}%")
    print(f"Percentage of squares with near-zero mean col-pair cov: {100*zero_col_pairs/len(squares):.1f}%")
    
    print()
    print("="*70)
    
    # Save results
    output_file = "covariance_analysis_results.pkl"
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)
    print(f"\nDetailed results saved to: {output_file}")
    
    # Create visualizations
    create_visualizations(results, squares)
    
    return results, squares


def create_visualizations(results, squares):
    """Create visualizations of the covariance analysis."""
    print("\nGenerating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Covariance Analysis of 880 4x4 Magic Squares', fontsize=16, fontweight='bold')
    
    # Plot 1: Row-position covariance distribution
    ax = axes[0, 0]
    ax.hist(results['cov_row_pos'], bins=50, edgecolor='black', alpha=0.7)
    ax.axvline(0, color='red', linestyle='--', linewidth=2, label='Zero')
    ax.set_xlabel('Row-Position Covariance', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Distribution of Row-Position Covariance', fontsize=13, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Column-position covariance distribution
    ax = axes[0, 1]
    ax.hist(results['cov_col_pos'], bins=50, edgecolor='black', alpha=0.7, color='orange')
    ax.axvline(0, color='red', linestyle='--', linewidth=2, label='Zero')
    ax.set_xlabel('Column-Position Covariance', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Distribution of Column-Position Covariance', fontsize=13, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Mean row-pair covariance distribution
    ax = axes[1, 0]
    ax.hist(results['mean_row_cov'], bins=50, edgecolor='black', alpha=0.7, color='green')
    ax.axvline(0, color='red', linestyle='--', linewidth=2, label='Zero')
    ax.set_xlabel('Mean Row-Pair Covariance', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Distribution of Mean Row-Pair Covariance', fontsize=13, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Mean column-pair covariance distribution
    ax = axes[1, 1]
    ax.hist(results['mean_col_cov'], bins=50, edgecolor='black', alpha=0.7, color='purple')
    ax.axvline(0, color='red', linestyle='--', linewidth=2, label='Zero')
    ax.set_xlabel('Mean Column-Pair Covariance', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Distribution of Mean Column-Pair Covariance', fontsize=13, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_fig = "covariance_distributions.png"
    plt.savefig(output_fig, dpi=150, bbox_inches='tight')
    print(f"Visualization saved to: {output_fig}")
    
    plt.show()


if __name__ == "__main__":
    # Run the complete analysis
    results, squares = analyze_all_880_squares()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
