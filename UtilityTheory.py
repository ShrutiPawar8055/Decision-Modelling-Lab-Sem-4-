import numpy as np
import matplotlib.pyplot as plt

# Utilities
utilities_A = np.array([100, -30, -80])
probs_A = np.array([0.7, 0.2, 0.1])

utilities_B = np.array([100, -80, -500])
probs_B = np.array([0.85, 0.1, 0.05])

# Expected Utility
EU_A = np.sum(probs_A * utilities_A)
EU_B = np.sum(probs_B * utilities_B)

print("Expected Utility of Treatment A:", EU_A)
print("Expected Utility of Treatment B:", EU_B)

# Plot
labels = ['Treatment A', 'Treatment B']
values = [EU_A, EU_B]

plt.bar(labels, values)
plt.title("Medical Decision: Expected Utility")
plt.ylabel("Utility")

plt.show()