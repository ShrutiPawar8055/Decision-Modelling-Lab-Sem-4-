import heapq
import math

# --------------------------------------------------
# Heuristic 1: Misplaced Blocks
# --------------------------------------------------
def heuristic_misplaced_blocks(state, goal):
    misplaced = 0
    for i in range(len(state)):
        current_stack = state[i]
        goal_stack = goal[i]

        for level in range(len(current_stack)):
            if level >= len(goal_stack) or current_stack[level] != goal_stack[level]:
                misplaced += len(current_stack) - level
                break
    return misplaced


# --------------------------------------------------
# Helper: Get block positions
# --------------------------------------------------
def get_block_positions(state):
    positions = {}
    for stack_idx, stack in enumerate(state):
        for height_idx, block in enumerate(stack):
            positions[block] = (stack_idx, height_idx)
    return positions


# --------------------------------------------------
# Heuristic 2: Manhattan Distance
# --------------------------------------------------
def heuristic_manhattan(state, goal):
    current_pos = get_block_positions(state)
    goal_pos = get_block_positions(goal)
    distance = 0
    for block in current_pos:
        x1, y1 = current_pos[block]
        x2, y2 = goal_pos[block]
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# --------------------------------------------------
# Heuristic 3: Euclidean Distance
# --------------------------------------------------
def heuristic_euclidean(state, goal):
    current_pos = get_block_positions(state)
    goal_pos = get_block_positions(goal)
    distance = 0
    for block in current_pos:
        x1, y1 = current_pos[block]
        x2, y2 = goal_pos[block]
        distance += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


# --------------------------------------------------
# Generate Successor States
# --------------------------------------------------
def get_successors(state):
    successors = []
    num_stacks = len(state)

    for i in range(num_stacks):
        if not state[i]:
            continue

        block = state[i][-1]

        for j in range(num_stacks):
            if i != j:
                new_state = [list(stack) for stack in state]
                new_state[i].pop()
                new_state[j].append(block)
                successors.append(tuple(tuple(stack) for stack in new_state))

    return successors


# --------------------------------------------------
# A* Search Algorithm (prints heuristic values)
# --------------------------------------------------
def a_star(initial_state, goal_state):
    open_list = []
    heapq.heappush(open_list, (0, initial_state))

    g_cost = {initial_state: 0}
    parent = {initial_state: None}

    step = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        step += 1

        print(f"\nStep {step}")
        print("Current State:", current)
        print("Misplaced Blocks Heuristic:",
              heuristic_misplaced_blocks(current, goal_state))
        print("Manhattan Distance Heuristic:",
              heuristic_manhattan(current, goal_state))
        print("Euclidean Distance Heuristic:",
              round(heuristic_euclidean(current, goal_state), 2))

        if current == goal_state:
            return reconstruct_path(parent, current)

        for successor in get_successors(current):
            tentative_g = g_cost[current] + 1

            if successor not in g_cost or tentative_g < g_cost[successor]:
                g_cost[successor] = tentative_g
                f_cost = tentative_g + heuristic_manhattan(successor, goal_state)
                heapq.heappush(open_list, (f_cost, successor))
                parent[successor] = current

    return None


# --------------------------------------------------
# Reconstruct Solution Path
# --------------------------------------------------
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]


# --------------------------------------------------
# Example Execution
# --------------------------------------------------
if __name__ == "__main__":

    initial_state = (
        ('A', 'B'),
        ('C',),
        ()
    )

    goal_state = (
        ('A',),
        ('B', 'C'),
        ()
    )

    solution = a_star(initial_state, goal_state)

    print("\nSolution Path:")
    for step in solution:
        print(step)
