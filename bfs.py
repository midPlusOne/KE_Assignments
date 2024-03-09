from queue import PriorityQueue

# Define the graph as an adjacency list
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 5},
    'E': {'H': 3},
    'F': {},
    'G': {},
    'H': {}
}

# Define the heuristic values for each node
heuristic = {
    'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 3, 'F': 2, 'G': 1, 'H': 0
}

def best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))
    came_from = {}
    
    while not frontier.empty():
        _, current_node = frontier.get()
        
        if current_node == goal:
            break
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in came_from or cost < came_from[neighbor]:
                came_from[neighbor] = current_node
                priority = cost + heuristic[neighbor]
                frontier.put((priority, neighbor))
    
    path = []
    node = goal
    while node != start:
        path.insert(0, node)
        node = came_from[node]
    path.insert(0, start)
    
    return path

# Run the Best-First Search algorithm
start_node = 'A'
goal_node = 'H'
path = best_first_search(graph, start_node, goal_node)

print("Best-First Search Path:", path)
