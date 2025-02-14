import time


def state_to_tuple(state):
    """Convert a string state to a tuple representation."""
    return ((state[0], state[1], state[2]),
            (state[3], state[4], state[5]),
            (state[6], state[7], state[8]))


def tuple_to_state(matrix):
    """Convert a tuple representation back to a string state."""
    return ''.join(''.join(row) for row in matrix)


def get_moves(matrix):
    """Generate possible moves from the given state."""
    lowest_highest = (0, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    moves = []
    # Convert tuple to list for mutability
    grid = [list(row) for row in matrix]

    free = (0, 0)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '0':
                free = (i, j)
                break

    for direction in directions:
        node = free[0] + direction[0], free[1] + direction[1]
        if lowest_highest[0] <= node[0] < lowest_highest[1] \
                and lowest_highest[0] <= node[1] < lowest_highest[1]:
            new_grid = [row[:] for row in grid]  # copy grid
            new_grid[free[0]][free[1]], new_grid[node[0]][node[1]] = new_grid[node[0]][node[1]], \
                                                                     new_grid[free[0]][free[1]]  # swap

            moves.append(state_to_tuple(tuple_to_state(new_grid)))

    return moves


def dfs(start_state, goal_state):
    """Perform Depth-First Search (DFS) to find a solution path."""
    stack = [(start_state, [])]  # Stack for DFS: (current_state, path_to_state)
    visited = set()

    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue

        visited.add(current_state)

        # If goal state is reached, return the path
        if current_state == goal_state:
            return path + [current_state]

        # Generate possible moves and add them to stack
        for move in get_moves(current_state):
            if move not in visited:
                stack.append((move, path + [current_state]))

    return None  # Return None if no solution found


def main():
    """Main function to take input and execute the DFS algorithm."""
    start_state = "102345678"  # input("Enter start State: ")
    goal_state = "012345678"  # input("Enter goal State: ")

    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)

    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")

    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()

    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path) - 1)
        print("No of Nodes Visited:", len(solution_path))

        for state in solution_path:
            for row in state:
                print(' '.join(row))
            print("-----")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
