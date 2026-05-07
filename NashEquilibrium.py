import numpy as np
import matplotlib.pyplot as plt
import random

# Payoff matrices
A = np.array([
    [1, -1],
    [-1, 1]
])

B = -A  # Zero-sum game

strategies = ['H', 'T']

# Check pure Nash equilibrium
nash = []

for i in range(2):
    for j in range(2):
        if i == np.argmax(A[:, j]) and j == np.argmax(B[i, :]):
            nash.append((i, j))

print("Pure Nash Equilibria:", nash)

# Simulation
rounds = 1000
A_score = 0

scores = []

for _ in range(rounds):

    A_choice = random.choice([0, 1])
    B_choice = random.choice([0, 1])

    if A_choice == B_choice:
        A_score += 1
    else:
        A_score -= 1

    scores.append(A_score)

# Plot
plt.plot(scores)

plt.title("Matching Pennies Score Over Time")
plt.xlabel("Rounds")
plt.ylabel("Player A Score")

plt.show()