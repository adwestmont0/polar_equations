import matplotlib.pyplot as plt
import numpy as np

class PolarCurves:
    def __init__(self):
        self.name = "Roses"
        self.name = "Lemniscates"
        self.name = "Cardioids"
        self.name = "Limacons"
        self.name = "Archimedean Spirals"
        self.name = "Logarithmic Spirals"

def get_user_parameters():
    # Get user input for curve parameters
    print(f"Polar Curves Parameter Input\n")
    
    # Rose Curve: r = a*sin(n*theta)
    print(f"Rose Curve: r = a*sin(n*θ)\n")
    a_rose = float(input("  Enter amplitude (a) [default=2]: ")) # a determines the amplitude of the curve
    n_rose = float(input("  Enter number of petals (n) [default=4]: ")) # n determines the number of petals (if n is odd, n petals; if n is even, 2n petals)
    
    # Lemniscate: r = sqrt(a*cos(2*theta))
    print(f"Lemniscate: r = √(a*cos(2*θ))\n")
    a_lemniscate = float(input("  Enter amplitude (a) [default=2]: "))
    
    # Cardioid: r = a(1 + sin(theta))
    print(f"Cardioid: r = a(1 + sin(θ))\n")
    a_cardioid = float(input("  Enter amplitude (a) [default=2]: "))
    
    # Limacon: r = a + b*cos(theta)
    print(f"Limacon: r = a + b*cos(θ)\n")
    a_limacon = float(input("  Enter amplitude (a) [default=2]: "))
    b_limacon = float(input("  Enter coefficient (b) [default=1]: "))
    
    # Archimedean Spiral: r = a + b*theta
    print(f"Archimedean Spiral: r = a + b*θ\n")
    a_spiral = float(input("  Enter amplitude (a) [default=3]: "))
    b_spiral = float(input("  Enter coefficient (b) [default=2]: "))
    
    # Logarithmic Spiral: r = a*e^(b*theta)
    print(f"Logarithmic Spiral: r = a*e^(b*θ)\n")
    a_log_spiral = float(input("  Enter amplitude (a) [default=4]: "))
    b_log_spiral = float(input("  Enter coefficient (b) [default=3]: "))
    
    return {
        'rose': {'a': a_rose, 'n': n_rose},
        'lemniscate': {'a': a_lemniscate},
        'cardioid': {'a': a_cardioid},
        'limacon': {'a': a_limacon, 'b': b_limacon},
        'spiral': {'a': a_spiral, 'b': b_spiral},
        'log_spiral': {'a': a_log_spiral, 'b': b_log_spiral}
    }

def plot_polar_curves(parameters=None):
    # Plot polar curves with optional user-defined parameters
    theta = np.linspace(0, 2 * np.pi, 1000) # We need to plot from 0 to 2*pi to capture the full curves.
    print(f"theta range: {theta[0]:.2f} to {theta[-1]:.2f}")
    
    # Just use default parameters if none are provided
    if parameters is None:
        pars = {
            'rose': {'a': 2, 'n': 4},
            'lemniscate': {'a': 2},
            'cardioid': {'a': 2},
            'limacon': {'a': 2, 'b': 1},
            'spiral': {'a': 3, 'b': 2},
            'log_spiral': {'a': 4, 'b': 3}
        }
    else:
        pars = parameters
    
    # Calculate curves with parameters
    r1 = pars['rose']['a'] * np.sin(pars['rose']['n'] * theta)  # Roses
    
    # Lemniscate: only plot where cos(2*theta) >= 0
    lemniscate_values = pars['lemniscate']['a'] * np.cos(2 * theta) 
    # cos2theta can be negative, so we will take lemniscate max with 0 to avoid complex numbers
    r2 = np.sqrt(np.maximum(lemniscate_values, 0))
    
    r3 = pars['cardioid']['a'] * (1 + np.sin(theta))  # Cardioid
    r4 = pars['limacon']['a'] + pars['limacon']['b'] * np.cos(theta)  # Limacon
    r5 = pars['spiral']['a'] + pars['spiral']['b'] * theta  # Archimedean Spiral
    r6 = pars['log_spiral']['a'] * np.exp(pars['log_spiral']['b'] * theta)  # Logarithmic Spiral

    plt.figure(figsize=(15, 10))
    
    plt.subplot(231, projection='polar')
    plt.plot(theta, r1, linewidth=2)
    plt.fill(theta, r1, alpha=0.5)
    plt.title(f'Rose Curve: r = {pars["rose"]["a"]}*sin({pars["rose"]["n"]}θ)')
    plt.grid()

    plt.subplot(232, projection='polar')
    plt.plot(theta, r2, linewidth=2)
    plt.fill(theta, r2, alpha=0.5)
    plt.title(f'Lemniscate: r = √({pars["lemniscate"]["a"]}*cos(2θ))')
    plt.grid()

    plt.subplot(233, projection='polar')
    plt.plot(theta, r3, linewidth=2)
    plt.fill(theta, r3, alpha=0.5)
    plt.title(f'Cardioid: r = {pars["cardioid"]["a"]}(1 + sin(θ))')
    plt.grid()

    plt.subplot(234, projection='polar')
    plt.plot(theta, r4, linewidth=2)
    plt.fill(theta, r4, alpha=0.5)
    plt.title(f'Limacon: r = {pars["limacon"]["a"]} + {pars["limacon"]["b"]}*cos(θ)')
    plt.grid()

    plt.subplot(235, projection='polar')
    plt.plot(theta, r5, linewidth=2)
    plt.title(f'Archimedean Spiral: r = {pars["spiral"]["a"]} + {pars["spiral"]["b"]}*θ')
    plt.grid()

    plt.subplot(236, projection='polar')
    plt.plot(theta, r6, linewidth=2)
    plt.title(f'Logarithmic Spiral: r = {pars["log_spiral"]["a"]}*e^({pars["log_spiral"]["b"]}*θ)')
    plt.grid()

    plt.tight_layout()
    plt.savefig('polar_curves.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    print(f'Polar Curves Visualization Tool\n')
    user_choice = input("Use custom parameters? (yes/no) [default=no]: ").lower().strip()
    
    if user_choice in ['yes', 'y']:
        parameters = get_user_parameters()
    elif user_choice in ['no', 'n', '']: # Use defaults
        parameters = None
    
    plot_polar_curves(parameters)