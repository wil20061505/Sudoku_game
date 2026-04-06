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
    
    c = (column // 3) * 3 # tính vị trí cột của box
    r = (row // 3) * 3 # tính vị trí hàng của box
    count = 0
    for i in range (3):
        for j in range (3):
            if (r + i == row) and (c + j == column): continue
            if value == topic[r + i][c + j]: count += 1
            
    # đếm theo 
    for j in range(9): # đếm theo hàng
        if column == j: continue
        if value == topic[row][j]: count += 1
     
    for i in range(9): # đếm theo cột
        if row == i: continue
        if value == topic[i][column]: count += 1
    return count     

topic = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
tableConflict = [[False]*9 for _ in range(9)]

def checkConflict(i, j):
    if tableConflict[i][j] == True: # True == conflict
        return True
    return False

# Tìm ra vị trí có conflict n hở nhất trong ô 3x3
def find_Min_Conflict(i, j, value):
    row = (i // 3) * 3
    col = (j // 3) * 3
    tempMinConflict = Conflict(100, 100, 100)
    for r in range(3):
        for c in range(3):
            count = count_conflict(row + r, col + c, value)
            if tempMinConflict.error > count:
                tempMinConflict.error = count
                tempMinConflict.indexRow = r + row
                tempMinConflict.indexCol = c + col
    return tempMinConflict

def swap(a:Conflict, b:Conflict):
    c = a
    a.indexCol = b.indexCol
    a.indexRow = b.indexRow
    b.indexCol = c.indexCol
    b.indexRow = c.indexRow
    
# kiểm tra conflict toàn bảng
def updateConflictTable():
    
    for i in range(9):
        for j in range(9):
            if count_conflict(i, j, topic[i][j]) > 0:
                tableConflict[i][j] = True
            else:
                tableConflict[i][j] = False


# hàm giải thuật Min-Conflicts
def min_conflicts(max_steps = 1000):
    #print(1)
    for step in range(max_steps):
        conflicted = [(i, j) for i in range(9) for j in range(9) if tableConflict[i][j]]
        if not conflicted: return
        i, j = random.choice(conflicted)
        
        #i = random.randint(0, 8)
        #j = random.randint(0, 8)
        #while checkConflict(i, j) != True:
        #    i = random.randint(0, 8)
        #    j = random.randint(0, 8)
        #    checkConflict(i, j)

        indexMinConflict = find_Min_Conflict(i, j, topic[i][j])
        indexCurrent = Conflict(1, i, j)
        # mỗi lần đổi kiểm tra lại conflict toàn bảng
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
    min_conflicts()
    if check():
        print("Đã giải xong")
        print_table()
    else:
        print("Không thể giải được")    



