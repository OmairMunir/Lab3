from collections import deque


def find_shortest_path(grid, start=(0, 0), end=(3, 3)):
    lowest_highest = (0, len(grid) - 1)

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    q.append((start, [start])) # start node + path
    visited = set()
    visited.add(start)

    while len(q) > 0:
        node, path = q.pop()
        if node == end:
            return path

        for direction in directions:
            new_node = (node[0] + direction[0], node[1] + direction[1])
            # print(
            #     "node:", new_node, "is valid:", range[0] <= new_node[0] <= range[1],
            #     range[0] <= new_node[1] <= range[1],
            #     new_node in visited)

            # is valid:
            if lowest_highest[0] <= new_node[0] <= lowest_highest[1] \
                    and lowest_highest[0] <= new_node[1] <= lowest_highest[1] \
                    and not (new_node in visited):
                q.append((new_node, path + [new_node]))
                visited.add(new_node)

    return None


matrix = [[0] * 5 for _ in range(5)]
print("Shortest path:", find_shortest_path(matrix, (1, 1), (4, 4)))
