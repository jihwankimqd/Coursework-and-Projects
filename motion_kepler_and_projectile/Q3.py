import numpy as np
import matplotlib.pyplot as plt

# Initial constants
g = 9.8 #m/s^2
m = 10  # kg
R = 0.08  # m

theta_array = []

v_0 = 1000  # m/s
rho = 1.22  # kg/m^3
C = 0.47  # drag coefficient

t_0 = 4
t_f = 8
N = 1000
h = (t_f - t_0) / N #interval smaller than 0.5s

for i in range (1400,800,-1):
    theta_array.append(np.arctan([1000/i])[0])

c = np.pi * R ** 2 * rho * C / 2
def combined_constant(m):
    return c/m

def f(r, t, m):
    # x = r[0]
    vx = r[1]
    # y = r[2]
    vy = r[3]
    v = np.sqrt(vx ** 2 + vy ** 2)
    return np.array([vx, - combined_constant(m) * vx * v,
                  vy, -g - combined_constant(m) * vy * v], float)


tpoints = np.arange(t_0, t_f, h)
def trajectory(m, theta_0):
    xpoints = []
    ypoints = []
    r = np.array([0, v_0 * np.cos(theta_0), 0, v_0 * np.sin(theta_0)], float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[2])
        k1 = h * f(r, t, m)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, m)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, m)
        k4 = h * f(r + k3, t + h, m)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return np.array(xpoints, float), np.array(ypoints, float)

# trajectory_x_array = []
# trajectory_y_array = []

#plotting the projectile
for theta_0 in range(len(theta_array)):
# for theta_0 in range(10):
    trajectory_x = trajectory(m,theta_array[theta_0])[0]
    trajectory_y = trajectory(m,theta_array[theta_0])[1]
    plt.plot(trajectory_x,trajectory_y)

# plot a horizontal line to show the intersection of the bomber path and the cannonball
plt.plot([0,1750],[1000,1000], 'k-', label ='Bomber Path')

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.show()