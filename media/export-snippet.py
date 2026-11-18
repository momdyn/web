# Generate the KanesMethod object
kane = KanesMethod(inertial, q_ind=coords, u_ind=speeds, kd_eqs=kinematic_equations)
fr, frstar = kane.kanes_equations(bodies, loads)


# Generate the lambdified equation
states = coords + speeds
rhs = lambdify([t]+states, kane.rhs().subs(parameters))
def fun(t, x):
    return list(rhs(t, *x)[:, 0])


# Simulate and plot
initial_conditions = list(initial_coords.values()) + list(initial_speeds.values())
sol = solve_ivp(fun, tspan, initial_conditions, first_step=first_step, rtol=tol)
plt.plot(sol.t, sol.y.transpose())
plt.xlabel("Time [sec]")
plt.ylabel("State")
plt.legend([str(state) for state in states])
plt.savefig("states.png")
