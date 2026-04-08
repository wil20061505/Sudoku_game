from do_thoi_gian import measure_time

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

    for j in range(9):
        if board[row][j] == num and col != j:
            return False

    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


@measure_time
def run_sudoku(board):
    print("Sudoku ban đầu:")
    print_board(board)

    if solve(board):
        print("\nSudoku sau khi giải:")
        print_board(board)
        return True
    else:
        print("\nKhông có lời giải!")
        return False


