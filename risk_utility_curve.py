# HW - Risk Utility Curve
# Due: April 28 @ 11:59pm
# Author: John Dawood
# Description: Analyze and graph the utility preferences of a company using U(M) = e^(M/50) - 1.
# Evaluate two options:
#   Option A: Guaranteed return of $M
#   Option B: M% chance of $100, (100 - M)% chance of $0

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# --- Task 1: Derive Utility Equations ---
# Utility function: U(M) = e^(M/50) - 1

# Option A:
# A guaranteed return of $M:
# UA(M) = e^(M/50) - 1

# Option B:
# M% chance of $100 and (100 - M)% chance of $0:
# UB(M) = (M / 100) * [e^(100/50) - 1] + (1 - M / 100) * [e^(0/50) - 1]
#       = (M / 100) * (e^2 - 1)

def utility(m):
    return np.exp(m / 50) - 1

def option_a(m):
    return utility(m)

def option_b(m):
    return (m / 100) * (np.exp(100 / 50) - 1)

# --- Task 2: Plot Utility Curves for M = 0 to 100 (step of 10) ---
m_values = np.arange(0, 101, 10)
ua_values = option_a(m_values)
ub_values = option_b(m_values)

plt.figure(figsize=(10, 6))
plt.plot(m_values, ua_values, marker='o', label="Option A: Guaranteed $M")
plt.plot(m_values, ub_values, marker='s', label="Option B: Gamble")

# Adding markers at each step of 10 to the x-axis for clarity
for i, m in enumerate(m_values):
    plt.text(m, ua_values[i], f'{ua_values[i]:.2f}', ha='center', va='bottom', fontsize=9, color='blue')
    plt.text(m, ub_values[i], f'{ub_values[i]:.2f}', ha='center', va='top', fontsize=9, color='red')

plt.title("Utility Comparison: Option A vs Option B")
plt.xlabel("M Value")
plt.ylabel("Utility")
plt.xticks(m_values)  # Ensures the x-axis shows values from 0 to 100 in steps of 10
plt.legend()
plt.grid(True)
plt.savefig("utility_plot.png")  # Save plot for screenshot
plt.show()

# --- Task 3: Analyze Risk Preference ---
# The utility function is concave (exponential growth with diminishing returns),
# which implies the company is risk-averse.
# Although Option B has higher utility values in this setup,
# the shape of the utility curve reflects decreasing marginal utility,
# confirming risk aversion.

# --- Task 4: Evaluate Options at M = $40 ---
m_40 = 40
ua_40 = option_a(m_40)
ub_40 = option_b(m_40)
print(f"\n--- For M = $40 ---")
print(f"Utility Option A (UA): {ua_40:.4f}")
print(f"Utility Option B (UB): {ub_40:.4f}")
if ua_40 > ub_40:
    print("Preferred Option: A (Guaranteed)")
    print("Reason: The guaranteed option provides higher utility, which aligns with the company's risk-averse nature.")
else:
    print("Preferred Option: B (Gamble)")
    print("Reason: The expected utility of the gamble is higher, even though the company is risk-averse. In this case, the gamble offers more value.")

# --- Task 5: Evaluate Options at M = $70 ---
m_70 = 70
ua_70 = option_a(m_70)
ub_70 = option_b(m_70)
print(f"\n--- For M = $70 ---")
print(f"Utility Option A (UA): {ua_70:.4f}")
print(f"Utility Option B (UB): {ub_70:.4f}")
if ua_70 > ub_70:
    print("Preferred Option: A (Guaranteed)")
    print("Reason: The guaranteed amount gives more utility, consistent with risk-averse preferences.")
else:
    print("Preferred Option: B (Gamble)")
    print("Reason: The gamble yields higher utility than the guaranteed $70, so despite risk aversion, it is the better choice in this scenario.")

# --- Task 6: Find Equivalent Gamble % for a Guaranteed $70 ---

# Objective:
# We want to find the exact percentage chance M such that the utility of the gamble (Option B)
# is equal to the utility of receiving a guaranteed $70 (Option A).
# That means: UB(M) = UA(70)

# Step 1: Compute the utility of a guaranteed $70.
target_utility = option_a(70)

# Step 2: Solve for M such that UB(M) = UA(70)
# We define an equation where the difference between UB(M) and UA(70) is zero,
# and use a numerical solver (fsolve) from scipy to find the value of M.

def equation(m):
    return option_b(m) - target_utility

# Step 3: Use an initial guess of M = 50 (a midpoint) for the solver to start from.
m_equivalent = fsolve(equation, 50)[0]

# Step 4: Print and explain the result.
print(f"\n--- Equivalent Gamble % for $70 Guaranteed ---")
print(f"A guaranteed $70 has a utility of: {target_utility:.4f}")
print(f"To match this utility, the company would accept a gamble with a {m_equivalent:.2f}% chance of receiving $100.")
print("This means the company is indifferent between a guaranteed $70 and a ~{:.2f}% chance of $100.".format(m_equivalent))

