"""
Generate figures for the Attentional Blink paper.
All figures are saved to the 'figures' directory.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Create figures directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

# Set style
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 300

def generate_ab_curve():
    """Generate typical attentional blink curve showing T2 accuracy by lag."""
    lags = np.arange(1, 9)
    
    # Simulate typical AB curve with lag-1 sparing
    t2_accuracy = np.array([0.75, 0.45, 0.40, 0.42, 0.55, 0.65, 0.72, 0.75])
    
    # Add some variability
    np.random.seed(42)
    noise = np.random.normal(0, 0.02, len(lags))
    t2_accuracy_noisy = t2_accuracy + noise
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(lags, t2_accuracy_noisy, 'o-', linewidth=2, markersize=8, 
            color='#2E86AB', label='T2|T1 correct')
    ax.axhline(y=0.75, color='gray', linestyle='--', alpha=0.5, label='Baseline')
    
    ax.set_xlabel('Lag (items)', fontsize=12)
    ax.set_ylabel('T2 Accuracy (proportion correct)', fontsize=12)
    ax.set_title('Typical Attentional Blink Curve', fontsize=14, fontweight='bold')
    ax.set_ylim(0.3, 0.85)
    ax.set_xticks(lags)
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/ab_curve.pdf', bbox_inches='tight')
    plt.savefig('figures/ab_curve.png', bbox_inches='tight')
    plt.close()
    
    return t2_accuracy_noisy

def generate_erp_timeline():
    """Generate ERP component timeline showing disrupted vs intact processes."""
    components = ['P1\n(~100ms)', 'N2pc\n(~200ms)', 'N400\n(~400ms)', 'P3b\n(~500ms)']
    status = ['Intact', 'Disrupted', 'Intact', 'Disrupted']
    colors = ['#06A77D', '#D62828', '#06A77D', '#D62828']
    y_positions = [1, 2, 1, 2]
    x_positions = [100, 200, 400, 500]
    
    fig, ax = plt.subplots(figsize=(8, 3))
    
    for i, (comp, stat, col, y, x) in enumerate(zip(components, status, colors, y_positions, x_positions)):
        ax.scatter(x, y, s=800, c=col, alpha=0.7, edgecolors='black', linewidth=2)
        ax.text(x, y, comp, ha='center', va='center', fontsize=9, fontweight='bold')
    
    ax.axhline(y=1, color='#06A77D', linewidth=3, alpha=0.3, label='Intact')
    ax.axhline(y=2, color='#D62828', linewidth=3, alpha=0.3, label='Disrupted')
    
    ax.set_xlabel('Time after stimulus (ms)', fontsize=12)
    ax.set_ylabel('', fontsize=12)
    ax.set_title('ERP Components During Attentional Blink', fontsize=14, fontweight='bold')
    ax.set_ylim(0.5, 2.5)
    ax.set_xlim(50, 550)
    ax.set_yticks([1, 2])
    ax.set_yticklabels(['Intact\nProcessing', 'Disrupted\nProcessing'])
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('figures/erp_timeline.pdf', bbox_inches='tight')
    plt.savefig('figures/erp_timeline.png', bbox_inches='tight')
    plt.close()

def generate_individual_differences():
    """Generate scatter plot showing individual differences in AB magnitude."""
    np.random.seed(42)
    n_subjects = 50
    
    # Simulate working memory capacity and AB magnitude (negative correlation)
    wm_capacity = np.random.normal(3, 0.8, n_subjects)
    ab_magnitude = 0.6 - 0.12 * wm_capacity + np.random.normal(0, 0.08, n_subjects)
    ab_magnitude = np.clip(ab_magnitude, 0.05, 0.55)
    
    # Fit regression line
    slope, intercept, r_value, p_value, std_err = stats.linregress(wm_capacity, ab_magnitude)
    line_x = np.array([wm_capacity.min(), wm_capacity.max()])
    line_y = slope * line_x + intercept
    
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(wm_capacity, ab_magnitude, alpha=0.6, s=60, color='#2E86AB', edgecolors='black', linewidth=0.5)
    ax.plot(line_x, line_y, 'r--', linewidth=2, 
            label=f'r = {r_value:.3f}, p < 0.001')
    
    ax.set_xlabel('Working Memory Capacity (z-score)', fontsize=12)
    ax.set_ylabel('AB Magnitude (Baseline - Lag 3 Accuracy)', fontsize=12)
    ax.set_title('Individual Differences in Attentional Blink', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/individual_differences.pdf', bbox_inches='tight')
    plt.savefig('figures/individual_differences.png', bbox_inches='tight')
    plt.close()
    
    return wm_capacity, ab_magnitude, r_value, p_value

def generate_dual_process():
    """Generate visualization of continuous vs discrete processing."""
    time = np.linspace(0, 600, 1000)
    
    # Continuous amplification (exponential growth)
    continuous = np.where(time < 150, 
                          0.1 * np.exp(time / 80), 
                          0.1 * np.exp(150 / 80))
    
    # Discrete selection (step function at 350ms)
    discrete = np.where(time < 350, 0, 1.0)
    
    # Combined process
    combined = continuous * discrete
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
    
    # Continuous phase
    ax1.plot(time, continuous, color='#06A77D', linewidth=2)
    ax1.fill_between(time, 0, continuous, alpha=0.3, color='#06A77D')
    ax1.set_ylabel('Activation', fontsize=11)
    ax1.set_title('Stage 1: Continuous Amplification (~150ms)', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axvline(x=150, color='gray', linestyle='--', alpha=0.5)
    
    # Discrete phase
    ax2.plot(time, discrete, color='#D62828', linewidth=2)
    ax2.fill_between(time, 0, discrete, alpha=0.3, color='#D62828')
    ax2.set_ylabel('Selection', fontsize=11)
    ax2.set_title('Stage 2: Discrete Selection (~350ms)', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axvline(x=350, color='gray', linestyle='--', alpha=0.5)
    
    # Combined
    ax3.plot(time, combined, color='#2E86AB', linewidth=2)
    ax3.fill_between(time, 0, combined, alpha=0.3, color='#2E86AB')
    ax3.set_xlabel('Time after stimulus (ms)', fontsize=12)
    ax3.set_ylabel('Output', fontsize=11)
    ax3.set_title('Combined: Conscious Report', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.axvline(x=150, color='gray', linestyle='--', alpha=0.3, label='150ms')
    ax3.axvline(x=350, color='gray', linestyle='--', alpha=0.5, label='350ms')
    ax3.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('figures/dual_process.pdf', bbox_inches='tight')
    plt.savefig('figures/dual_process.png', bbox_inches='tight')
    plt.close()

def generate_neural_oscillations():
    """Generate neural oscillation patterns for seen vs missed targets."""
    time = np.linspace(-100, 600, 1000)
    
    # Alpha/beta oscillations
    alpha_seen = 0.3 * np.sin(2 * np.pi * 10 * time / 1000)
    alpha_missed = 0.6 * np.sin(2 * np.pi * 10 * time / 1000)
    
    # Beta increase for seen targets at 200-400ms
    beta_boost = np.where((time > 200) & (time < 400), 
                          0.5 * np.exp(-((time - 300)**2) / (2 * 50**2)), 
                          0)
    
    alpha_seen = alpha_seen + beta_boost
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    
    # Seen target
    ax1.plot(time, alpha_seen, color='#06A77D', linewidth=1.5, label='Seen')
    ax1.fill_between(time, 0, alpha_seen, alpha=0.3, color='#06A77D')
    ax1.axvspan(200, 400, alpha=0.2, color='yellow', label='Beta boost (200-400ms)')
    ax1.set_ylabel('Power (a.u.)', fontsize=11)
    ax1.set_title('Neural Oscillations: Target Seen', fontsize=12, fontweight='bold')
    ax1.axhline(y=0, color='black', linewidth=0.5)
    ax1.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='T1 onset')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # Missed target
    ax2.plot(time, alpha_missed, color='#D62828', linewidth=1.5, label='Missed')
    ax2.fill_between(time, 0, alpha_missed, alpha=0.3, color='#D62828')
    ax2.axvspan(80, 200, alpha=0.2, color='gray', label='Early alpha/beta (80ms+)')
    ax2.set_xlabel('Time after T1 (ms)', fontsize=12)
    ax2.set_ylabel('Power (a.u.)', fontsize=11)
    ax2.set_title('Neural Oscillations: Target Missed', fontsize=12, fontweight='bold')
    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='T1 onset')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/neural_oscillations.pdf', bbox_inches='tight')
    plt.savefig('figures/neural_oscillations.png', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print("Generating figures for Attentional Blink paper...")
    
    print("  - Generating AB curve...")
    ab_data = generate_ab_curve()
    
    print("  - Generating ERP timeline...")
    generate_erp_timeline()
    
    print("  - Generating individual differences plot...")
    wm, ab, r, p = generate_individual_differences()
    
    print("  - Generating dual process model...")
    generate_dual_process()
    
    print("  - Generating neural oscillations...")
    generate_neural_oscillations()
    
    print(f"\nAll figures saved to 'figures' directory!")
    print(f"Generated {len(os.listdir('figures'))} figure files (PDF + PNG)")
