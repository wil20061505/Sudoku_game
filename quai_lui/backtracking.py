def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # trả về vị trí ô trống
    return None


def is_valid(board, num, pos):
    row, col = pos

    # Kiểm tra hàng
    for j in range(9):
        if board[row][j] == num and col != j:
            return False

    # Kiểm tra cột
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Kiểm tra ô 3x3
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # đã giải xong

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # quay lui

    return False


# Ví dụ Sudoku (0 là ô trống)
board = [
    [0, 4, 2, 0, 0, 5, 0, 0, 6],
    [1, 9, 7, 0, 0, 0, 0, 4, 0],
    [5, 6, 0, 4, 0, 0, 1, 0, 9],
    [8, 0, 1, 3, 0, 0, 2, 6, 0],
    [9, 0, 0, 0, 7, 1, 4, 5, 0],
    [0, 0, 3, 2, 5, 6, 0, 0, 0],
    [0, 0, 5, 0, 3, 2, 7, 0, 0],
    [0, 0, 4, 5, 9, 0, 6, 0, 0],
    [0, 0, 0, 7, 6, 0, 0, 8, 0]
]

print("Sudoku ban đầu:")
print_board(board)

if solve_sudoku(board):
    print("\nSudoku sau khi giải:")
    print_board(board)
else:
    print("Không có lời giải!")