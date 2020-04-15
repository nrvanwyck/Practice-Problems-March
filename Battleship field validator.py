# Write a method that takes a field for well-known board game "Battleship" as 
# an argument and returns true if it has a valid disposition of ships, false 
# otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements 
# in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

# Battleship (also Battleships or Sea Battle) is a guessing game for two 
# players. Each player has a 10x10 grid containing several "ships" and 
# objective is to destroy enemy's forces by targetting individual cells on his 
# field. The ship occupies one or more cells in the grid. Size and number of 
# ships may differ from version to version. In this kata we will use 
# Soviet/Russian version of the game.

# Before the game begins, players set up the board and place the ships 
# accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 
# destroyers (size 2) and 4 submarines (size 1). Any additional ships are not 
# allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just 
# single cell.

# The ship cannot overlap or be in contact with any other ship, neither by 
# edge nor by corner.

# This is all you need to solve this kata. If you're interested in more 
# information about the game, visit this link.

def validate_battlefield(field):
    adjacentcy_dict = {}
    for i in range(10):
        for j in range(10):
            if field[i][j] == 1:
                coordinates = str(i) + '|' + str(j)
                adjacentcy_dict[coordinates] = None
                if (i < 9) and (j < 9):
                    if field[i + 1][j + 1] == 1:
                        return False
                if (i < 9) and (j > 0):
                    if field[i + 1][j - 1] == 1:
                        return False
                if (i > 0):
                    if field[i - 1][j] == 1:
                        adjacent = str(i - 1) + '|' + str(j)
                        adjacentcy_dict[adjacent] = coordinates
                if (j > 0):
                    if field[i][j - 1] == 1:
                        adjacent = str(i) + '|' + str(j - 1)
                        adjacentcy_dict[adjacent] = coordinates
    
    visited = set()
    ships = {'battleship': 0, 'cruiser': 0, 'destroyer': 0, 'submarine': 0}
    for key in sorted(adjacentcy_dict):
        if key not in visited:
            visited.add(key)
            counter = 1
            while adjacentcy_dict[key] != None:
                key = adjacentcy_dict[key]
                counter += 1
                visited.add(key)
            if counter == 1:
                if ships['submarine'] < 4:
                    ships['submarine'] += 1
                else:
                    return False
            elif counter == 2:
                if ships['destroyer'] < 3:
                    ships['destroyer'] += 1
                else:
                    return False
            elif counter == 3:
                if ships['cruiser'] < 2:
                    ships['cruiser'] += 1
                else:
                    return False
            elif counter == 4:
                if ships['battleship'] < 1:
                    ships['battleship'] += 1
                else:
                    return False
    
    if ships != {'battleship': 1,
                 'cruiser': 2,
                 'destroyer': 3,
                 'submarine': 4}:
        return False
    
    return True