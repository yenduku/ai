from collections import deque

def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '0':  # Assume '0' represents the blank tile
                return i, j

def is_goal(state, goal_state):
    return state == goal_state

def generate_moves(state):
    moves = []
    x, y = find_blank_position(state)
    if x > 0:
        moves.append((x - 1, y))  # Move Up
    if x < 2:
        moves.append((x + 1, y))  # Move Down
    if y > 0:
        moves.append((x, y - 1))  # Move Left
    if y < 2:
        moves.append((x, y + 1))  # Move Right
    return moves

def swap_tiles(state, pos1, pos2):
    new_state = [row[:] for row in state]
    x1, y1 = pos1
    x2, y2 = pos2
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def solve_puzzle(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    
    while queue:
        current_state, path = queue.popleft()
        if is_goal(current_state, goal_state):
            return path
        
        for move in generate_moves(current_state):
            new_state = swap_tiles(current_state, find_blank_position(current_state), move)
            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                queue.append((new_state, path + [move]))
                
    return None

def input_state(name):
    while True:
        try:
            state_input = input(f"Enter the {name} state : ")
            state_list = state_input.split()
            
            # Check for any negative numbers
            if any(int(x) < 0 for x in state_list if x.isdigit()):
                raise ValueError("Negative numbers are not allowed.")
            
            if len(state_list) != 9:
                raise ValueError("Input must contain exactly 9 elements.")
            
            # Convert flat list to 3x3 matrix
            state = [state_list[i:i + 3] for i in range(0, 9, 3)]
            return state
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def print_state(state, name):
    print(f"\n{name} state:")
    for row in state:
        print(" ".join(row))

def print_move(current_state, new_state, direction):
    print(f"\nMoving {direction}:")
    print_state(current_state, "Current")
    print_state(new_state, "After Move")

# Main execution
initial_state = input_state("initial")
goal_state = input_state("goal")

print_state(initial_state, "initial")
solution = solve_puzzle(initial_state, goal_state)

if solution:
    print("\nSolution found!")
    for move in solution:
        current_position = find_blank_position(initial_state)
        direction = ""
        if move == (current_position[0] - 1, current_position[1]):
            direction = "Up"
        elif move == (current_position[0] + 1, current_position[1]):
            direction = "Down"
        elif move == (current_position[0], current_position[1] - 1):
            direction = "Left"
        elif move == (current_position[0], current_position[1] + 1):
            direction = "Right"
        
        new_state = swap_tiles(initial_state, current_position, move)
        print_move(initial_state, new_state, direction)
        initial_state = new_state  # Update the current state to the new state
else:
    print("\nNo solution exists")

print_state(goal_state, "goal")