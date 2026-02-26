"""
Quick Example: Understanding Irreversible Heat Transfer
========================================================
This script demonstrates the key calculations without the full GUI.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_irreversible_heat_transfer():
    """
    Simple example calculation showing entropy generation
    in irreversible heat transfer.
    """
    
    print("\n" + "="*70)
    print("EXAMPLE: Irreversible Heat Transfer Calculation")
    print("="*70)
    
    # Initial conditions
    T_hot_initial = 400  # K
    T_cold_initial = 300  # K
    m_hot = 1.0  # kg
    m_cold = 1.0  # kg
    c_p = 1000  # J/(kg·K)
    
    print(f"\nInitial Conditions:")
    print(f"  Hot reservoir:  T = {T_hot_initial} K, mass = {m_hot} kg")
    print(f"  Cold reservoir: T = {T_cold_initial} K, mass = {m_cold} kg")
    print(f"  Specific heat:  c_p = {c_p} J/(kg·K)")
    
    # Calculate equilibrium temperature (energy conservation)
    T_eq = (m_hot * c_p * T_hot_initial + m_cold * c_p * T_cold_initial) / \
           (m_hot * c_p + m_cold * c_p)
    
    print(f"\nEquilibrium Temperature:")
    print(f"  T_equilibrium = {T_eq} K")
    
    # Calculate heat transferred
    Q_transferred = m_hot * c_p * (T_hot_initial - T_eq)
    
    print(f"\nHeat Transferred:")
    print(f"  Q = {Q_transferred} J = {Q_transferred/1000} kJ")
    
    # Calculate entropy change for each reservoir
    # ΔS = m × c_p × ln(T_final / T_initial)
    
    Delta_S_hot = m_hot * c_p * np.log(T_eq / T_hot_initial)
    Delta_S_cold = m_cold * c_p * np.log(T_eq / T_cold_initial)
    Delta_S_total = Delta_S_hot + Delta_S_cold
    
    print(f"\nEntropy Changes:")
    print(f"  ΔS_hot  = {Delta_S_hot:.2f} J/K (negative - entropy decreases)")
    print(f"  ΔS_cold = {Delta_S_cold:.2f} J/K (positive - entropy increases)")
    print(f"  ΔS_total (generated) = {Delta_S_total:.2f} J/K")
    
    print(f"\n{'Key Observation:':-^70}")
    print(f"  Total entropy INCREASED by {Delta_S_total:.2f} J/K")
    print(f"  This confirms the process is IRREVERSIBLE!")
    print(f"  (Second Law: ΔS_universe ≥ 0, here ΔS_universe > 0)")
    
    # Calculate lost work (exergy destruction)
    T_ambient = 298  # K (25°C)
    lost_work = T_ambient * Delta_S_total
    
    print(f"\nLost Work Potential (Exergy Destruction):")
    print(f"  W_lost = T_ambient × ΔS_gen = {T_ambient} K × {Delta_S_total:.2f} J/K")
    print(f"  W_lost = {lost_work:.2f} J = {lost_work/1000:.3f} kJ")
    print(f"\n  This is the maximum work that COULD have been extracted")
    print(f"  if we had used a reversible process (heat engine).")
    
    # Efficiency comparison
    print(f"\n{'Comparison with Reversible Process:':-^70}")
    # Carnot efficiency between initial temperatures
    eta_carnot = 1 - T_cold_initial / T_hot_initial
    W_max_reversible = eta_carnot * Q_transferred
    
    print(f"  If we used a Carnot engine between these reservoirs:")
    print(f"  Maximum efficiency: η = {eta_carnot*100:.2f}%")
    print(f"  Maximum work output: W_max = {W_max_reversible/1000:.3f} kJ")
    print(f"\n  But with direct heat transfer (irreversible):")
    print(f"  Work output: 0 kJ")
    print(f"  Lost opportunity: {W_max_reversible/1000:.3f} kJ")
    
    print("\n" + "="*70 + "\n")
    
    return T_eq, Delta_S_total, Q_transferred


def plot_entropy_vs_temperature_difference():
    """
    Show how entropy generation depends on initial temperature difference.
    """
    
    T_cold = 300  # K (fixed)
    T_hot_range = np.linspace(310, 500, 50)  # K
    
    m = 1.0  # kg
    c_p = 1000  # J/(kg·K)
    
    entropy_generated = []
    
    for T_hot in T_hot_range:
        # Equilibrium temperature
        T_eq = (T_hot + T_cold) / 2  # Equal masses
        
        # Entropy generation
        Delta_S_hot = m * c_p * np.log(T_eq / T_hot)
        Delta_S_cold = m * c_p * np.log(T_eq / T_cold)
        Delta_S_total = Delta_S_hot + Delta_S_cold
        
        entropy_generated.append(Delta_S_total)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(T_hot_range - T_cold, entropy_generated, 'b-', linewidth=2)
    plt.xlabel('Initial Temperature Difference (K)', fontsize=12)
    plt.ylabel('Total Entropy Generated (J/K)', fontsize=12)
    plt.title('Entropy Generation vs Temperature Difference\n(Irreversible Heat Transfer)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add annotation
    plt.text(0.6, 0.95, 
             'Larger temperature difference\n→ More irreversibility\n→ More entropy generated',
             transform=plt.gca().transAxes,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
             fontsize=10, va='top')
    
    plt.tight_layout()
    plt.savefig('/home/claude/entropy_vs_temperature.png', dpi=150, bbox_inches='tight')
    print("Plot saved: entropy_vs_temperature.png")
    plt.close()


def main():
    """Run example calculations."""
    
    # Basic calculation
    T_eq, Delta_S, Q = calculate_irreversible_heat_transfer()
    
    # Generate plot
    plot_entropy_vs_temperature_difference()
    
    print("\nNext Steps:")
    print("  1. Run the full interactive simulation:")
    print("     python irreversible_heat_transfer.py")
    print("\n  2. Experiment with different parameters using the sliders")
    print("\n  3. Observe how entropy ALWAYS increases (Second Law!)")


if __name__ == "__main__":
    main()
