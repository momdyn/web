# PLACEHOLDER: sample script, not real MOMDYN output. Replace with a real export.
import numpy as np
from scipy.integrate import solve_ivp

m1, m2, l1, l2, g = 1.0, 1.0, 1.0, 1.0, 9.81

def rhs(t, y):
    th1, th2, w1, w2 = y
    d = th1 - th2
    M = np.array([[(m1 + m2) * l1**2, m2 * l1 * l2 * np.cos(d)],
                  [m2 * l1 * l2 * np.cos(d), m2 * l2**2]])
    F = np.array([-m2 * l1 * l2 * w2**2 * np.sin(d) - (m1 + m2) * g * l1 * np.sin(th1),
                  m2 * l1 * l2 * w1**2 * np.sin(d) - m2 * g * l2 * np.sin(th2)])
    return [w1, w2, *np.linalg.solve(M, F)]

sol = solve_ivp(rhs, (0, 10), [1.0, 0.5, 0, 0], max_step=0.01)
