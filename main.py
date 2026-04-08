from quai_lui.backtracking import run_sudoku
from local_search.min_conflicts import solve_sudoku,print_table
if __name__ == "__main__":

    # bảng sudoku của quay lui
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    run_sudoku(board)


    #bản sudoku của local_search
    topic_input = [
        [8, 1, 7, 3, 6, 4, 2, 5, 9],
        [5, 9, 4, 1, 2, 8, 3, 6, 7],
        [3, 2, 6, 9, 5, 7, 1, 8, 4],

        [2, 3, 5, 4, 1, 6, 7, 9, 8],
        [4, 7, 1, 8, 9, 2, 5, 3, 6],
        [6, 8, 9, 7, 3, 5, 4, 2, 1],

        [7, 6, 8, 2, 4, 3, 9, 1, 5],
        [1, 5, 3, 6, 7, 9, 8, 4, 2],
        [9, 4, 2, 5, 8, 1, 6, 7, 3]
    ]

    result = solve_sudoku(topic_input)

    if result:
        print("Đã giải xong")
        print_table()
    else:
        print("Không thể giải")