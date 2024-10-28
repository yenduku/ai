import itertools

# Function to get positive input from the user
def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive number.")

# Function to get the source matrix (distance matrix)
def get_distance_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Distance to itself is 0
            else:
                distance = get_positive_input(f"Enter distance from node {i+1} to node {j+1}: ")
                row.append(distance)
        matrix.append(row)
    return matrix

# Function to calculate the total distance of a path
def calculate_path_distance(matrix, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += matrix[path[i]][path[i+1]]
    total_distance += matrix[path[-1]][path[0]]  # Returning to the start
    return total_distance

# Function to find the minimum distance path using brute force approach
def travelling_salesman(matrix, n):
    nodes = list(range(n))
    all_permutations = itertools.permutations(nodes[1:])  # All permutations excluding the starting node
    min_distance = float('inf')
    best_path = None
    
    for perm in all_permutations:
        path = [0] + list(perm)  # Fixing the first node as the start point (node 0)
        current_distance = calculate_path_distance(matrix, path)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path
    
    return best_path, min_distance

# Main function to execute the TSP
def main():
    # Get number of nodes
    n = int(get_positive_input("Enter number of nodes: "))
    
    # Get distance matrix
    print("Enter the source matrix (distance between nodes):")
    matrix = get_distance_matrix(n)
    
    # Solve the TSP
    best_path, min_distance = travelling_salesman(matrix, n)
    
    # Display the results
    print("\nOptimal path:", " -> ".join(str(node+1) for node in best_path), " -> ", best_path[0]+1)
    print(f"Minimum distance: {min_distance:.2f}")

if __name__ == "__main__":
    main()
