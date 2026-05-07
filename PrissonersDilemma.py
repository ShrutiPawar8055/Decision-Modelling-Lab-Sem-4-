import numpy as np
import matplotlib.pyplot as plt

# Payoff matrices
A = np.array([
    [3, 0],
    [5, 1]
])

B = np.array([
    [3, 5],
    [0, 1]
])

strategies = ['C', 'D']

# Find best responses
def best_response_A(j):
    return np.argmax(A[:, j])

def best_response_B(i):
    return np.argmax(B[i, :])

# Find Nash Equilibrium
nash = []

for i in range(2):
    for j in range(2):
        if i == best_response_A(j) and j == best_response_B(i):
            nash.append((i, j))

print(
    "Nash Equilibrium:",
    [(strategies[i], strategies[j]) for i, j in nash]
)

# Plot
fig, ax = plt.subplots()

matrix = np.array([
    [3, 0],
    [5, 1]
])

ax.imshow(matrix)

for i in range(2):
    for j in range(2):
        ax.text(
            j,
            i,
            f"A:{A[i, j]}\nB:{B[i, j]}",
            ha='center',
            va='center'
        )

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])

ax.set_xticklabels(['C', 'D'])
ax.set_yticklabels(['C', 'D'])

plt.title("Prisoner's Dilemma Payoff Matrix")

plt.show()