# Decision Modelling Lab Experiments
 
A quick-reference guide to all 10 experiments — what each one is about, in plain English.

Owner : Shruti Pawar
Semester 4
---
 
## Experiment 1 — Classical Search Algorithms (Robot Path Planning)
 
**Classical Planning** is about finding a sequence of steps to get from a start point to a goal. Think of it as solving a maze — the AI tries different paths until it finds one that works.
 
**BFS (Breadth-First Search)**
Explores all paths level by level — checks everything 1 step away, then 2 steps, and so on. Always finds the shortest path, but uses a lot of memory.
> Like spreading water on a flat surface — it fills nearby spots before moving further out.
 
**DFS (Depth-First Search)**
Dives deep into one path before backtracking and trying another. Uses less memory than BFS but doesn't guarantee the shortest path.
> Like exploring a cave — go down one tunnel until it's a dead end, then try the next.
 
**A\* (A-Star) Search**
The smartest of the three. Combines the actual distance travelled with an estimated distance to the goal, always exploring the most promising path first.
 
`f(n) = g(n) + h(n)`
- `g(n)` — cost from start to current node
- `h(n)` — estimated cost from current node to goal (heuristic)
- `f(n)` — total estimated cost; A\* always picks the lowest
> **Real life:** Google Maps uses A\* to find your route — it skips roads clearly going the wrong direction using the heuristic.
 
---
 
## Experiment 2 — Heuristic Generation & Analysis
 
A **heuristic** is an educated guess about how far you are from the goal. It helps A\* skip bad paths without fully exploring them.
 
**Manhattan Distance**
Distance when you can only move up/down/left/right (no diagonals) — like navigating a city grid.
 
`h(n) = |x₁ - x₂| + |y₁ - y₂|`
 
**Euclidean Distance**
Straight-line ("as the crow flies") distance between two points, ignoring walls or obstacles.
 
`h(n) = √((x₁-x₂)² + (y₁-y₂)²)`
 
**Custom Heuristic**
When neither Manhattan nor Euclidean fits, you design one for the specific problem. For the 8-puzzle, a common custom heuristic is simply counting how many tiles are out of place.
 
- A good heuristic never *overestimates* the real cost (called **admissible**) — this guarantees A\* finds the optimal path.
- The closer the heuristic is to reality, the fewer nodes A\* explores.
> **Real life:** Video game AI uses custom heuristics — a unit crossing a river gets a higher movement cost than one on flat terrain.
 
---
 
## Experiment 3 — Bayes' Theorem for Probabilistic Inference
 
**Probabilistic reasoning** lets AI deal with uncertainty by working with likelihoods instead of hard yes/no answers.
 
**Bayes' Theorem** tells you how to update your belief when you get new evidence.
 
`P(A|B) = [ P(B|A) × P(A) ] / P(B)`
 
- `P(A)` — your belief *before* seeing evidence (prior)
- `P(B|A)` — how likely is the evidence if A is true (likelihood)
- `P(A|B)` — your updated belief *after* seeing evidence (posterior)
**Example:** A disease affects 1% of people. A test is 95% accurate. You test positive. Intuitively you panic — but Bayes shows your actual chance of having the disease is only ~16%, because false positives are common when the disease is rare.
 
> **Real life:** Gmail's spam filter and medical diagnosis systems run on Bayes' Theorem under the hood.
 
---
 
## Experiment 4 — Naïve Bayes Classifier
 
A **classifier** takes a set of features and assigns a category label (e.g., "spam" or "not spam").
 
**Naïve Bayes** applies Bayes' Theorem to classify data, with one simplifying assumption: all features are treated as *independent* of each other. This assumption is "naïve" but works surprisingly well in practice.
 
`P(class | features) ∝ P(class) × ∏ P(featureᵢ | class)`
 
**How it works:**
- **Data Preparation** — collect labelled examples, clean and format the data
- **Training** — model learns the probability of each feature appearing in each class
- **Testing & Evaluation** — feed new data, model picks the class with the highest probability, accuracy is measured against known labels
> **Real life:** Your email spam folder was almost certainly built with a Naïve Bayes classifier.
 
---
 
## Experiment 5 — Bayesian Networks
 
A **Bayesian Network** is a diagram where nodes are variables (e.g., Rain, Sprinkler, Wet Grass) and arrows show cause-and-effect relationships. Each node stores a probability table based on its parent nodes.
 
Instead of "if it rains, the grass is wet," it says "if it rains, there is a 95% chance the grass is wet."
 
**Two parts:**
- **Structure** — which variables influence which others (the graph)
- **Conditional Probability Tables (CPTs)** — the actual probability numbers for every combination of parent states
**Inference** — you provide known facts (evidence) and ask the network to compute the probability of unknown variables. Example: grass is wet → what is the probability it rained vs. the sprinkler was on?
 
> **Real life:** Windows troubleshooter uses a Bayesian Network — you answer a few questions and it computes the most probable cause of your issue.
 
---
 
## Experiment 6 — Hidden Markov Models & Kalman Filters
 
Both tools are for tracking something that changes over time when you can't directly observe the true state — only noisy sensor readings.
 
**Hidden Markov Model (HMM)**
The system moves through hidden states (e.g., actual weather: Sunny/Rainy) and produces observable outputs (e.g., does someone carry an umbrella: Dry/Wet). You use the observations to infer the hidden states.
 
Key components:
- **Transition probabilities** — how likely is the state to change? (e.g., Sunny→Rainy = 30%)
- **Emission probabilities** — given a state, how likely is each observation?
- **Forward Algorithm** — computes the probability of an observed sequence given the model
**Kalman Filter**
The continuous-state equivalent. Estimates a smoothly varying quantity (e.g., position of a moving object) from noisy sensor readings. Balances trust between the prediction and the new measurement.
 
`x̂ₖ = x̂ₖ₋₁ + K(zₖ - x̂ₖ₋₁)`
- `K` = Kalman Gain — how much to trust the new sensor reading vs. the old prediction
> **Real life:** HMMs power speech recognition. Kalman filters smooth your GPS — the Apollo spacecraft navigation system was its first use.
 
---
 
## Experiment 7 — Bayesian Networks for Real-World Reasoning
 
This applies Bayesian Networks to realistic, multi-variable problems.
 
**Student Exam Performance** — variables: hours studied, course difficulty, attendance, intelligence → output: probability of passing. You can query: "Student studied 2 hours, hard course — probability of passing?"
 
**Medical Diagnosis System** — symptoms (fever, cough, fatigue) are connected to diseases (flu, COVID, pneumonia). The network gives a ranked list of probable diagnoses based on observed symptoms.
 
**Car Starting Problem** — variables: battery, fuel, ignition, alternator, starter motor. Observation: car won't start. The network points to the most probable faulty component first.
 
> **Real life:** Windows Network Troubleshooter, clinical decision support systems, and smart car diagnostic tools all use this approach.
 
---
 
## Experiment 8 — Particle Filters for Object Tracking
 
A **particle filter** tracks an object by maintaining hundreds of hypotheses (particles) about where the object might be. Particles that match sensor readings survive and multiply; ones that don't match are discarded. The cloud of surviving particles converges on the true position.
 
**Steps:**
1. **Initialise** — scatter particles randomly across all possible positions
2. **Predict** — move each particle according to the motion model (with noise)
3. **Update** — weight each particle by how well it matches the sensor reading
4. **Resample** — keep particles proportional to their weight; discard poor ones
5. Repeat — particles converge around the true state
**Example tasks:**
- Robot on a 1D grid tracking its position
- Person tracking with noisy GPS
- Drone altitude estimation with a noisy barometric sensor
> **Real life:** Self-driving cars use particle filters for precise localisation. GPS gives ~5m accuracy; particle filters fused with LIDAR give centimetre-level precision.
 
---
 
## Experiment 9 — Utility Theory & Decision-Making
 
**Utility theory** is a framework for making rational decisions when outcomes are uncertain. A *utility* is a number representing how desirable an outcome is. The rational choice is the action with the highest **Expected Utility (EU)**.
 
`EU(action) = Σ P(outcome | action) × U(outcome)`
 
**Medical Treatment Example:**
- Treatment A: 70% full recovery (U=100), 30% no effect (U=20) → EU = **76**
- Treatment B: 50% full recovery (U=100), 50% partial improvement (U=60) → EU = **80**
- → Treatment B is the rational choice.
**Investment Decision** — same logic: weigh each possible financial outcome by its probability and utility, pick the highest EU option.
 
> **Real life:** Insurance is pure utility theory — you trade a small certain loss (premium) to avoid a rare catastrophic loss. Both sides are maximising their expected utility.
 
---
 
## Experiment 10 — Game Theory & Multi-Agent Strategy
 
**Game theory** studies strategic interaction where your outcome depends on others' choices too — not just your own.
 
**Nash Equilibrium** — a stable state where no player can improve their outcome by changing their strategy alone, assuming everyone else holds theirs.
 
**Prisoner's Dilemma**
Two suspects independently choose: stay silent (cooperate) or betray (defect).
- Both silent → light sentence for both
- One betrays → betrayer goes free, other gets heavy sentence
- Both betray → medium sentence for both
Rational self-interest pushes both to betray — yet mutual cooperation gives the better outcome for both. The Nash Equilibrium (both defect) is worse than the cooperative outcome — this is the core tension.
 
**Matching Pennies**
Players simultaneously show heads or tails. Player 1 wins if they match; Player 2 wins if they don't. No pure strategy works — the optimal play is to randomise 50/50 (**Mixed Strategy Equilibrium**).
 
> **Real life:** Google's ad auction is game theory in action — it's designed so every advertiser's best strategy is to bid their true value (a Nash Equilibrium), making the auction fair and self-enforcing.
 
---
 