# Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

# The data structure is a multi-dimensional Array, i.e:

# [
#   [7,8,4,  1,5,9,  3,2,6],
#   [5,3,9,  6,7,2,  8,4,1],
#   [6,1,2,  4,3,8,  7,5,9],

#   [9,2,8,  7,1,5,  4,6,3],
#   [3,5,7,  8,4,6,  1,9,2],
#   [4,6,1,  9,2,3,  5,8,7],

#   [8,7,6,  3,9,4,  2,1,5],
#   [2,4,3,  5,6,1,  9,7,8],
#   [1,9,5,  2,8,7,  6,3,4]
# ]
# Rules for validation

# Data structure dimension: NxN where N > 0 and √N == integer
# Rows may only contain integers: 1..N (N included)
# Columns may only contain integers: 1..N (N included)
# 'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

class Sudoku(object):
    def __init__(self, data):
    
        rows_dict = {}
        columns_dict = {}
        squares_dict = {}
        for i in range(len(data)):
            if i not in rows_dict:
                rows_dict[i] = data[i]
            for j in range(len(data[i])):
                if j not in columns_dict:
                    columns_dict[j] = []
                columns_dict[j].append(data[i][j])
                
                root = len(data)**.5
                square = str(int(i/root)) + '_' + str(int(j/root))
                if square not in squares_dict:
                    squares_dict[square] = []
                squares_dict[square].append(data[i][j])
                
        self.rows = rows_dict
        self.columns = columns_dict
        self.squares = squares_dict
        
    def is_valid(self):
        for row in self.rows:
            if len([elem for elem in self.rows[row] if type(elem) != int]) != 0:
                return False
            if sorted(self.rows[row]) != list(range(1, len(self.rows) + 1)):
                return False
        for column in self.columns:
            if sorted(self.columns[column]) != list(range(1, len(self.rows) + 1)):
                return False
        for square in self.squares:
            if sorted(self.squares[square]) != list(range(1, len(self.rows) + 1)):
                return False
        return True