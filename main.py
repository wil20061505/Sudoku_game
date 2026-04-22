from quai_lui.backtracking import run_sudoku
from local_search.min_conflicts import solve_sudoku,print_table
import testcases as tc
if __name__ == "__main__":

    # bảng sudoku của quay lui
    board = tc.Backtracking_easy_1

    run_sudoku(board)


    #bản sudoku của local_search
    topic_input = tc.min_conflict_easy_1

    result = solve_sudoku(topic_input)

    if result:
        print("Đã giải xong")
        print_table()
    else:
        print("Không thể giải")