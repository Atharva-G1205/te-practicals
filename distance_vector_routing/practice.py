import copy

def input_cost_matrix():
    global n, cost, dist, next_hop
    n = int(input("Enter the number of nodes in the network: "))
    print("Enter the cost matrix (use 999 for infinity where no direct link exists):")
    cost = []
    for i in range(n):
        row = list(map(int, input(f"Cost from node {i} to others: ").split()))
        cost.append(row)
    dist = copy.deepcopy(cost)
    next_hop = [[j if cost[i][j] != 999 else -1 for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][i] = 0
        next_hop[i][i] = i
    print("Cost matrix and tables initialized.")

def compute_routing_tables():
    global dist, next_hop
    if 'cost' not in globals():
        print("Please input the cost matrix first.")
        return
    updated = True
    while updated:
        updated = False
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_hop[i][j] = next_hop[i][k]
                        updated = True
    print("Routing tables computed.")

def display_routing_tables():
    if 'dist' not in globals() or 'next_hop' not in globals():
        print("Please input the cost matrix and compute the routing tables first.")
        return
    print("\n--- Final Routing Tables ---")
    for i in range(n):
        print(f"\nRouting table for router {i}:")
        print("Destination\tNext Hop\tDistance")
        for j in range(n):
            if i != j:
                nh = next_hop[i][j] if next_hop[i][j] != -1 else "None"
                print(f"{j}\t\t{nh}\t\t{dist[i][j]}")

def main_menu():
    while True:
        print("\n--- Distance Vector Routing Menu ---")
        print("1. Input cost matrix")
        print("2. Compute routing tables")
        print("3. Display routing tables")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            input_cost_matrix()
        elif choice == '2':
            if 'cost' not in globals():
                print("Please input the cost matrix first.")
            else:
                compute_routing_tables()
        elif choice == '3':
            display_routing_tables()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
