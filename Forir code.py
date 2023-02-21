import numpy as np
import matplotlib.pyplot as plt

# Define the grid
L = 1.0 # length of the rod
nx = 51 # number of grid points
dx = L/(nx-1)
x = np.linspace(0, L, nx)

# Define the initial temperature distribution
T0 = np.zeros(nx)
T0[int(nx/2)] = 1.0

# Define the parameters of the problem
alpha = 1.0 # thermal diffusivity
dt = 0.01 # time step
nt = 100 # number of time steps

# Define the finite difference coefficients
a = alpha*dt/dx**2
b = 1 - 2*a

# Define the matrix A for solving the heat equation
A = np.zeros((nx, nx))
A[0, 0] = 1
A[-1, -1] = 1
for i in range(1, nx-1):
    A[i, i-1] = a
    A[i, i] = b
    A[i, i+1] = a

# Solve the heat equation
T = T0.copy()
for n in range(nt):
    T = np.dot(A, T)

# Plot the temperature distribution at the final time step
plt.plot(x, T)
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.show()
