




def victory_condition(col, line):
    if col == 3 and line == 1:
        print("Victory!")
        return True
    return False




def make_move(user_input, col, line):
    

    if user_input == "n" and line < 3:
        line += 1
    elif user_input == "s" and line > 1:
        line -= 1
    elif user_input == "e" and col < 3:
        col += 1
    elif user_input == "w" and col > 1:
        col -= 1
    return col, line

def invalid_move(user_input, col,line):
    
    if col == 1 and line == 1 and user_input != "n":
        print("Not a valid direction!")
    if col == 1 and line == 2 and user_input == "w":
        print("Not a valid direction!")
    if col == 1 and line == 3 and (user_input != "e" or user_input != "s"):
        print("Not a valid direction!")
    if col == 2 and line == 1 and user_input != "n":
        print("Not a valid direction!")
    if col == 2 and line == 2 and (user_input != "s" or user_input != "w"):
        print("Not a valid direction!")
    if col == 2 and line == 3 and (user_input != "w" or user_input != "e"):
        print("Not a valid direction!")
    if col == 3 and line == 1 and user_input != "n":
        print("Not a valid direction!")
    if col == 3 and line == 2 and (user_input != "n" or user_input != "s"):
        print("Not a valid direction!")
    if col == 3 and line == 3 and (user_input != "s" or user_input != "w"):
        print("Not a valid direction!")

def where(col, line):
    if col == 1:
        if line == 1:
            print("You can travel: (N)orth.")
        elif line == 2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif line == 3: 
            print("You can travel: (S)outh or (E)ast.")
        
    elif col == 2:
        if line == 1:
            print("You can travel: (N)orth.")
        elif line == 2: 
            print("You can travel: (W)est.")
        elif line == 3: 
            print("You can travel: (E)east or (W)est.")
       
    elif col == 3:
        if line == 1: 
            print("You can travel: (N)orth.")
        elif line == 2:
            print("You can travel: (N)orth or (S)outh.")
        elif line == 3: 
            print("You can travel: (E)ast or (S)outh.")
    


col = 1
line = 1

victory = False

while not victory:
    where(col,line)
    user_input = input("Direction: ")
    user_input = user_input.lower()
    invalid_move(user_input,col,line)
    col, line = make_move(user_input,col,line)
    victory = victory_condition(col, line)
