import numpy as np
from collections import deque


def shortest_path(maze):
    """
    Function to calculate the shortest path between coordinate (0, 0) of a matrix and the number 9,
    where it may fall.
    :param maze: 2d array where values of 1 are traversable, values of 0 aren't, and value of 9 is goal.
    :return: Shortest distance from start to finish provied as an integer.
    """

    # Used to build our tracker matrix for locations we've visited.
    num_rows = len(maze)
    num_cols = len(maze[0])

    # We can 1 of 4 directions, assuming their valid.
    row_moves = [1, -1, 0, 0]
    col_moves = [0, 0, 1, -1]

    # Convert maze to an array and use numpy to find coordinates of our goal, which is the 9.
    maze_to_matrix = np.array(maze)
    destination = np.where(maze_to_matrix == 9)
    destination_x, destination_y = destination[1][0], destination[0][0]

    def is_valid_move(matrix, visited, y, x):
        """
        Function to determine if our proposed move is valid (e.g. 1 valid, 0 not valid).
        :param matrix: 2d list provided to parent shortest_path function
        :param visited: Our 2d list tracking where we've been (True) and haven't (False)
        :param y: Proposed y-coordinate for next move
        :param x: Proposed x-coordinate for next move
        :return: Truthy if valid, Falsy if invalid.
        """

        return (y >= 0) and (y < num_rows) and (x >= 0) and (x < num_cols) \
               and (matrix[y][x] == 1 or matrix[y][x] == 9) and not visited[y][x]


    def bfs(matrix, dest_y, dest_x):
        """
        Runs the breadth-first-search algorithm to determine the shortest path.
        :param matrix: 2d list provided to the surrounding shortest_path function.
        :param dest_y: Y-coordinate of our destination cell (i.e. where the 9 is).
        :param dest_x: X-coordination of our destination cell (i.e. where the 9 is).
        :return: The shortest path to our destination.
        """

        # Construct matrix to keep track of visited cells.
        visited = [[False for x in range(num_cols)] for y in range(num_rows)]

        # Mark our origin as visited.
        # Our origin is always the top left node.
        visited[0][0] = True

        # Create an empty queue to keep track of our nodes to visit.
        queue = deque()

        # Append our starting coordinates and its minimum distance from the source to our queue.
        # First number is y coordinate, or outer list index.
        # Second number is x coordinate, or inner list index.
        queue.append((0, 0, 0))

        # Store the length of the longest path from source to destination
        min_dist = float('inf')

        # Pull most recently visited node off queue and determine if neighbouring
        # nodes are accessible. Continue until no valid unvisited nodes remain.
        while queue:
            (y, x, dist) = queue.popleft()

            # If our destination is found then break the loop and return value.
            if y == dest_y and x == dest_x:
                min_dist = dist
                break

            # Check for all possible movement directions from current (x, y)
            # and add valid movements to our queue.
            for i in range(4):
                if is_valid_move(matrix, visited, y + row_moves[i], x + col_moves[i]):
                    visited[y + row_moves[i]][x + col_moves[i]] = True
                    queue.append((y + row_moves[i], x + col_moves[i], dist + 1))

        if min_dist != float('inf'):
            return min_dist
        else:
            return "Desired destination can't be reached from given origin points."

    return bfs(maze, destination_y, destination_x)


maze = [
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 9, 0]
]

print(shortest_path(maze))
