
# sudoku to be solved
puzzle = [
    [9, 0, 0, 2, 6, 5, 8, 0, 0],
    [7, 0, 0, 4, 0, 0, 0, 6, 0],
    [6, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 3, 0, 2, 7, 0],
    [2, 0, 8, 0, 0, 0, 6, 0, 0],
    [3, 0, 6, 8, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 4, 0, 0],
    [4, 3, 2, 0, 8, 6, 7, 0, 0],
    [0, 6, 7, 0, 0, 0, 0, 0, 0]
]


def print_sudoku(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if j == 8:
                print(puzzle[i][j])
            else:
                print(puzzle[i][j], end=" ")


# get empty cell
def get_empty(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 0:
                return row, col
    return None


# test validation
def is_valid(puzzle, candidate, row, col):
    # check row
    if candidate in puzzle[row]:
        return False
    # check column
    if candidate in [puzzle[i][col] for i in range(len(puzzle))]:
        return False
    # check 3*3 box
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if puzzle[i][j] == candidate:
                return False
    return True


# solve puzzle
def solve_sudoku(puzzle):
    # get empty cell
    empty_cell = get_empty(puzzle)
    if not empty_cell:
        return True
    row, col = empty_cell

    for candidate in range(1, 10):
        if is_valid(puzzle, candidate, row, col):
            puzzle[row][col] = candidate
            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0

    return False


if __name__ == "__main__":
    print("input sudoku:")
    print_sudoku(puzzle)
    if solve_sudoku(puzzle):
        print("The solved sudoku is as follow:")
        print_sudoku(puzzle)
    else:
        print("The input sudoku is not solvable")