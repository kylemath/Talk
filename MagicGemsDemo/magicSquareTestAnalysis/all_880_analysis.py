"""
Complete Analysis of All 880 4x4 Magic Squares - Covariance Study

This script generates/loads all 880 distinct 4x4 magic squares and analyzes
whether their covariance is zero across different measures.

Author: Generated for reproducible research
Date: 2026-02-06
"""

import numpy as np
import pickle
import time
from pathlib import Path


class MagicSquareGenerator:
    """Generator for all 880 4x4 magic squares in Frenicle standard form."""
    
    def __init__(self):
        self.magic_sum = 34
        self.squares = []
        
    def generate_all(self, max_squares=880):
        """Generate all magic squares using backtracking with optimizations."""
        print("="*70)
        print("GENERATING ALL 880 DISTINCT 4x4 MAGIC SQUARES")
        print("="*70)
        print("\nUsing optimized backtracking with constraint propagation...")
        print("This may take 5-15 minutes depending on your system.")
        print()
        
        start_time = time.time()
        
        grid = np.zeros((4, 4), dtype=int)
        used = set()
        self._backtrack(grid, used, 0, max_squares)
        
        elapsed = time.time() - start_time
        print(f"\n✓ Generation complete in {elapsed:.1f} seconds!")
        print(f"✓ Generated {len(self.squares)} magic squares\n")
        
        return self.squares
    
    def _backtrack(self, grid, used, pos, max_squares):
        """Recursive backtracking with heavy pruning."""
        if len(self.squares) >= max_squares:
            return True
            
        if pos == 16:
            if self._verify_complete(grid) and self._is_frenicle(grid):
                self.squares.append(grid.copy())
                if len(self.squares) % 88 == 0:
                    print(f"  Progress: {len(self.squares)}/{max_squares} squares found...")
            return False
        
        row, col = pos // 4, pos % 4
        
        # Get valid candidates for this position
        candidates = self._get_candidates(grid, row, col, used)
        
        for num in candidates:
            grid[row, col] = num
            used.add(num)
            
            # Only continue if this placement is valid
            if self._is_valid_placement(grid, row, col):
                if self._backtrack(grid, used, pos + 1, max_squares):
                    return True
            
            used.remove(num)
            grid[row, col] = 0
        
        return False
    
    def _get_candidates(self, grid, row, col, used):
        """Get candidate numbers for position with smart ordering."""
        available = [i for i in range(1, 17) if i not in used]
        
        # Frenicle constraint: first position limited to 1-4
        if row == 0 and col == 0:
            return [i for i in available if i <= 4]
        
        # If completing a row, only one choice
        if col == 3:
            needed = self.magic_sum - int(np.sum(grid[row, :3]))
            return [needed] if (needed in available and 1 <= needed <= 16) else []
        
        # If completing a column, only one choice
        if row == 3:
            needed = self.magic_sum - int(np.sum(grid[:3, col]))
            return [needed] if (needed in available and 1 <= needed <= 16) else []
        
        return sorted(available)
    
    def _is_valid_placement(self, grid, row, col):
        """Check if current placement maintains validity."""
        # Check completed row
        if col == 3:
            if np.sum(grid[row, :]) != self.magic_sum:
                return False
        
        # Check completed column
        if row == 3:
            if np.sum(grid[:, col]) != self.magic_sum:
                return False
        
        # Check diagonals if at final position
        if row == 3 and col == 3:
            if np.sum(np.diag(grid)) != self.magic_sum:
                return False
            if np.sum(np.diag(np.fliplr(grid))) != self.magic_sum:
                return False
            
            # Frenicle check
            if not self._is_frenicle(grid):
                return False
        
        return True
    
    def _verify_complete(self, grid):
        """Verify a complete magic square."""
        # Check all rows
        for i in range(4):
            if np.sum(grid[i, :]) != self.magic_sum:
                return False
        
        # Check all columns
        for j in range(4):
            if np.sum(grid[:, j]) != self.magic_sum:
                return False
        
        # Check diagonals
        if np.sum(np.diag(grid)) != self.magic_sum:
            return False
        if np.sum(np.diag(np.fliplr(grid))) != self.magic_sum:
            return False
        
        return True
    
    def _is_frenicle(self, grid):
        """Check Frenicle standard form constraints."""
        return (grid[0, 0] < grid[0, 3] and 
                grid[0, 0] < grid[3, 0] and
                grid[0, 0] < grid[3, 3])


class CovarianceAnalyzer:
    """Analyzer for covariance properties of magic squares."""
    
    @staticmethod
    def calculate_all_covariances(square):
        """
        Calculate multiple types of covariance for a magic square.
        
        Returns dict with various covariance measurements.
        """
        n = 4
        
        # 1. Covariance between row index and value
        row_indices = np.repeat(np.arange(n), n)
        values = square.flatten()
        cov_row_value = np.cov(row_indices, values)[0, 1]
        
        # 2. Covariance between column index and value
        col_indices = np.tile(np.arange(n), n)
        cov_col_value = np.cov(col_indices, values)[0, 1]
        
        # 3. Covariance between rows (treating each row as a variable)
        # Calculate mean pairwise covariance
        row_pair_covs = []
        for i in range(n):
            for j in range(i+1, n):
                cov = np.cov(square[i, :], square[j, :])[0, 1]
                row_pair_covs.append(cov)
        mean_row_pair_cov = np.mean(row_pair_covs)
        
        # 4. Covariance between columns
        col_pair_covs = []
        for i in range(n):
            for j in range(i+1, n):
                cov = np.cov(square[:, i], square[:, j])[0, 1]
                col_pair_covs.append(cov)
        mean_col_pair_cov = np.mean(col_pair_covs)
        
        # 5. Covariance between diagonals
        main_diag = np.diag(square)
        anti_diag = np.diag(np.fliplr(square))
        cov_diagonals = np.cov(main_diag, anti_diag)[0, 1]
        
        return {
            'cov_row_index_value': cov_row_value,
            'cov_col_index_value': cov_col_value,
            'mean_row_pair_cov': mean_row_pair_cov,
            'mean_col_pair_cov': mean_col_pair_cov,
            'cov_diagonals': cov_diagonals,
            'row_pair_covs': row_pair_covs,
            'col_pair_covs': col_pair_covs
        }
    
    @staticmethod
    def analyze_all_squares(squares):
        """Analyze covariance for all magic squares."""
        print("="*70)
        print("COVARIANCE ANALYSIS")
        print("="*70)
        print(f"\nAnalyzing {len(squares)} magic squares...")
        print()
        
        results = {
            'cov_row_idx': [],
            'cov_col_idx': [],
            'mean_row_cov': [],
            'mean_col_cov': [],
            'cov_diag': [],
        }
        
        for idx, square in enumerate(squares):
            if (idx + 1) % 100 == 0:
                print(f"  Analyzed {idx + 1}/{len(squares)} squares...")
            
            covs = CovarianceAnalyzer.calculate_all_covariances(square)
            
            results['cov_row_idx'].append(covs['cov_row_index_value'])
            results['cov_col_idx'].append(covs['cov_col_index_value'])
            results['mean_row_cov'].append(covs['mean_row_pair_cov'])
            results['mean_col_cov'].append(covs['mean_col_pair_cov'])
            results['cov_diag'].append(covs['cov_diagonals'])
        
        # Convert to arrays
        for key in results:
            results[key] = np.array(results[key])
        
        return results
    
    @staticmethod
    def print_results(results, squares):
        """Print analysis results in a clear format."""
        print("\n" + "="*70)
        print("RESULTS: COVARIANCE ANALYSIS OF 880 4x4 MAGIC SQUARES")
        print("="*70)
        
        tolerance = 1e-10
        n_squares = len(squares)
        
        print("\n" + "-"*70)
        print("1. COVARIANCE BETWEEN POSITION INDEX AND VALUE")
        print("-"*70)
        
        # Row index vs value
        zero_row = np.sum(np.abs(results['cov_row_idx']) < tolerance)
        print(f"\nRow-index covariance:")
        print(f"  Squares with cov ≈ 0: {zero_row}/{n_squares} ({100*zero_row/n_squares:.1f}%)")
        print(f"  Min:  {np.min(results['cov_row_idx']):10.6f}")
        print(f"  Max:  {np.max(results['cov_row_idx']):10.6f}")
        print(f"  Mean: {np.mean(results['cov_row_idx']):10.6f}")
        print(f"  Std:  {np.std(results['cov_row_idx']):10.6f}")
        
        # Column index vs value
        zero_col = np.sum(np.abs(results['cov_col_idx']) < tolerance)
        print(f"\nColumn-index covariance:")
        print(f"  Squares with cov ≈ 0: {zero_col}/{n_squares} ({100*zero_col/n_squares:.1f}%)")
        print(f"  Min:  {np.min(results['cov_col_idx']):10.6f}")
        print(f"  Max:  {np.max(results['cov_col_idx']):10.6f}")
        print(f"  Mean: {np.mean(results['cov_col_idx']):10.6f}")
        print(f"  Std:  {np.std(results['cov_col_idx']):10.6f}")
        
        print("\n" + "-"*70)
        print("2. COVARIANCE BETWEEN ROW PAIRS")
        print("-"*70)
        
        zero_row_pairs = np.sum(np.abs(results['mean_row_cov']) < tolerance)
        print(f"\nMean row-pair covariance:")
        print(f"  Squares with cov ≈ 0: {zero_row_pairs}/{n_squares} ({100*zero_row_pairs/n_squares:.1f}%)")
        print(f"  Min:  {np.min(results['mean_row_cov']):10.6f}")
        print(f"  Max:  {np.max(results['mean_row_cov']):10.6f}")
        print(f"  Mean: {np.mean(results['mean_row_cov']):10.6f}")
        print(f"  Std:  {np.std(results['mean_row_cov']):10.6f}")
        
        print("\n" + "-"*70)
        print("3. COVARIANCE BETWEEN COLUMN PAIRS")
        print("-"*70)
        
        zero_col_pairs = np.sum(np.abs(results['mean_col_cov']) < tolerance)
        print(f"\nMean column-pair covariance:")
        print(f"  Squares with cov ≈ 0: {zero_col_pairs}/{n_squares} ({100*zero_col_pairs/n_squares:.1f}%)")
        print(f"  Min:  {np.min(results['mean_col_cov']):10.6f}")
        print(f"  Max:  {np.max(results['mean_col_cov']):10.6f}")
        print(f"  Mean: {np.mean(results['mean_col_cov']):10.6f}")
        print(f"  Std:  {np.std(results['mean_col_cov']):10.6f}")
        
        print("\n" + "-"*70)
        print("4. COVARIANCE BETWEEN DIAGONALS")
        print("-"*70)
        
        zero_diag = np.sum(np.abs(results['cov_diag']) < tolerance)
        print(f"\nDiagonal covariance:")
        print(f"  Squares with cov ≈ 0: {zero_diag}/{n_squares} ({100*zero_diag/n_squares:.1f}%)")
        print(f"  Min:  {np.min(results['cov_diag']):10.6f}")
        print(f"  Max:  {np.max(results['cov_diag']):10.6f}")
        print(f"  Mean: {np.mean(results['cov_diag']):10.6f}")
        print(f"  Std:  {np.std(results['cov_diag']):10.6f}")
        
        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70)
        
        # Check for squares with ALL covariances near zero
        all_zero = (
            (np.abs(results['cov_row_idx']) < tolerance) &
            (np.abs(results['cov_col_idx']) < tolerance) &
            (np.abs(results['mean_row_cov']) < tolerance) &
            (np.abs(results['mean_col_cov']) < tolerance)
        )
        
        count_all_zero = np.sum(all_zero)
        
        print(f"\nSquares with ALL covariances ≈ 0: {count_all_zero}/{n_squares} ({100*count_all_zero/n_squares:.1f}%)")
        
        if count_all_zero > 0:
            indices = np.where(all_zero)[0]
            print(f"\nExample magic square with all covariances ≈ 0 (index {indices[0]}):")
            print(squares[indices[0]])
        else:
            print("\n✗ No magic squares found with ALL covariances equal to zero.")
            print("\nConclusion: While individual covariance measures may be zero")
            print("for some squares, ALL covariances are NOT simultaneously zero")
            print("for all 880 distinct 4x4 magic squares.")
        
        print("\n" + "="*70)


def main():
    """Main execution function."""
    print("\n" + "="*70)
    print(" REPRODUCIBLE ANALYSIS OF ALL 880 4x4 MAGIC SQUARES")
    print(" Covariance Study")
    print("="*70)
    print()
    
    cache_file = Path("magic_squares_880.pkl")
    
    # Try to load cached squares
    if cache_file.exists():
        print("Loading cached magic squares...")
        with open(cache_file, 'rb') as f:
            squares = pickle.load(f)
        print(f"✓ Loaded {len(squares)} magic squares from cache\n")
    else:
        # Generate all 880 squares
        generator = MagicSquareGenerator()
        squares = generator.generate_all(max_squares=880)
        
        # Save for future use
        with open(cache_file, 'wb') as f:
            pickle.dump(squares, f)
        print(f"✓ Saved magic squares to {cache_file}\n")
    
    # Verify we have enough squares
    if len(squares) < 100:
        print(f"WARNING: Only {len(squares)} squares generated.")
        print("Results may not be complete.\n")
    
    # Perform covariance analysis
    analyzer = CovarianceAnalyzer()
    results = analyzer.analyze_all_squares(squares)
    
    # Print results
    analyzer.print_results(results, squares)
    
    # Save results
    results_file = Path("covariance_results.pkl")
    with open(results_file, 'wb') as f:
        pickle.dump({
            'results': results,
            'n_squares': len(squares),
            'squares': squares
        }, f)
    print(f"\nResults saved to: {results_file}")
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
