# Classical Planning Example:
# Simple Vacuum Cleaner World
# Two rooms: A and B

# ---------- STATE AND ACTION DEFINITIONS ----------

class WorldState:
    def __init__(self, robot_at, dirty_a, dirty_b):
        self.robot_at = robot_at
        self.dirty_a = dirty_a
        self.dirty_b = dirty_b

    def is_goal(self):
        return not self.dirty_a and not self.dirty_b

    def __repr__(self):
        return f"(Robot={self.robot_at}, DirtyA={self.dirty_a}, DirtyB={self.dirty_b})"


def move(state):
    if state.robot_at == "A":
        return WorldState("B", state.dirty_a, state.dirty_b)
    else:
        return WorldState("A", state.dirty_a, state.dirty_b)


def suck(state):
    if state.robot_at == "A":
        return WorldState("A", False, state.dirty_b)
    else:
        return WorldState("B", state.dirty_a, False)


# ---------- SIMPLE PLANNER (BREADTH FIRST SEARCH) ----------

from collections import deque

def plan(initial_state):
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        state, actions = queue.popleft()

        if state.is_goal():
            return actions

        key = (state.robot_at, state.dirty_a, state.dirty_b)
        if key in visited:
            continue
        visited.add(key)

        # Try actions
        queue.append((move(state), actions + ["MOVE"]))
        queue.append((suck(state), actions + ["SUCK"]))

    return None


# ---------- MAIN PROGRAM ----------

initial = WorldState(robot_at="A", dirty_a=True, dirty_b=True)

print("Initial State:", initial)

solution = plan(initial)

print("\nPlan to clean the room:")
for i, step in enumerate(solution, 1):
    print(i, step)