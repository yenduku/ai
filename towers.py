def print_towers(towers):
    height = max(len(towers['Source']), len(towers['Destination']), len(towers['Auxiliary']))
    
    for i in range(height - 1, -1, -1):
        for tower in ['Source', 'Destination', 'Auxiliary']:
            if i < len(towers[tower]):
                print(f" {towers[tower][i]} ", end="\t")
            else:
                print(" | ", end="\t")
        print()  
    print("---------------------------")
    print("Source\tDestination\tAuxiliary\n")

def tower_of_hanoi(n, source, destination, aux, towers, step):
    if n == 1:
        disk = towers[source].pop()
        towers[destination].append(disk)
        step[0] += 1
        print(f"Step {step[0]}: Move disk {disk} from {source} to {destination}")
        print_towers(towers)
        return
    
    tower_of_hanoi(n - 1, source, aux, destination, towers, step)
    
    disk = towers[source].pop()
    towers[destination].append(disk)
    step[0] += 1
    print(f"Step {step[0]}: Move disk {disk} from {source} to {destination}")
    print_towers(towers)
    
    tower_of_hanoi(n - 1, aux, destination, source, towers, step)

def get_valid_number():
    while True:
        user_input = input("Enter the number of disks: ")
        try:
            n = int(user_input)
            if n <= 0:
                print("Please enter a positive number greater than 0.")
            else:
                return n
        except ValueError:
            if user_input.strip().lower() == 's':
                print("You entered 's'. Please input a number to solve the Tower of Hanoi.")
            else:
                print("Invalid input! Please enter a valid number.")

n = get_valid_number()

towers = {
    'Source': list(range(n, 0, -1)), 
    'Destination': [],
    'Auxiliary': []
}

print("Initial state:")
print_towers(towers)

step = [0]  
tower_of_hanoi(n, 'Source', 'Destination', 'Auxiliary', towers, step)