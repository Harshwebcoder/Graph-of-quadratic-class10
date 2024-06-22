import numpy as np
import matplotlib.pyplot as plt
# Coefficients of the quadratic equation
a = -3
b = 7
c = -6

# Calculate the discriminant
d = b**2 - 4*a*c

# Function to compute roots of the quadratic equation
def compute_roots(a, b, c):
    if a == 0:
        return None, None  # Not a quadratic equation
    else:
        sqrt_d = np.sqrt(d)
        if d > 0:
            root1 = (-b + sqrt_d) / (2 * a)
            root2 = (-b - sqrt_d) / (2 * a)
            return root1, root2
        elif d == 0:
            root = -b / (2 * a)
            return root, root
        else:
            return None, None  # No real roots

# Compute roots
root1, root2 = compute_roots(a, b, c)

# Calculate x-coordinate of the vertex
vertex_x = -b / (2 * a)

# Calculate y-coordinate of the vertex
vertex_y = -d / (4 * a)

vertex = (vertex_x, vertex_y)

# Plotting the quadratic function and roots
x = np.linspace(-3, 4, 600)  # Generate x values for plotting
y = a*x**2 + b*x + c  # Compute y values for the quadratic equation

plt.figure(figsize=(10, 10))

# Plot the quadratic function
plt.plot(x, y, label=f"${a}x^2 + {b}x + {c}$")

# Plot the roots
if root1 is not None:
    plt.plot(root1, 0, 'ro', label=f"Root 1: {root1:.2f}")
if root2 is not None:
    plt.plot(root2, 0, 'go', label=f"Root 2: {root2:.2f}")
    
# Plot the vertex
plt.plot(vertex_x, vertex_y, 'yo', label=f"Vertex: ({vertex_x:.2f}, {vertex_y:.2f})")

# Plot the y-intercept
plt.plot(0, c, 'bo', label=f"Y-intercept: (0, {c})")

plt.title('Quadratic Equation and Roots')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-8, 9)
plt.legend(shadow=True, edgecolor='black', title='Information', fancybox=True)
plt.show()
