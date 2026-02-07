"""
Display a 3x3 Magic Square

A magic square is a grid where all rows, columns, and diagonals sum to the same value.
This script displays the classic 3x3 magic square using the Lo Shu square configuration.
"""

import numpy as np


def create_magic_square_3x3():
    """
    Create a 3x3 magic square.
    
    Returns:
        numpy.ndarray: A 3x3 magic square where all rows, columns, and diagonals sum to 15.
    """
    # The classic 3x3 magic square (Lo Shu square)
    magic_square = np.array([
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ])
    return magic_square


def verify_magic_square(square):
    """
    Verify that the square is a valid magic square.
    
    Args:
        square: numpy.ndarray representing the magic square
        
    Returns:
        bool: True if valid magic square, False otherwise
    """
    n = len(square)
    magic_sum = n * (n * n + 1) // 2  # Formula for magic constant
    
    # Check all rows
    for row in square:
        if np.sum(row) != magic_sum:
            return False
    
    # Check all columns
    for col_idx in range(n):
        if np.sum(square[:, col_idx]) != magic_sum:
            return False
    
    # Check main diagonal (top-left to bottom-right)
    if np.sum(np.diag(square)) != magic_sum:
        return False
    
    # Check anti-diagonal (top-right to bottom-left)
    if np.sum(np.diag(np.fliplr(square))) != magic_sum:
        return False
    
    return True


def display_magic_square(square):
    """
    Display the magic square in a formatted way.
    
    Args:
        square: numpy.ndarray representing the magic square
    """
    print("\n3x3 Magic Square:")
    print("=" * 20)
    
    for row in square:
        print(" | ".join(f"{num:2d}" for num in row))
        print("-" * 20)
    
    # Calculate and display sums
    magic_sum = np.sum(square[0])
    
    print("\nVerification:")
    print(f"Magic constant (target sum): {magic_sum}")
    print("\nRow sums:")
    for i, row in enumerate(square):
        print(f"  Row {i+1}: {np.sum(row)}")
    
    print("\nColumn sums:")
    for i in range(len(square)):
        print(f"  Column {i+1}: {np.sum(square[:, i])}")
    
    print("\nDiagonal sums:")
    print(f"  Main diagonal: {np.sum(np.diag(square))}")
    print(f"  Anti-diagonal: {np.sum(np.diag(np.fliplr(square)))}")
    
    # Verify
    is_valid = verify_magic_square(square)
    print(f"\nIs this a valid magic square? {is_valid}")
    print("=" * 20)


if __name__ == "__main__":
    # Create and display the magic square
    magic_square = create_magic_square_3x3()
    display_magic_square(magic_square)
