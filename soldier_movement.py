
from collections import deque


def find_best_move(start, target, battlefield):
    """
    Find the next position on the shortest path to a target.

    Primary author: Chukwuma Maduwuba

    Parameters:
        start: Tuple containing the soldier's position.
        target: Tuple containing the destination.
        battlefield: 2D list where 0 is open and 1 is blocked.

    Returns:
        The next position toward the target, or None
        if no valid path exists.
    """
    rows = len(battlefield)
    cols = len(battlefield[0])

    # Check that start and target are valid.
    for row, col in (start, target):
        if not (0 <= row < rows and 0 <= col < cols):
            return None
        if battlefield[row][col] == 1:
            return None

    if start == target:
        return start

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([start])
    visited = {start}
    previous = {}

    while queue:
        current = queue.popleft()

        if current == target:
            break

        for dr, dc in directions:
            new_row = current[0] + dr
            new_col = current[1] + dc
            next_position = (new_row, new_col)

            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            if battlefield[new_row][new_col] == 1:
                continue

            if next_position in visited:
                continue

            visited.add(next_position)
            previous[next_position] = current
            queue.append(next_position)

    if target not in visited:
        return None

    # Trace the shortest path back to the first move.
    position = target

    while previous[position] != start:
        position = previous[position]

    return position


if __name__ == "__main__":
    battlefield = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    soldier = (2, 0)
    destination = (2, 4)

    next_move = find_best_move(soldier, destination, battlefield)

    print(f"Soldier's next move: {next_move}")
