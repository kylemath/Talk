"""
3D Visualization of a Magic Square

This script creates a 3D bar chart where the height of each bar represents
the value in the magic square at that position.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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


def plot_magic_square_3d(square):
    """
    Create a 3D visualization of the magic square.
    
    Args:
        square: numpy.ndarray representing the magic square
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Get the dimensions
    n = len(square)
    
    # Create meshgrid for x, y positions
    x_pos = np.arange(n)
    y_pos = np.arange(n)
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    
    # Flatten the arrays for bar3d
    x_pos = x_pos.flatten()
    y_pos = y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    
    # Width and depth of bars
    dx = dy = 0.8
    
    # Heights are the magic square values
    dz = square.flatten()
    
    # Create color map based on height
    colors = plt.cm.viridis(dz / dz.max())
    
    # Create the 3D bar chart
    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, alpha=0.8, edgecolor='black')
    
    # Add value labels on top of each bar
    for i in range(n):
        for j in range(n):
            value = square[i, j]
            ax.text(j, i, value, f'{value}', 
                   ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    # Set labels and title
    ax.set_xlabel('X Position', fontsize=12, labelpad=10)
    ax.set_ylabel('Y Position', fontsize=12, labelpad=10)
    ax.set_zlabel('Magic Square Value (Height)', fontsize=12, labelpad=10)
    ax.set_title('3D Visualization of 3x3 Magic Square\n(Height represents the value at each position)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Set tick labels
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels([f'Col {i}' for i in range(n)])
    ax.set_yticklabels([f'Row {i}' for i in range(n)])
    
    # Set z-axis limits
    ax.set_zlim(0, np.max(square) + 1)
    
    # Adjust viewing angle
    ax.view_init(elev=25, azim=45)
    
    # Add grid
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    return fig, ax


def plot_magic_square_surface(square):
    """
    Create a 3D surface plot of the magic square.
    
    Args:
        square: numpy.ndarray representing the magic square
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create meshgrid for x, y positions
    n = len(square)
    x = np.arange(n)
    y = np.arange(n)
    X, Y = np.meshgrid(x, y)
    Z = square
    
    # Create the surface plot
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                          edgecolor='black', linewidth=0.5)
    
    # Add a color bar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    # Add value labels
    for i in range(n):
        for j in range(n):
            value = square[i, j]
            ax.text(j, i, value + 0.3, f'{value}', 
                   ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Set labels and title
    ax.set_xlabel('X Position', fontsize=12, labelpad=10)
    ax.set_ylabel('Y Position', fontsize=12, labelpad=10)
    ax.set_zlabel('Magic Square Value (Height)', fontsize=12, labelpad=10)
    ax.set_title('3D Surface Plot of 3x3 Magic Square', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Set tick labels
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    
    # Adjust viewing angle
    ax.view_init(elev=25, azim=45)
    
    plt.tight_layout()
    
    return fig, ax


if __name__ == "__main__":
    # Create the magic square
    magic_square = create_magic_square_3x3()
    
    # Display the magic square as text
    print("\n3x3 Magic Square:")
    print("=" * 20)
    for row in magic_square:
        print(" | ".join(f"{num:2d}" for num in row))
    print("=" * 20)
    
    # Create both visualizations
    print("\nGenerating 3D visualizations...")
    
    # Bar chart visualization
    fig1, ax1 = plot_magic_square_3d(magic_square)
    
    # Surface plot visualization
    fig2, ax2 = plot_magic_square_surface(magic_square)
    
    print("\nDisplaying 3D plots...")
    print("Close the plot windows to exit.")
    plt.show()
