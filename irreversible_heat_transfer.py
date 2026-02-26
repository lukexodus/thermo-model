"""
Interactive Thermodynamic Simulation: Irreversible Heat Transfer
=================================================================
Educational model demonstrating heat conduction between hot and cold reservoirs
with entropy generation analysis.

Author: Educational Thermodynamics Simulator
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches

class IrreversibleHeatTransfer:
    """
    Simulates irreversible heat transfer between two thermal reservoirs.
    
    Key Concepts:
    - Heat flows from hot to cold reservoir
    - Temperature gradients drive the process
    - Entropy is generated (irreversibility)
    - System approaches thermal equilibrium
    """
    
    def __init__(self, T_hot_initial=400, T_cold_initial=300, 
                 mass_hot=1.0, mass_cold=1.0, c_p=1000, system_type="Closed"):
        """
        Initialize the thermodynamic system.
        
        Parameters:
        -----------
        T_hot_initial : float
            Initial temperature of hot reservoir (K)
        T_cold_initial : float
            Initial temperature of cold reservoir (K)
        mass_hot : float
            Mass of hot reservoir (kg)
        mass_cold : float
            Mass of cold reservoir (kg)
        c_p : float
            Specific heat capacity (J/kg·K)
        system_type : str
            Type of system: 'Closed', 'Open', or 'Isolated'
        """
        self.T_hot_0 = T_hot_initial
        self.T_cold_0 = T_cold_initial
        self.m_hot = mass_hot
        self.m_cold = mass_cold
        self.c_p = c_p
        
        # Heat transfer coefficient (controls rate)
        self.h = 50  # W/K
        
        # System type: 'Closed', 'Open', 'Isolated'
        self.system_type = system_type

        # Calculate equilibrium temperature
        self.T_eq = self._calculate_equilibrium_temp()
        
        # Time parameters
        self.dt = 0.1  # time step (s)
        self.t_max = 200  # maximum time (s)
        
        # Initialize arrays
        self.reset_simulation()
    
    def _calculate_equilibrium_temp(self):
        """Calculate final equilibrium temperature (energy balance)."""
        numerator = self.m_hot * self.c_p * self.T_hot_0 + self.m_cold * self.c_p * self.T_cold_0
        denominator = self.m_hot * self.c_p + self.m_cold * self.c_p
        return numerator / denominator
    
    def reset_simulation(self):
        """Reset simulation to initial conditions."""
        self.time = np.arange(0, self.t_max, self.dt)
        self.n_steps = len(self.time)
        
        self.T_hot = np.zeros(self.n_steps)
        self.T_cold = np.zeros(self.n_steps)
        self.Q_transferred = np.zeros(self.n_steps)
        self.S_gen_cumulative = np.zeros(self.n_steps)
        self.heat_flux = np.zeros(self.n_steps)
        
        # Initial conditions
        self.T_hot[0] = self.T_hot_0
        self.T_cold[0] = self.T_cold_0
        
        self.current_step = 0
    
    def calculate_heat_transfer_rate(self, T_h, T_c):
        """
        Calculate instantaneous heat transfer rate.
        Q_dot = h * (T_hot - T_cold)
        For 'Isolated' system, Q_dot = 0.
        """
        if self.system_type == "Isolated":
            return 0.0
        return self.h * (T_h - T_c)
    
    def calculate_entropy_generation_rate(self, Q_dot, T_h, T_c):
        """
        Calculate entropy generation rate for irreversible process.
        
        S_gen_dot = Q_dot * (1/T_cold - 1/T_hot)
        
        This is always positive for irreversible heat transfer.
        """
        if Q_dot == 0 or T_h == T_c:
            return 0
        return Q_dot * (1/T_c - 1/T_h)
    
    def step(self):
        """Advance simulation by one time step."""
        if self.current_step >= self.n_steps - 1:
            return False
        i = self.current_step
        Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
        self.heat_flux[i] = Q_dot

        # Closed: energy exchange, no mass exchange
        # Open: allow mass/energy exchange (for now, treat as closed, can extend)
        # Isolated: no energy or mass exchange
        if self.system_type == "Isolated":
            dT_hot = 0.0
            dT_cold = 0.0
        else:
            dT_hot = -Q_dot * self.dt / (self.m_hot * self.c_p)
            dT_cold = Q_dot * self.dt / (self.m_cold * self.c_p)

        self.T_hot[i+1] = self.T_hot[i] + dT_hot
        self.T_cold[i+1] = self.T_cold[i] + dT_cold
        self.Q_transferred[i+1] = self.Q_transferred[i] + Q_dot * self.dt
        S_gen_dot = self.calculate_entropy_generation_rate(Q_dot, self.T_hot[i], self.T_cold[i])
        self.S_gen_cumulative[i+1] = self.S_gen_cumulative[i] + S_gen_dot * self.dt
        self.current_step += 1
        return True
    
    def run_full_simulation(self):
        """Run complete simulation to equilibrium."""
        self.reset_simulation()
        for i in range(self.n_steps - 1):
            self.step()


class InteractiveVisualizer:
    """Interactive visualization with animation and controls."""

    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]
        self.sim = IrreversibleHeatTransfer(system_type="Closed")
        self.setup_figure()
        self.is_playing = False
        self.animation = None

    def on_system_type_change(self, label):
        self.sim.system_type = label
        self.sim.T_eq = self.sim._calculate_equilibrium_temp()
        self.update_simulation()
        self.plot_all()
        
    def setup_figure(self):
        """Create the figure with subplots and controls."""
        self.fig = plt.figure(figsize=(16, 10))
        self.fig.suptitle('Irreversible Heat Transfer: Hot and Cold Reservoirs', 
                         fontsize=16, fontweight='bold')
        
        # Create grid for subplots
        gs = self.fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3, 
                                   left=0.08, right=0.95, top=0.92, bottom=0.25)
        
        # Main plots
        self.ax_visual = self.fig.add_subplot(gs[0, :])  # Reservoir visualization
        self.ax_temp = self.fig.add_subplot(gs[1, :2])    # Temperature vs time
        self.ax_heat = self.fig.add_subplot(gs[1, 2])     # Heat transferred
        self.ax_entropy = self.fig.add_subplot(gs[2, :2]) # Entropy generation
        self.ax_flux = self.fig.add_subplot(gs[2, 2])     # Heat flux
        
        # Add sliders
        self.setup_sliders()
        self.setup_buttons()
        
        # Initial plot
        self.update_simulation()
        self.plot_all()
        
    def setup_sliders(self):
        """Create interactive sliders."""
        # System type radio buttons
        from matplotlib.widgets import RadioButtons
        ax_sys = plt.axes([0.55, 0.15, 0.12, 0.08], facecolor='lightgoldenrodyellow')
        self.radio_system = RadioButtons(ax_sys, self.system_types, active=0)
        self.radio_system.on_clicked(self.on_system_type_change)

        slider_color = 'lightgoldenrodyellow'
        # Slider axes
        ax_T_hot = plt.axes([0.15, 0.15, 0.25, 0.02], facecolor=slider_color)
        ax_T_cold = plt.axes([0.15, 0.11, 0.25, 0.02], facecolor=slider_color)
        ax_h = plt.axes([0.15, 0.07, 0.25, 0.02], facecolor=slider_color)
        ax_mass = plt.axes([0.15, 0.03, 0.25, 0.02], facecolor=slider_color)

        # Create sliders
        self.slider_T_hot = Slider(ax_T_hot, 'T_hot (K)', 310, 500, 
                                   valinit=self.sim.T_hot_0, valstep=10)
        self.slider_T_cold = Slider(ax_T_cold, 'T_cold (K)', 250, 400, 
                                    valinit=self.sim.T_cold_0, valstep=10)
        self.slider_h = Slider(ax_h, 'Heat Transfer Coeff (W/K)', 10, 200, 
                               valinit=self.sim.h, valstep=10)
        self.slider_mass_ratio = Slider(ax_mass, 'Mass Ratio (m_hot/m_cold)', 0.2, 5.0, 
                                       valinit=1.0, valstep=0.1)

        # Connect sliders to update function
        self.slider_T_hot.on_changed(self.on_slider_change)
        self.slider_T_cold.on_changed(self.on_slider_change)
        self.slider_h.on_changed(self.on_slider_change)
        self.slider_mass_ratio.on_changed(self.on_slider_change)
    
    def setup_buttons(self):
        """Create control buttons."""
        # Button axes
        ax_play = plt.axes([0.55, 0.10, 0.08, 0.04])
        ax_reset = plt.axes([0.55, 0.05, 0.08, 0.04])
        
        # Create buttons
        self.btn_play = Button(ax_play, 'Play/Pause')
        self.btn_reset = Button(ax_reset, 'Reset')
        
        # Connect buttons
        self.btn_play.on_clicked(self.toggle_animation)
        self.btn_reset.on_clicked(self.reset_animation)
    
    def on_slider_change(self, val):
        """Handle slider changes."""
        self.sim.T_hot_0 = self.slider_T_hot.val
        self.sim.T_cold_0 = self.slider_T_cold.val
        self.sim.h = self.slider_h.val
        self.sim.m_hot = self.slider_mass_ratio.val
        self.sim.m_cold = 1.0
        
        self.sim.T_eq = self.sim._calculate_equilibrium_temp()
        self.update_simulation()
        self.plot_all()
    
    def update_simulation(self):
        """Run simulation with current parameters."""
        self.sim.run_full_simulation()
    
    def plot_all(self):
        """Update all plots."""
        self.plot_reservoir_visual()
        self.plot_temperature()
        self.plot_heat_transferred()
        self.plot_entropy()
        self.plot_heat_flux()
        self.fig.canvas.draw_idle()
    
    def plot_reservoir_visual(self):
        """Visual representation of the two reservoirs."""
        self.ax_visual.clear()
        self.ax_visual.set_xlim(0, 10)
        self.ax_visual.set_ylim(0, 3)
        self.ax_visual.axis('off')
        self.ax_visual.set_title('Thermal Reservoirs', fontsize=14, fontweight='bold')
        
        # Get current temperatures (at current animation step or final)
        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        T_h = self.sim.T_hot[idx]
        T_c = self.sim.T_cold[idx]
        
        # Color mapping (red = hot, blue = cold)
        def temp_to_color(T):
            # Normalize temperature to color
            T_min, T_max = 250, 500
            normalized = (T - T_min) / (T_max - T_min)
            normalized = np.clip(normalized, 0, 1)
            # Red for hot, blue for cold
            r = normalized
            b = 1 - normalized
            return (r, 0.2, b)
        
        # Hot reservoir (left)
        hot_rect = patches.Rectangle((1, 0.5), 2, 2, 
                                     facecolor=temp_to_color(T_h), 
                                     edgecolor='black', linewidth=2)
        self.ax_visual.add_patch(hot_rect)
        self.ax_visual.text(2, 2.7, f'HOT\n{T_h:.1f} K', 
                           ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Cold reservoir (right)
        cold_rect = patches.Rectangle((7, 0.5), 2, 2, 
                                      facecolor=temp_to_color(T_c), 
                                      edgecolor='black', linewidth=2)
        self.ax_visual.add_patch(cold_rect)
        self.ax_visual.text(8, 2.7, f'COLD\n{T_c:.1f} K', 
                           ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Heat flow arrow
        if T_h > T_c:
            arrow = patches.FancyArrowPatch((3.2, 1.5), (6.8, 1.5),
                                          arrowstyle='->', mutation_scale=30, 
                                          linewidth=3, color='red')
            self.ax_visual.add_patch(arrow)
            self.ax_visual.text(5, 1.8, 'Heat Flow', ha='center', 
                               fontsize=11, color='red', fontweight='bold')
        
        # Display equilibrium temperature
        self.ax_visual.text(5, 0.3, f'Equilibrium: {self.sim.T_eq:.1f} K', 
                   ha='center', fontsize=11, 
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        # Display system type
        self.ax_visual.text(5, 2.95, f'System: {self.sim.system_type}',
                   ha='center', fontsize=12, fontweight='bold', color='black',
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    def plot_temperature(self):
        """Plot temperature evolution."""
        self.ax_temp.clear()
        
        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        
        self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_hot[:idx+1], 
                         'r-', linewidth=2, label='Hot Reservoir')
        self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_cold[:idx+1], 
                         'b-', linewidth=2, label='Cold Reservoir')
        self.ax_temp.axhline(self.sim.T_eq, color='green', linestyle='--', 
                            linewidth=2, label='Equilibrium')
        
        self.ax_temp.set_xlabel('Time (s)', fontsize=11)
        self.ax_temp.set_ylabel('Temperature (K)', fontsize=11)
        self.ax_temp.set_title('Temperature Evolution (Irreversible Process)', fontsize=12)
        self.ax_temp.legend(loc='best')
        self.ax_temp.grid(True, alpha=0.3)
        self.ax_temp.set_xlim(0, self.sim.t_max)
    
    def plot_heat_transferred(self):
        """Plot cumulative heat transferred."""
        self.ax_heat.clear()
        
        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        
        self.ax_heat.plot(self.sim.time[:idx+1], self.sim.Q_transferred[:idx+1]/1000, 
                         'purple', linewidth=2)
        
        self.ax_heat.set_xlabel('Time (s)', fontsize=11)
        self.ax_heat.set_ylabel('Heat (kJ)', fontsize=11)
        self.ax_heat.set_title('Cumulative Heat\nTransferred', fontsize=12)
        self.ax_heat.grid(True, alpha=0.3)
        self.ax_heat.set_xlim(0, self.sim.t_max)
    
    def plot_entropy(self):
        """Plot entropy generation (shows irreversibility)."""
        self.ax_entropy.clear()
        
        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        
        self.ax_entropy.plot(self.sim.time[:idx+1], self.sim.S_gen_cumulative[:idx+1], 
                            'orange', linewidth=2, label='Total Entropy Generated')
        
        self.ax_entropy.set_xlabel('Time (s)', fontsize=11)
        self.ax_entropy.set_ylabel('Entropy Generation (J/K)', fontsize=11)
        self.ax_entropy.set_title('Entropy Generation (Irreversibility Measure)', fontsize=12)
        self.ax_entropy.grid(True, alpha=0.3)
        self.ax_entropy.set_xlim(0, self.sim.t_max)
        
        # Add annotation
        if idx > 0:
            total_S = self.sim.S_gen_cumulative[idx]
            self.ax_entropy.text(0.98, 0.95, f'Total: {total_S:.2f} J/K', 
                                transform=self.ax_entropy.transAxes,
                                ha='right', va='top',
                                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    def plot_heat_flux(self):
        """Plot instantaneous heat transfer rate."""
        self.ax_flux.clear()
        
        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        
        self.ax_flux.plot(self.sim.time[:idx+1], self.sim.heat_flux[:idx+1], 
                         'darkgreen', linewidth=2)
        
        self.ax_flux.set_xlabel('Time (s)', fontsize=11)
        self.ax_flux.set_ylabel('Heat Flux (W)', fontsize=11)
        self.ax_flux.set_title('Instantaneous\nHeat Transfer Rate', fontsize=12)
        self.ax_flux.grid(True, alpha=0.3)
        self.ax_flux.set_xlim(0, self.sim.t_max)
    
    def animate(self, frame):
        """Animation function."""
        if self.is_playing and self.sim.current_step < self.sim.n_steps - 1:
            # Advance several steps per frame for smoother animation
            for _ in range(5):
                if not self.sim.step():
                    self.is_playing = False
                    break
            self.plot_all()
        return []
    
    def toggle_animation(self, event):
        """Start/stop animation."""
        self.is_playing = not self.is_playing
        if self.is_playing:
            if self.animation is None:
                self.animation = FuncAnimation(self.fig, self.animate, 
                                              interval=50, blit=False)
            self.sim.current_step = 0  # Restart from beginning
        
    def reset_animation(self, event):
        """Reset simulation and animation."""
        self.is_playing = False
        self.sim.reset_simulation()
        self.plot_all()
    
    def show(self):
        """Display the interactive visualization."""
        plt.show()


def main():
    """Main function to run the interactive simulation."""
    print("=" * 70)
    print("IRREVERSIBLE HEAT TRANSFER SIMULATION")
    print("=" * 70)
    print("\nEducational Model: Heat Conduction Between Thermal Reservoirs")
    print("\nKey Thermodynamic Concepts:")
    print("  • Heat flows spontaneously from hot to cold")
    print("  • Temperature difference drives irreversible heat transfer")
    print("  • Entropy is generated (Second Law of Thermodynamics)")
    print("  • System approaches thermal equilibrium")
    print("\nControls:")
    print("  • Use sliders to adjust initial temperatures and parameters")
    print("  • Click 'Play/Pause' to animate the process")
    print("  • Click 'Reset' to restart with current parameters")
    print("\nObservations to make:")
    print("  • Temperature evolution toward equilibrium")
    print("  • Entropy always increases (irreversibility)")
    print("  • Heat flux decreases as temperatures approach equilibrium")
    print("=" * 70)
    
    visualizer = InteractiveVisualizer()
    visualizer.show()


if __name__ == "__main__":
    main()
