def blox_solver(ar):
    valid_moves = {}
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            position = str(i) + '_' + str(j)
            valid_moves[position] = {}
            if ar[i][j] not in [0, 'X']:
                if (i > 1):
                    if (ar[i - 1][j] not in [0, 'X']) and (
                        ar[i - 2][j] not in [0, 'X']):
                        up = str(i - 2) + '|' + str(i - 1) + '_' + str(j)
                        valid_moves[position]['U'] = up
                        if up not in valid_moves:
                            valid_moves[up] = {}
                        valid_moves[up]['D'] = position
                if (j > 1):
                    if (ar[i][j - 1] not in [0, 'X']) and (
                        ar[i][j - 2] not in [0, 'X']):
                        left = str(i) + '_' + str(j - 2) + '|' + str(j - 1)
                        valid_moves[position]['L'] = left
                        if left not in valid_moves:
                            valid_moves[left] = {}
                        valid_moves[left]['R'] = position
                if (i < (len(ar) - 2)):
                    if (ar[i + 1][j] not in [0, 'X']) and (
                        ar[i + 2][j] not in [0, 'X']):
                        down = str(i + 1) + '|' + str(i + 2) + '_' + str(j)
                        valid_moves[position]['D'] = down
                        if down not in valid_moves:
                            valid_moves[down] = {}
                        valid_moves[down]['U'] = position
                if (j < (len(ar[i]) - 2)):
                    if (ar[i][j + 1] not in [0, 'X']) and (
                        ar[i][j + 2] not in [0, 'X']):
                        right = str(i) + '_' + str(j + 1) + '|' + str(j + 2)
                        valid_moves[position]['R'] = right
                        if right not in valid_moves:
                            valid_moves[right] = {}
                        valid_moves[right]['L'] = position
            if ar[i][j] == 'B':
                start = position
                        
    for key in valid_moves:
        if '|' in key:
            row = key.split('_')[0]
            column = key.split('_')[1]
            if '|' in row:
                row_1 = int(row.split('|')[0])
                row_2 = int(row.split('|')[1])
                column = int(column)
                if column > 0:
                    if ((ar[row_1][column - 1] not in [0, 'X']) and (
                         ar[row_2][column - 1] not in [0, 'X'])):
                         valid_moves[key]['L'] = (str(row_1) + '|' + str(row_2) + 
                                                  '_' + str(column))
                if column < (len(ar[row_1]) - 1):
                    if ((ar[row_1][column + 1] not in [0, 'X']) and (
                         ar[row_2][column + 1] not in [0, 'X'])):
                         valid_moves[key]['R'] = (str(row_1) + '|' + str(row_2) + 
                                                  '_' + str(column))
                if row_1 > 0:
                    if ar[row_1 - 1][column] == 'X':
                        valid_moves[key]['U'] = 'X'
                if row_2 < (len(ar) - 1):
                    if ar[row_2 + 1][column] == 'X':
                        valid_moves[key]['D'] = 'X'
    
            elif '|' in column:
                column_1 = int(column.split('|')[0])
                column_2 = int(column.split('|')[1])
                row = int(row)
                if row > 0:
                    if ((ar[row - 1][column_1] not in [0, 'X']) and (
                         ar[row - 1][column_2] not in [0, 'X'])):
                         valid_moves[key]['L'] = (str(row) + '_' + str(column_1) + 
                                                  '|' + str(column_2))
                if row < (len(ar) - 1):
                    if ((ar[row + 1][column_1] not in [0, 'X']) and (
                         ar[row + 1][column_2] not in [0, 'X'])):
                         valid_moves[key]['R'] = (str(row) + '_' + str(column_1) + 
                                                  '|' + str(column_2))
                if column_1 > 0:
                    if ar[row][column_1 - 1] == 'X':
                        valid_moves[key]['U'] = 'X'
                if column_2 < (len(ar[row]) - 1):
                    if ar[row][column_2 + 1] == 'X':
                        valid_moves[key]['D'] = 'X'
    
    def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for move in graph[start]:
            node = graph[start][move]
            if node not in path:
                print(node)
                print(path)
                print()
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
        
    find_shortest_path(valid_moves, start, 'X', path=[])