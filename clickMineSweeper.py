# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] != 0:
        return field
    
    to_check = [(given_i, given_j)]
    while to_check:
        i, j = to_check.pop()
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x >= 0 and x < num_rows) and (y >= 0 and y < num_cols) and (field[x][y] == 0):
                    field[x][y] = -2
                    to_check.append((x, y))
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


if __name__ == "__main__":

    # NOTE: The following input values will be used for testing your solution.
    field1 = [[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, -1, 1, 0]]
    result = click(field1, 3, 5, 1, 4)
    print(to_string(result))
    # click(field1, 3, 5, 2, 2) should return:
    # [[0, 0, 0, 0, 0],
    #  [0, 1, 1, 1, 0],
    #  [0, 1, -1, 1, 0]]

    # click(field1, 3, 5, 1, 4) should return:
    # [[-2, -2, -2, -2, -2],
    #  [-2, 1, 1, 1, -2],
    #  [-2, 1, -1, 1, -2]]


    field2 = [[-1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, -1]]

    # click(field2, 4, 4, 0, 1) should return:
    # [[-1, 1, 0, 0],
    #  [1, 1, 0, 0],
    #  [0, 0, 1, 1],
    #  [0, 0, 1, -1]]

    # click(field2, 4, 4, 1, 3) should return:
    # [[-1, 1, -2, -2],
    #  [1, 1, -2, -2],
    #  [-2, -2, 1, 1],
    #  [-2, -2, 1, -1]]
