import numpy as np
import matplotlib.pyplot as plt

# Initializing and declaring variables
G = 6.6738e-11 * ((24*60*60*365)**2) # Multiply by time in year in seconds
M = 1.9891 * (10**30)
H = 1 / 52  # 52 weeks in a year
x_0 = 1.4710 * (10**11)
vx_0 = 0
y_0 = 0
vy_0 = 3.0287 * (10**4) * (24*60*60*365)
delta = 1000  # 1km in meters


def fx(x, y):
    return -G * M * x / np.sqrt(x ** 2 + y ** 2) ** 3

def fy(x, y):
    return -G * M * y / np.sqrt(x ** 2 + y ** 2) ** 3

def f(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    return np.array([vx, fx(x, y), vy, fy(x, y)], float)

def Bulirsch_Stoer_step(r, H):

    def modified_midpoint_step(r, n):
        r = np.copy(r)
        h = H / n
        k = r + 0.5 * h * f(r)
        r += h * f(k)
        for i in range(n - 1):
            k += h * f(r)
            r += h * f(k)
        return 0.5 * (r + k + 0.5 * h * f(r))

    target_accuracy = H * delta
    def compute_row_n(R1, n):
        def R_n_m(m):
            return R2[m - 2] + (R2[m - 2] - R1[m - 2]) / ((n / (n - 1)) ** (2 * (m - 1)) - 1)

        # Compute R_n,1
        R2 = [ modified_midpoint_step(r, n) ]
        # Compute the rest of the row
        for m in range(2, n + 1):
            R2.append(R_n_m(m))

        # Convert to array to compute error
        R2 = np.array(R2, float)
        error_vector = (R2[n - 2] - R1[n - 2]) / ((n / (n - 1)) ** (2 * (n - 1)) - 1)
        error = np.sqrt(error_vector[0] ** 2 + error_vector[2] ** 2)
        if error < target_accuracy:
            return R2[n - 1]
        else:
            return compute_row_n(R2, n + 1)

    return compute_row_n(np.array([modified_midpoint_step(r, 1)], float), 2)

plt.figure()

# Calculate Earth's orbit
xpoints = []
ypoints = []
r = np.array([x_0, vx_0, y_0, vy_0], float)
for i in range (2 * 53):
    xpoints.append(r[0])
    ypoints.append(r[2])
    r = Bulirsch_Stoer_step(r, H)

plt.plot(xpoints, ypoints, 'b', label= 'Earth Orbit')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
# plt.show()

# Calculate Pluto's orbit
xpoints = []
ypoints = []
r = np.array([4.4368e12, 0, 0, 6.1218e3 * 8760 * 60 * 60], float)
H = 1  # year
for i in range (260):
    xpoints.append(r[0])
    ypoints.append(r[2])
    r = Bulirsch_Stoer_step(r, H)

plt.plot(xpoints, ypoints, 'g', label = 'Pluto Orbit')
plt.xlim(-7.5e12, 7.5e12)
plt.ylim(-7.5e12, 7.5e12)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.show()
