def DFS(current, goal):
    """
    Depth first search
    """
    if current == goal:
        return current
    for x in adjacent(current):
        result = DFS(next)
        if result != None:
            return [current] + result

    return None

