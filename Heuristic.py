#Heauristic approach to 8-puzzle problem

import heapq

def solve_8puzzle(initial_state):
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    priority_queue = [(heuristic(initial_state, goal_state), 0, initial_state, [])]  
    visited = set()

    while priority_queue:
        f_cost, g_cost, current_state, current_path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return current_path + [current_state]

        if tuple(map(tuple, current_state)) in visited:
            continue
        visited.add(tuple(map(tuple, current_state)))

        for next_state, action in get_possible_moves(current_state):
            new_g_cost = g_cost + 1
            new_f_cost = new_g_cost + heuristic(next_state, goal_state)
            heapq.heappush(priority_queue, (new_f_cost, new_g_cost, next_state, current_path + [(current_state, action)]))

    return None


def heuristic(state, goal_state):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                misplaced_tiles += 1
    return misplaced_tiles


def find_position(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return i, j


def get_possible_moves(state):
    row, col = find_position(state, 0)
    possible_moves = []

    if row > 0:
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
        possible_moves.append((new_state, 'Up'))
    if row < 2:
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
        possible_moves.append((new_state, 'Down'))
    if col > 0:
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
        possible_moves.append((new_state, 'Left'))
    if col < 2:
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
        possible_moves.append((new_state, 'Right'))

    return possible_moves


initial_state = [[2, 8, 3], [1, 6, 4], [0, 7, 5]]
solution = solve_8puzzle(initial_state)

if solution:
    print("Solution found:")
    for state, action in solution[:-1]:
        print("--------------------")
        for row in state:
            print(row)
        print("Move:", action)
    print("--------------------")
    for row in solution[-1]:
        print(row)
else:
    print("No solution found.")
