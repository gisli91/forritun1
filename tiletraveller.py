

# push 

def display(col, line):
    print("You can go to {}")

def make_move(user_move, col, line):
    if user_move == "n":
        line += 1
    elif user_move == "s":
        line -= 1
    elif user_move == "e":
        col += 1
    elif user_move == "w":
        col -= 1
    return line, col

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




def mover(direction):
