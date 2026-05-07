import heapq

# 0 = free cell, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (2, 3)

# Movement directions: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# ---------------- Heuristic Function ----------------
def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ---------------- A* Algorithm ----------------
def astar():
    open_list = []
    heapq.heappush(open_list, (0, start, [start], 0))
    visited = set()

    while open_list:
        f, current, path, g = heapq.heappop(open_list)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and neighbor not in visited:
                    g_new = g + 1
                    h = heuristic(neighbor, goal)
                    f_new = g_new + h
                    heapq.heappush(open_list,
                                   (f_new, neighbor, path + [neighbor], g_new))
    return None


# ---------------- Greedy Best-First Search ----------------
def greedy():
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start, [start]))
    visited = set()

    while open_list:
        h, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and neighbor not in visited:
                    heapq.heappush(open_list,
                                   (heuristic(neighbor, goal),
                                    neighbor,
                                    path + [neighbor]))
    return None


# ---------------- Main Execution ----------------
print("Grid:")
for row in grid:
    print(row)
print("A* Path:")
print(astar())

print("\nGreedy Best-First Search Path:")
print(greedy())
