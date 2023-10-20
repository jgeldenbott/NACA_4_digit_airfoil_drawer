import numpy as np
from scipy.interpolate import CubicSpline, BPoly, interp1d
import matplotlib.pyplot as plt

x_upper = [0.0, 0.05, 0.4, 1.0]
y_upper = [0.0, -0.03, -0.12, 0.07]
cs_upper = CubicSpline(x_upper, y_upper)

x_lower = [0.0, 0.4, 1.0]
y_lower = [0.0, -0.03, 0.07]
cs_lower = CubicSpline(x_lower, y_lower)

xs = np.arange(0, 1.01, 0.01)

characteristic_line = (cs_upper(xs) + cs_lower(xs)) / 2
x_1 = 0.0
x_2 = 1.0
y_1 = characteristic_line[0]
y_2 = characteristic_line[-1]
chord_slope = y_2 - y_1
chord = np.empty([len(xs)])
for i, val in enumerate(xs):
    chord[i] = val * chord_slope + y_1

# Plotting
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x_upper, y_upper, 'o')
ax.plot(x_lower, y_lower, 'o')
ax.plot(xs, cs_upper(xs), label="Lower Surface")
ax.plot(xs, cs_lower(xs), label="Upper Sruface")
ax.plot(xs, characteristic_line, label="Characteristic Line")
ax.plot(xs, chord, label="Chord", color="black")
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.2, 0.2)
ax.legend(loc='lower right', ncol=2)
plt.show()