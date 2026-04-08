from multiprocessing import Value
import random

# "┌"  "─"  "┐"  "├"  "─"  "┤"  "└"  "─"  "┘"  "│" "┬ ┴ ┼"

#lưu conflict
class Conflict:
    def __init__(self, error, indexRow, indexCol):
        self.error = error
        self.indexRow = indexRow
        self.indexCol = indexCol

# hàm đếm conflict    
def count_conflict(row, column, value):
    # đếm trong ô 3x3
    count = 0
    r = (row // 3) * 3
    c = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            ni, nj = r+i, c+j
            if ni == row or nj == column:
                continue
            if topic[ni][nj] == value:
                count += 1
            
    # đếm theo 
    for j in range(9): # đếm theo hàng
        if column == j: continue
        if value == topic[row][j]: count += 1
     
    for i in range(9): # đếm theo cột
        if row == i: continue
        if value == topic[i][column]: count += 1
    return count     

 
topic = [
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

tableConflict = [[False]*9 for _ in range(9)]

def checkConflict(i, j):
    if tableConflict[i][j] == True: # True == conflict
        return True
    return False

# Tìm ra vị trí có conflict n hở nhất trong ô 3x3
def find_Min_Conflict(i, j):
    row = (i // 3) * 3
    col = (j // 3) * 3
    best = Conflict(100, i, j)

    for r in range(3):
        for c in range(3):
            ni, nj = row + r, col + c
            
            # swap thử
            topic[i][j], topic[ni][nj] = topic[ni][nj], topic[i][j]
            
            conflict = count_conflict(i, j, topic[i][j]) + count_conflict(ni, nj, topic[ni][nj])
            
            if conflict < best.error:
                best.error = conflict
                best.indexRow = ni
                best.indexCol = nj
            
            # swap lại
            topic[i][j], topic[ni][nj] = topic[ni][nj], topic[i][j]

    return best

def swap(a: Conflict, b: Conflict):
    topic[a.indexRow][a.indexCol], topic[b.indexRow][b.indexCol] = \
        topic[b.indexRow][b.indexCol], topic[a.indexRow][a.indexCol]
    
# kiểm tra conflict toàn bảng
def updateConflictTable():
    
    for i in range(9):
        for j in range(9):
            if count_conflict(i, j, topic[i][j]) > 0:
                tableConflict[i][j] = True
            else:
                tableConflict[i][j] = False

def init_random():
    for block in range(9):
        nums = list(range(1, 10))
        row = (block // 3) * 3
        col = (block % 3) * 3

        # remove fixed numbers nếu có đề bài

        random.shuffle(nums)
        k = 0
        for i in range(3):
            for j in range(3):
                topic[row+i][col+j] = nums[k]
                k += 1

def solve():
    for _ in range(50):  # restart 50 lần
        init_random()    # xáo lại bảng
        updateConflictTable()
        min_conflicts()
        if check():
            return True
    return False

# hàm giải thuật Min-Conflicts
def min_conflicts(max_steps = 1000000):
    #print(1)
    for step in range(max_steps):
        print(step)
        conflicted = [(i, j) for i in range(9) for j in range(9) if tableConflict[i][j]]
        if not conflicted: return
        i, j = random.choice(conflicted)
        
        indexMinConflict = find_Min_Conflict(i, j)
        indexCurrent = Conflict(1, i, j)
        # mỗi lần đổi kiểm tra lại conflict toàn bảng
        #swap(indexCurrent, indexMinConflict)
        if random.random() < 0.1:
            row = (i // 3) * 3
            col = (j // 3) * 3
            while True:
                ri = row + random.randint(0,2)
                rj = col + random.randint(0,2)
                if ri != i or rj != j:
                    break
            swap(indexCurrent, Conflict(0, ri, rj))
        else:
            swap(indexCurrent, indexMinConflict)
        updateConflictTable()

            
# check lại
def check():
    for i in range(9):
        for j in range(9):
            if count_conflict(i, j, topic[i][j]) != 0:
                return False
    return True

def print_table():
    for i in range(9):
        for j in range(9):
            print(topic[i][j], end = " ")
        print("\n")

if __name__ == "__main__":
    updateConflictTable()
    solve()
    if check():
        print("Đã giải xong")
        print_table()
    else:
        print("Không thể giải được")    



