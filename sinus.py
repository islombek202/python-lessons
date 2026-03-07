import numpy as np
import matplotlib.pyplot as plt

# x oraliq [-π/2, π/2]
x = np.linspace(-np.pi/2, np.pi/2, 400)
y = np.sin(2*x)

# tenglama yechimlari
solutions = [np.pi/12, 5*np.pi/12]

plt.figure(figsize=(8,4))
plt.plot(x, y, label='y = sin(2x)')
plt.axhline(1/2, color='red', linestyle='--', label='y = 1/2')
plt.scatter(solutions, [1/2, 1/2], color='green', zorder=5, label='yechimlar')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-np.pi/2, np.pi/2)
plt.ylim(-1, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(2x) = 1/2 yechimlari [-π/2, π/2] oraliqda')
plt.legend()
plt.grid(True)
plt.show()
