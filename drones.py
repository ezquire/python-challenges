from collections import defaultdict

def get_areas(edges, target):
    neighbors = get_neighbors(edges)
    # print neighbors

    for node1, node2, _ in sorted(edges, key=lambda e: e[-1], reverse=True):
        neighbors[node1].remove(node2)
        neighbors[node2].remove(node1)

        areas = get_connected_components(neighbors)
        # print areas
        if len(areas) == target:
            return areas
    return areas

def get_neighbors(edges):
    neighbors = defaultdict(set)
    for node1, node2, _ in edges:
        neighbors[node1].add(node2)
        neighbors[node2].add(node1)
    return neighbors

def get_connected_components(neighbors):
    visited = set()
    connected_components = []
    for node in neighbors:
        if node not in visited:
            connected_component = dfs(node, neighbors)
            connected_components.append(connected_component)
            visited.update(connected_component)
    return connected_components

def dfs(root, neighbors):
    stack = [root]
    visited = set(stack)
    while stack:
        node = stack.pop()
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                stack.append(neighbor)
            visited.add(node)
    return list(visited)

test_input = [
      ['a', 'b', 6],
      ['a', 'c', 3],
      ['a', 'd', 8],
      ['b', 'c', 4],
      ['b', 'f', 8],
      ['c', 'd', 7],
      ['c', 'g', 8],
      ['d', 'e', 1],
      ['d', 'g', 11],
      ['e', 'g', 10],
      ['f', 'g', 1],
      ['f', 'h', 6],
      ['g', 'h', 7],
    ]

print(get_areas(test_input, 3))
