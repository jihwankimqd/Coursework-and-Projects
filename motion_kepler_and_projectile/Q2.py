import numpy as np
import matplotlib.pyplot as plt

# Initial variables and constants
e = 1.602 * (10 ** -19)
V0 = 50 * e  # J
a = 10 ** -11  # Angstrom
x_0 = -10 ** -10
x_f = 10 ** -10
psi_0 = 0.0
hbar = 1.05457 * (10 ** -34)  # J*s
m = 9.10938 * (10 ** -31) # electron mass in kg
N = 1000  # number of steps to use in Runge-Kutta
h = (x_f - x_0) / N

# def V(x):
#     return V0 * x ** 2 / a ** 2
def V(x):
    return V0 * x ** 4 / a ** 4

def psi(E):
    def f(r, x):
        psi = r[0]
        phi = r[1]
        return np.array([phi, (2 * m / hbar ** 2) * (V(x) - E) * psi], float)

    r = np.array([psi_0, 1.0] ,float)
    wavefunction = []
    for x in np.arange(x_0, x_f, h):
        wavefunction.append(r[0])
        k1 = h * f(r, x)
        k2 = h * f(r + 0.5 * k1, x + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, x + 0.5 * h)
        k4 = h * f(r + k3, x + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return np.array(wavefunction, float)


def secant_root(E1, E2):
    target_accuracy = e / 1000 
    wavefunction = psi(E1)
    psi2 = wavefunction[N - 1]
    while abs(E1 - E2) > target_accuracy:
        wavefunction = psi(E2)
        psi1, psi2 = psi2, wavefunction[N - 1]
        E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)

    #Simpson's Rule
    mod_squared = wavefunction * wavefunction
    integral = h / 3 *(mod_squared[0] + mod_squared[N//2 - 1] + \
            4 * sum(mod_squared[1 : N//2 : 2]) + 2 * sum(mod_squared[0 : N//2 + 1 : 2]) )

    return (E2 / e), (wavefunction / np.sqrt(2*integral))


# Harmonic Oscillator
# print('First three lowest energies of a harmonic oscillator')
# print('E_0 = ', secant_root(0, 0.5*e)[0], 'eV')
# print('E_1 = ', secant_root(200*e, 400*e)[0], 'eV')
# print('E_2 = ', secant_root(500*e, 700*e)[0], 'eV')


# Anharmonic Oscillator
print('First three lowest energies of an anharmonic oscillator')
print('E_0 = ', secant_root(0, 0.5*e)[0], 'eV')
print('E_1 = ', secant_root(400*e, 600*e)[0], 'eV')
print('E_2 = ', secant_root(900*e, 1100*e)[0], 'eV')

