import heapq
from collections import defaultdict
def dijkstra(graph, start):
    shortest_dist = {node: float('inf') for node in graph}
    shortest_dist[start] = 0
    predecessors = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if (current_dist > shortest_dist[u]): continue

        for v, weight in graph[u].items():
            dist = current_dist + weight
            if dist < shortest_dist[v]:
                shortest_dist[v] = dist
                predecessors[v] = u
                heapq.heappush(pq, (dist, v))
    
    return shortest_dist, predecessors

def create_graph():
    graph = defaultdict(dict)

    nodes = input("enter nodes for the graph separated by space: ").strip().split()

    for node in nodes:
        graph[node] = {}

    print("enter edges for the graph:")

    while True:
        print(f"current graph: {dict(graph)}")

        start_node = input("enter starting node: ")
        if start_node not in graph: 
            print("node not present in graph, adding")

        end_node = input("enter end node")
        if end_node not in graph:
            print("node not present in graph, adding")
        
        weight = float(input("enter weight of edge: "))

        graph[start_node][end_node] = weight

        isBidirectional = True if input("is the edge bidirectional? (y/n): ") == 'y' else False

        if isBidirectional:
            graph[end_node][start_node] = weight

        if input("do you wanna add more edges? (y/n): ") == 'y':
            continue
        else:
            break

    return graph
        
def print_path(predecessors, start, end):
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = predecessors[node]
    
    path.reverse()

    if path[0] == start:
        print(f"path from {start} to {end} exists: {'->'.join(path)}")
    else:
        print(f"no path from {start} to {end} exists")


def display_graph(graph):
    if not graph:
        print("the graph is empty")
        return

    print("------------graph (adjacency list)------------")
    for node, neighbours in graph.items():
        if neighbours:
            print(f"{node}: {neighbours}")
        else:
            print(f"{node}: ×")

def run_dijkstra(graph):
    if not graph:
        print("graph is empty, create a graph first")
        return
    
    print(f"available nodes: {', '.join(graph.keys())}")
    start = input("enter starting node: ").strip()

    if start not in graph:
        print("starting node not in graph")
        return
    
    distances, predecessors = dijkstra(graph, start)

    print(f"--------shortest distances from {start}--------")
    for node, dist in distances.items():
        if (dist == float('inf')):
            print(f"{node}: unreachable")
        else:
            print(f"{node}: {dist}")
        print_path(predecessors, start, node)
        print()


def main():
    """Main menu-driven program"""
    graph = None
    
    while True:
        print("\n" + "="*50)
        print("   DIJKSTRA'S SHORTEST PATH ALGORITHM")
        print("="*50)
        print("1. Create a new graph")
        print("2. Use default graph")
        print("3. Display current graph")
        print("4. Run Dijkstra's algorithm")
        print("5. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            graph = create_graph()
            if graph:
                print("\nGraph created successfully!")
        
        elif choice == '2':
            continue
        
        elif choice == '3':
            display_graph(graph)
        
        elif choice == '4':
            run_dijkstra(graph)
        
        elif choice == '5':
            print("\nThank you for using the program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


