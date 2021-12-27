# This program takes in data representing house prices from a file and puts 
# them into a grid. The zeros in the data are replaced by the average of the
# neighbouring houses. Then shows the total average housing price and maximum
# housing price.

def create_grid(filename):
    # Create a nested list based on the data given in a file and returns a 
    # two-dimensional nested list populated with data
    # - filename is a string representing the name of a file
    
    # opens file and reads it
    file = open(filename, 'r')
    data = file.read()
    file.close()
    data = data.splitlines()
    
    # the first 2 numbers in the file tell the number of rows and cols
    num_of_rows = int(data[0])
    num_of_col = int(data[1])
    counter = 2
    grid = []
    for row_index in range(num_of_rows):
        row = []
        for col_index in range(num_of_col):
            row.append(int(data[counter]))
            counter += 1
        grid.append(row) 
    
    return grid
        
def display_grid(grid):
    # Displays the grid by printing it to the terminal
    # - grid is a two-dimensional nested list

    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            number = grid[row_index][col_index]
            number = round(number)
            # prints | before each number
            print('|', end = ' ')
            print(number, '', end = '') 
        # prints | at the end of each row
        print('|')
        
def find_neighbors(row_index, col_index, grid):
    # Finds the values of all the neighbors of a particular cell in the grid 
    # and returns list with the values of all the neighbors of a given cell
    # - row_index is an int representing the row index
    # - col_index is an int representing the column index
    # - grid is a two-dimensional nested list

    spot_to_the_left = col_index - 1
    spot_to_the_right = col_index + 1
    spot_above = row_index - 1
    spot_below = row_index + 1
    row_max = len(grid) - 1
    col_max = len(grid[0]) - 1
    neighbors = []
    
    # checks if spots to the left of a particular cell are in range, if not
    # they do not exist
    if  spot_to_the_left >= 0: 
        neighbors.append(grid[row_index][spot_to_the_left])
        if spot_above >= 0: 
            neighbors.append(grid[spot_above][spot_to_the_left])     
        if spot_below <= row_max:  
            neighbors.append(grid[spot_below][spot_to_the_left])
     
    # checks if spots to the right of a particular cell are in range, if not
    # they do not exist           
    if spot_to_the_right <= col_max:
        neighbors.append(grid[row_index][spot_to_the_right])
        if spot_above >= 0: 
            neighbors.append(grid[spot_above][spot_to_the_right]) 
        if spot_below <= row_max:
            neighbors.append(grid[spot_below][spot_to_the_right])
        
    # checks if spots directly above of a particular cell are in range, if not
    # they do not exist          
    if spot_above >= 0: 
        neighbors.append(grid[spot_above][col_index])  
        
    # checks if spots directly below of a particular cell are in range, if not
    # they do not exist       
    if spot_below <= row_max: 
        neighbors.append(grid[spot_below][col_index]) 
        
    return neighbors

def fill_gaps(grid):
    # Creates a new two-dimensional list that is identical to the original, but 
    # with all zero-cells replaced with the average of their neighbors.
    # - grid is a two-dimensional nested list
    
    new_grid = []
    for row_index in range(len(grid)):
        row = []
        for col_index in range(len(grid[0])):
            # appends each cell from grid into new_grid
            row.append(grid[row_index][col_index])
            if grid[row_index][col_index] == 0:
                neighbors = find_neighbors(row_index, col_index, grid)
                # gets the average of neigboring cells and replaces the 0
                new_zero_cell = (sum(neighbors) / len(neighbors))
                row[col_index] = new_zero_cell          
        new_grid.append(row)
    return new_grid
    
def find_max(grid):
    # Find and returns the maximum house value in all cells in the grid
    # - grid is a two-dimensional nested list
    
    current_num = 0
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            # goes through every cell and checks if it is bigger than the last
            if grid[row_index][col_index] > current_num:    
                current_num = grid[row_index][col_index]
                largest_num = grid[row_index][col_index]
    return largest_num
    
def find_average(grid):
    # Finds and returns the average house value in all cells in the grid 
    # - grid is a two-dimensional nested list
    
    # empty list for the sum of each row
    sums = []
    length = 0
    for row in grid:
        # gets sum of each row
        sums.append(sum(row))   
        # adding length of each row through each iteration of the loop
        length += len(row)
    average = sum(sums) / length
    return round(average)
    
def main():
    
    grid = create_grid('data_2.txt')
    print('This is our grid:')
    display_grid(grid)
    # creates a new grid with zeros replaced
    new_grid = fill_gaps(grid)
    print('This is our newly calculated grid:')
    display_grid(new_grid)
    print('STATS')
    print('Average housing price in this area is:', find_average(new_grid))
    print('Maximum housing price in this area is:', find_max(new_grid))
    
main()
