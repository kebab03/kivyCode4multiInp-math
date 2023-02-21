import numpy as np
import matplotlib.pyplot as plt

# Set parameters
Lx = 1.0  # Width of the wall (m)
Ly = 1.0  # Height of the wall (m)
nx = 21  # Number of grid points in the x direction
ny = 21  # Number of grid points in the y direction
dx = Lx / (nx - 1)  # Grid spacing in the x direction
dy = Ly / (ny - 1)  # Grid spacing in the y direction
alpha = 1.0  # Thermal diffusivity of the wall (m^2/s)
dt = 0.001  # Time step (s)
nt = 1000  # Number of time steps

# Set initial conditions
T0 = np.zeros((nx, ny))
T0[nx // 4:3 * nx // 4, ny // 4:3 * ny // 4] = 20.0  # Set a square region to a higher temperature
T = T0.copy()

# Define the finite difference operator
def laplacian(T):
    Ttop = T[0:-2, 1:-1]
    Tleft = T[1:-1, 0:-2]
    Tbottom = T[2:, 1:-1]
    Tright = T[1:-1, 2:]
    Tcenter = T[1:-1, 1:-1]
    return (Ttop + Tleft + Tbottom + Tright - 4 * Tcenter) / dx**2

# Perform the time evolution
for n in range(nt):
    Tn = T.copy()
    T[1:-1, 1:-1] = Tn[1:-1, 1:-1] + alpha * dt * laplacian(Tn)

    # Apply boundary conditions
    T[0, :] = 0.0  # Left boundary
    T[-1, :] = 0.0  # Right boundary
    T[:, 0] = 0.0  # Bottom boundary
    T[:, -1] = 0.0  # Top boundary

# Plot the temperature distribution
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, T, cmap=plt.cm.hot)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.colorbar()
plt.show()
