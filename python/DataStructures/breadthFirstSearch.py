def breadth_first_walk(graph, start):
    if graph is None or start not in graph:
        return None
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def breadth_first_search(graph, start, key):
    walk = breadth_first_walk(graph, start)
    if walk is not None:
        if key in walk:
            return True
        else:
            return False
    else:
        return "Graph is empty"

