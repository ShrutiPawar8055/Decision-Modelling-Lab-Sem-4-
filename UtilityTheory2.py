import numpy as np
import matplotlib.pyplot as plt

# Utilities

# Safe investment
utilities_safe = np.array([50, -20])
probs_safe = np.array([0.9, 0.1])

# Risky investment
utilities_risky = np.array([200, -150])
probs_risky = np.array([0.6, 0.4])

# Expected Utility
EU_safe = np.sum(probs_safe * utilities_safe)
EU_risky = np.sum(probs_risky * utilities_risky)

print("Expected Utility of Safe Investment:", EU_safe)
print("Expected Utility of Risky Investment:", EU_risky)

# Plot
labels = ['Safe Investment', 'Risky Investment']
values = [EU_safe, EU_risky]

plt.bar(labels, values)
plt.title("Investment Decision: Expected Utility")
plt.ylabel("Utility")

plt.show()