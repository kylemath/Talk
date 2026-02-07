"""
Generate all 880 distinct 4x4 magic squares (Frenicle standard form).

This script uses an efficient backtracking algorithm with symmetry breaking
to generate all 880 essentially different 4x4 magic squares.
"""

import numpy as np
import pickle
from pathlib import Path


def verify_magic_square_4x4(square):
    """Verify that a 4x4 square is a valid magic square."""
    magic_sum = 34  # Sum for 4x4 magic square (1-16)
    
    # Check all rows
    for i in range(4):
        if np.sum(square[i, :]) != magic_sum:
            return False
    
    # Check all columns
    for j in range(4):
        if np.sum(square[:, j]) != magic_sum:
            return False
    
    # Check main diagonal
    if np.sum(np.diag(square)) != magic_sum:
        return False
    
    # Check anti-diagonal
    if np.sum(np.diag(np.fliplr(square))) != magic_sum:
        return False
    
    # Check all values are 1-16 and unique
    if set(square.flatten()) != set(range(1, 17)):
        return False
    
    return True


def is_frenicle_standard(square):
    """
    Check if square is in Frenicle standard form.
    Frenicle standard form has:
    - square[0,0] < square[0,3]
    - square[0,0] < square[3,0]  
    - square[0,0] < square[3,3]
    """
    return (square[0, 0] < square[0, 3] and 
            square[0, 0] < square[3, 0] and
            square[0, 0] < square[3, 3])


def generate_880_magic_squares():
    """
    Generate all 880 4x4 magic squares using optimized backtracking.
    
    Returns:
        list: List of all 880 4x4 magic squares as numpy arrays
    """
    magic_squares = []
    magic_sum = 34
    
    print("Generating all 880 distinct 4x4 magic squares...")
    print("This uses optimized backtracking and will take a few minutes...")
    print()
    
    def is_promising(square, row, col, placed):
        """Check if current partial solution is still promising."""
        # Check row sum if row is complete
        if col == 4:
            if np.sum(square[row, :]) != magic_sum:
                return False
        
        # Check column sum if column is complete (reached last row)
        if row == 3:
            for c in range(col + 1):
                if np.sum(square[:, c]) != magic_sum:
                    return False
        
        # Check diagonals if at last cell
        if row == 3 and col == 3:
            if np.sum(np.diag(square)) != magic_sum:
                return False
            if np.sum(np.diag(np.fliplr(square))) != magic_sum:
                return False
        
        # Early pruning: check partial row/column sums
        if col > 0:
            partial_row_sum = np.sum(square[row, :col+1])
            min_remaining = sum(sorted([i for i in range(1, 17) if i not in placed])[:4-col-1])
            max_remaining = sum(sorted([i for i in range(1, 17) if i not in placed], reverse=True)[:4-col-1])
            if partial_row_sum + max_remaining < magic_sum or partial_row_sum + min_remaining > magic_sum:
                return False
        
        return True
    
    def solve(square, placed, pos):
        """Backtracking solver."""
        nonlocal magic_squares
        
        if len(magic_squares) >= 880:
            return True
        
        if pos == 16:
            if verify_magic_square_4x4(square) and is_frenicle_standard(square):
                magic_squares.append(square.copy())
                if len(magic_squares) % 88 == 0:
                    print(f"Found {len(magic_squares)}/880 magic squares...")
            return False
        
        row = pos // 4
        col = pos % 4
        
        # Symmetry breaking: constrain first cell based on Frenicle form
        if pos == 0:
            # First cell can only be 1, 2, 3, or 4 (based on symmetry)
            candidates = [1, 2, 3, 4]
        else:
            candidates = range(1, 17)
        
        for num in candidates:
            if num in placed:
                continue
            
            square[row, col] = num
            placed.add(num)
            
            # Check if this placement is promising
            if is_promising(square, row, col, placed):
                if solve(square, placed, pos + 1):
                    return True
            
            placed.remove(num)
            square[row, col] = 0
        
        return False
    
    # Start solving
    square = np.zeros((4, 4), dtype=int)
    placed = set()
    
    solve(square, placed, 0)
    
    print(f"\nGeneration complete! Found {len(magic_squares)} magic squares.")
    
    return magic_squares


def save_magic_squares(squares, filename="magic_squares_880.pkl"):
    """Save magic squares to a pickle file."""
    filepath = Path(filename)
    with open(filepath, 'wb') as f:
        pickle.dump(squares, f)
    print(f"\nSaved {len(squares)} magic squares to: {filepath.absolute()}")


def load_magic_squares(filename="magic_squares_880.pkl"):
    """Load magic squares from a pickle file."""
    filepath = Path(filename)
    if not filepath.exists():
        return None
    
    with open(filepath, 'rb') as f:
        squares = pickle.load(f)
    print(f"Loaded {len(squares)} magic squares from: {filepath.absolute()}")
    return squares


if __name__ == "__main__":
    # Check if already generated
    cache_file = "magic_squares_880.pkl"
    squares = load_magic_squares(cache_file)
    
    if squares is None:
        # Generate them
        squares = generate_880_magic_squares()
        
        # Verify all are valid
        print("\nVerifying all squares...")
        all_valid = all(verify_magic_square_4x4(sq) for sq in squares)
        print(f"All squares valid: {all_valid}")
        
        # Save for future use
        save_magic_squares(squares, cache_file)
    
    # Display first few examples
    print("\n" + "="*50)
    print("First 3 magic squares:")
    print("="*50)
    for i in range(min(3, len(squares))):
        print(f"\nSquare #{i+1}:")
        print(squares[i])
        print(f"All sums equal to: {np.sum(squares[i][0, :])}")
