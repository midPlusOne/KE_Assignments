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
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 0
}

# Define the Best-First Search algorithm without considering cost
def best_first_search_without_cost(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))
    
    came_from = {}
    
    came_from[start] = None
    
    while not frontier.empty():
        
        current_heuristic, current_node = frontier.get()
        if current_node == goal:
            break
        
        for next_node in graph[current_node]:
            if next_node not in came_from:
                frontier.put((heuristic[next_node], next_node))
                came_from[next_node] = current_node
    
    path = []
    current_node = goal
    while current_node != start:
        path.insert(0, current_node)
        current_node = came_from[current_node]
    
    path.insert(0, start)
    
    return path

start_node = 'A'
goal_node = 'H'
path = best_first_search_without_cost(graph, start_node, goal_node)

print("Best-First Search Path:", path)