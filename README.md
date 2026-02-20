# Polar Equations Visualizer

An interactive Python tool that visualizes polar curves using customizable parameters. Create beautiful mathematical visualizations of rose curves, lemniscates, cardioids, limacons, and spirals.

## Description

This project helps you explore polar coordinate mathematics by plotting six iconic polar curves with user-defined or default parameters:

- **Rose Curve**: `r = a·sin(n·θ)` - A flower-like pattern
- **Lemniscate**: `r = √(a·cos(2θ))` - A figure-8 shaped curve
- **Cardioid**: `r = a(1 + sin(θ))` - A heart-shaped curve
- **Limacon**: `r = a + b·cos(θ)` - A snail-like curve
- **Archimedean Spiral**: `r = a + b·θ` - A spiral that grows uniformly outward
- **Logarithmic Spiral**: `r = a·e^(b·θ)` - An exponential spiral usually found in nature

## Fixes

- **Interactive Parameter Input**: Customize amplitude and coefficients for each curve
- **2×3 Grid Display**: View all six curves simultaneously instead of just four curves
- **High-Quality Output**: Generates publication-ready PNG files
- **Dynamic Titles**: Equations update based on input parameters
- **Fixed Numerical Issues**: Handles edge cases like negative square roots in lemniscates

### Input Screen
```

They all have default values, but decimal and whole custom input values are allowed:

Use custom parameters? (yes/no) [default=no]:

Rose Curve: r = a*sin(n*θ)
  Enter amplitude (a) [default=2]:
  Enter number of petals (n) [default=4]:

Lemniscate: r = √(a*cos(2*θ))
  Enter amplitude (a) [default=2]:

Cardioid: r = a(1 + sin(θ))
  Enter amplitude (a) [default=2]:

Limacon: r = a + b*cos(θ)
  Enter amplitude (a) [default=2]:
  Enter coefficient (b) [default=1]:

Archimedean Spiral: r = a + b*θ
  Enter amplitude (a) [default=3]:
  Enter coefficient (b) [default=2]:

Logarithmic Spiral: r = a*e^(b*θ)
  Enter amplitude (a) [default=4]:
  Enter coefficient (b) [default=3]:
```

## Output

The program generates a `polar_curves.png` file containing a 2×3 subplot grid with all six polar curves. The titles display the actual equations used based on your input parameters.

## Parameters Explained

| Curve | Parameter | Effect |
|-------|-----------|--------|
| Rose | `a` (amplitude) | Controls the size of the curve |
| Rose | `n` (petals) | Odd n = n petals; Even n = 2n petals |
| Lemniscate | `a` | Controls the overall size |
| Cardioid | `a` | Controls the size of the heart shape |
| Limacon | `a` | Controls the inner size |
| Limacon | `b` | Controls the outer curvature |
| Archimedean Spiral | `a` | Starting radius (where spiral begins) |
| Archimedean Spiral | `b` | Growth rate (how fast it expands) |
| Logarithmic Spiral | `a` | Initial amplitude |
| Logarithmic Spiral | `b` | Growth factor (exponential rate) |

## Polar Coordinates
- 𝜃 represents the angle.
- Angles are measured in radians (not degrees).
- A full circle = 360° = 2π radians


## Tips for Further Exploration

- For **Rose curves**, try even vs. odd values of `n` to see different petal patterns
- For **Limacons**, adjust the ratio of `b/a` to create different shapes (loops, cusps, dimples)
- For **Archimedean Spirals**, increase `b` to make the spiral expand faster, or increase `a` for a larger starting radius
- For **Logarithmic Spirals**, larger `b` values create tighter spirals, while smaller values create looser ones
- Experiment with larger amplitudes to see how the curves scale
- Use the same parameters across different curves to compare their behaviors
