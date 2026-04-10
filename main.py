from quai_lui.backtracking import run_sudoku
from local_search.min_conflicts import solve_sudoku,print_table
if __name__ == "__main__":

    # bảng sudoku của quay lui
    board = [
   [1, 0, 3, 6, 7, 0, 9, 4, 5],
    [5, 8, 0, 2, 0, 9, 7, 0, 1],
    [9, 6, 7, 1, 4, 5, 0, 2, 0],

    [0, 7, 0, 0, 0, 0, 5, 0, 9],
    [6, 9,0, 5, 8, 0, 2, 0, 4],
    [4, 5, 0, 7, 9, 2, 6, 1, 3],

    [0, 3, 0, 9, 0, 4, 1, 5, 7],
    [0, 1, 0, 8,0, 7, 4, 0, 6],
    [0, 4, 5, 3, 1, 0, 0, 9, 2]
    ]

    run_sudoku(board)


    #bản sudoku của local_search
    topic_input = [
        [1, 2, 3, 6, 7, 8, 9, 4, 5],
    [5, 8, 4, 2, 3, 9, 7, 6, 1],
    [9, 6, 7, 1, 4, 5, 3, 2, 8],

    [3, 7, 2, 4, 6, 1, 5, 8, 9],
    [6, 9, 1, 5, 8, 3, 2, 7, 4],
    [4, 5, 8, 7, 9, 2, 6, 1, 3],

    [8, 3, 6, 9, 2, 4, 1, 5, 7],
    [2, 1, 9, 8, 5, 7, 4, 3, 6],
    [7, 4, 5, 3, 1, 6, 8, 9, 2]
]

    result = solve_sudoku(topic_input)

    if result:
        print("Đã giải xong")
        print_table()
    else:
        print("Không thể giải")