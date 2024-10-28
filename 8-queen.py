while True:
    user_input = input("Enter the n value of n*n board: ")

    try:
        n = int(user_input)

        if n <= 0:
            print("Please enter a positive number.")
            continue
        elif n == 3 or n == 2:
            print("Not possible. N-queen problem is only solvable for n > 3.")
            continue
        elif n >= 20:
            print("n value should be less than 20")
            continue
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")

matrix = [[0 for i in range(n)] for j in range(n)]  

while True:
    try:
        first_row = int(input("Enter a row for placing a queen to start: "))
        if first_row <= 0 or first_row > n:
            raise ValueError()
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        first_col = int(input("Enter a col for placing a queen to start: "))
        if first_col <= 0 or first_col > n:
            raise ValueError()
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

matrix[first_row - 1][first_col - 1] = 1  

def is_safe(matrix, row, col, n):  
    for i in range(row):  
        if matrix[i][col] == 1:  
            return False  
            
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j -= 1
   
    # Check lower-right diagonal
    i, j = row, col
    while j < n and i < n:
        if matrix[i][j] == 1:
            return False
        i += 1
        j += 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j += 1
       
    # Check lower-left diagonal
    i, j = row, col
    while j >= 0 and i < n:
        if matrix[i][j] == 1:
            return False
        i += 1
        j -= 1
           
    return True  

def solve_nqueens(matrix, row, n, col_taken):  
    if row >= n:  
        return True  

    if row == first_row - 1:  
        return solve_nqueens(matrix, row + 1, n, col_taken)  
       
    for col in range(n):  
        if col in col_taken:
            continue

        if is_safe(matrix, row, col, n):  
            matrix[row][col] = 1  
            col_taken.add(col)  

            if solve_nqueens(matrix, row + 1, n, col_taken):  
                return True  
                   
            matrix[row][col] = 0    
            col_taken.remove(col)  

    return False  

def print_grid(matrix):  
    print("\n+" + "---+" * len(matrix))  # Top border
    for row in matrix:
        print("|", end="")
        for cell in row:
            if cell == 1:
                print(" Q |", end="")  # Represent queen with 'Q'
            else:
                print(" . |", end="")  # Empty space
        print("\n+" + "---+" * len(matrix))  # Bottom border after each row

col_taken = {first_col - 1}
if solve_nqueens(matrix, 0, n, col_taken):  
    print("Solution found:")  
    print_grid(matrix)  # Call the grid display function
else:  
    print("No solution exists.")
