import random 

#can be expanded
availbale_colors =["\033[31m",#red
                   "\033[32m",#green
                   "\033[33m",#yellow
                   "\033[34m",#blue
                   "\033[0m"] #defult

#Generate random pattern
def generate_pattern(rows, cols, num_colors):
    x_colours =[f"X{i+1}" for i in range(num_colors)]
    
    pattern = []
    
    #create 2d grid:
    for row in range(rows):
        #create a new list for every row
        row_pattern = []
        for col in range(cols):
            #asign random colours to eacah column in that row
            row_pattern.append(random.choice(x_colours))
        pattern.append(row_pattern)
    return pattern

def create_colour_map(num_colors):
    
    final_colours = availbale_colors[:num_colors]
    #asign colour to each X-varible
    colour_map = {f"X{i+1}":final_colours[i] for i in range(num_colors)}
    return colour_map

def print_pattern(pattern, colour_map):
    for row in pattern:
        coloured_row =[]
        for x in row:
            #get the colour of the X-variable
            colour_code=colour_map.get(x, availbale_colors[-1]) #return default colour if there is none
            coloured_row.append(f"{colour_code}X\033[0m")
        print(" ".join(coloured_row))
            
#Get user input: how many colours
def get_num_colours():
    while True:
        try:
            num_colors = int(input("Enter number of colours (max 4): " )) 
            if num_colors > 4:
                print("Please enter number lower than 5")
            elif num_colors > 0:
                return num_colors
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input! Please enter a whole number")

#Get user input: what size (row,col)
def get_size():
    while True:
        try:
            size = tuple(map(int,input("Enter number of rows and columns, comma seperated: " ).split(",")))
            if len(size) == 2 and size[0] > 0 and size[1]>0:
                return size
            else:
                print("Please enter a positive number for both rows and columns ")
        except ValueError:
            print("Invalid input! Please enter 2 whole numbers")


def calculate_variables():
    num_colors = get_num_colours()
    size  = get_size()
    pattern = generate_pattern(size[0], size[1], num_colors)
    colour_map = create_colour_map(num_colors)
    return num_colors, size, pattern, colour_map

def run_program():
    num_colors, size, pattern, colour_map = calculate_variables()
    print("Welcomce to Crochet Tapestry Generator!")
    print(f"Here is your {size} pattern:" )
    print_pattern(pattern, colour_map)
    
