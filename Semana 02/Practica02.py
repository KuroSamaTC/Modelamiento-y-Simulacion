# Importado de ChatGPT
import matplotlib.pyplot as plt
import numpy as np

# Define the feed composition (x_F) and the distillate composition (xD)
xF = 0.4
xD = 0.9

# Define the vapor-liquid equilibrium data as a function of composition (y = f(x))
def equilibrium_curve(x):
    return 2 * x / (1 + x)

# McCabe-Thiele method calculations
x = np.linspace(0, 1, 100)  # Composition range from 0 to 1
y = equilibrium_curve(x)
RL_slope = (y[-1] - xD) / (xD - xF)
SL_slope = (y[0] - xF) / (xD - xF)

# Calculate the number of stages required
N = (xF - xD) / (RL_slope - SL_slope)

# Plot the McCabe-Thiele diagram
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Equilibrium Line')
plt.plot(x, x, label='45-degree Line', linestyle='--')
plt.plot([xF, xF], [xF, xD], label='Feed Line')
plt.plot([xD, xD], [xF, RL_slope * (xD - xF) + xF], label='Rectifying Line')
plt.plot([xF, xD], [xF, xF], label='Stripping Line')
plt.xlabel('x (Liquid Composition)')
plt.ylabel('y (Vapor Composition)')
plt.title('McCabe-Thiele Diagram')
plt.legend()
plt.grid(True)

# Print the number of equilibrium stages required
print(f'Number of equilibrium stages required (N): {N:.2f}')
plt.show()
