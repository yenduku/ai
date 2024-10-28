class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position, parent=None):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_position = boat_position
        self.parent = parent

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0 and self.boat_position == 1

    def is_valid(self, total_missionaries, total_cannibals):
        if (self.missionaries_left < 0 or self.cannibals_left < 0 or
            self.missionaries_left > total_missionaries or self.cannibals_left > total_cannibals):
            return False

        if (self.missionaries_left > 0 and self.missionaries_left < self.cannibals_left) or \
           (total_missionaries - self.missionaries_left > 0 and total_missionaries - self.missionaries_left < total_cannibals - self.cannibals_left):
            return False

        return True

    def get_possible_moves(self, boat_capacity, total_missionaries, total_cannibals):
        moves = []
        for m in range(boat_capacity + 1):
            for c in range(boat_capacity + 1):
                if 1 <= m + c <= boat_capacity:
                    if self.boat_position == 0:  
                        new_state = State(self.missionaries_left - m, self.cannibals_left - c, 1, self)
                    else:  
                        new_state = State(self.missionaries_left + m, self.cannibals_left + c, 0, self)

                    if new_state.is_valid(total_missionaries, total_cannibals):
                        moves.append(new_state)

        return moves

    def _eq_(self, other):
        return (self.missionaries_left == other.missionaries_left and
                self.cannibals_left == other.cannibals_left and
                self.boat_position == other.boat_position)

    def _hash_(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_position))

    def _repr_(self):
        return f"State({self.missionaries_left}M, {self.cannibals_left}C, Boat {'Left' if self.boat_position == 0 else 'Right'})"


def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()

    step_number = 1
    for i in range(1, len(path)):
        m_moved = abs(path[i].missionaries_left - path[i-1].missionaries_left)
        c_moved = abs(path[i].cannibals_left - path[i-1].cannibals_left)
        move_direction = "Right" if path[i].boat_position == 1 else "Left"
        previous_direction = "Left" if path[i-1].boat_position == 0 else "Right"

        # Display the movement in set format
        print(f"Step {step_number}:")
        print(f"Move: {{Moved {m_moved}M, {c_moved}C from {previous_direction} to {move_direction}}}")
        
        # Boat position as 1B or 0B and state of banks in set format
        left_bank_boat = "1B" if path[i].boat_position == 0 else "0B"
        right_bank_boat = "1B" if path[i].boat_position == 1 else "0B"
        
        # State of left and right bank as sets with boat position
        print(f"State: {{Left : ({path[i].missionaries_left}M, {path[i].cannibals_left}C, {left_bank_boat}) --> Right : ({total_missionaries - path[i].missionaries_left}M, {total_cannibals - path[i].cannibals_left}C, {right_bank_boat})}}")
        print()
       

        step_number += 1


def bfs_solve(start_state, total_missionaries, total_cannibals, boat_capacity):
    queue = [start_state]
    explored = set()

    while queue:
        current_state = queue.pop(0)
        if current_state.is_goal():
            print("Solution found!")
            print_solution(current_state)
            return True

        explored.add(current_state)

        for next_state in current_state.get_possible_moves(boat_capacity, total_missionaries, total_cannibals):
            if next_state not in explored:
                queue.append(next_state)

    print("No solution found!")
    return False


def is_valid_positive_integer(value):
    try:
        val = int(value)
        if val > 0:
            return val
        else:
            print("Input must be a positive number.")
            return None
    except ValueError:
        print("Input must be a number.")
        return None


def main():
    global total_missionaries, total_cannibals

    while True:
        missionaries_input = input("Enter the number of missionaries: ")
        total_missionaries = is_valid_positive_integer(missionaries_input)
        if total_missionaries is not None:
            break

    while True:
        cannibals_input = input("Enter the number of cannibals: ")
        total_cannibals = is_valid_positive_integer(cannibals_input)
        if total_cannibals is not None:
            break

    while True:
        boat_capacity_input = input("Enter the boat capacity : ")
        boat_capacity = is_valid_positive_integer(boat_capacity_input)
        if boat_capacity is not None and boat_capacity <= 100:
            break
        else:
            print("Boat capacity must be valid in range.")

    if total_cannibals > total_missionaries:
        print("No solution found! Cannibals cannot outnumber missionaries.")
        return

    start = State(total_missionaries, total_cannibals, 0)
    bfs_solve(start, total_missionaries, total_cannibals, boat_capacity)
    print("All missionaries and cannibels crossed the river successfully!\nGoal state is reached")



if __name__ == "__main__":
    main()