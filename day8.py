# Day 8
# DP Array to keep track of shortest in the current row
# and current column. Has to be all four ways as well.

score = 0
treeStore = []
NUMROWS = 0
NUMCOLS = 0
with open('day8.in') as f:
    for line in f:
        line = line.rstrip()
        line = [*line]
        line = list(map(int, line))
        treeStore.append([*line])
        NUMCOLS = len(line)
        NUMROWS += 1

# print(treeStore)

# smallest going (left, right, up, down)
import copy

initTreeStore = []
initTreeStore = copy.deepcopy(treeStore)
# print(initTreeStore)

# largestLeftCords = [[0] * NUMCOLS for i in range(NUMROWS)]
# largestRightCords =[[0] * NUMCOLS for i in range(NUMROWS)]
# largestBottomCords = [[0] * NUMCOLS for i in range(NUMROWS)]
# largestTopCords = [[0] * NUMCOLS for i in range(NUMROWS)]

# boolCoords = [[False] * NUMCOLS for i in range(NUMROWS)]

# for i in range(NUMROWS):
#     maxNum = -1
#     for j in range(NUMCOLS):
#         currNum = treeStore[i][j] 
#         boolCoords[i][j] = boolCoords[i][j] or (currNum > maxNum)
#         maxNum = max(currNum, maxNum)

# # TOP
# for i in range(NUMCOLS):
#     maxNum = -1
#     for j in range(NUMROWS):
#         currNum = treeStore[j][i] 
#         boolCoords[j][i] = boolCoords[j][i] or (currNum > maxNum)
#         maxNum = max(currNum, maxNum)


# for i in range(NUMROWS):
#     maxNum = -1
#     for j in range(NUMCOLS - 1, -1, -1):
#         currNum = treeStore[i][j] 
#         boolCoords[i][j] = boolCoords[i][j] or (currNum > maxNum)
#         maxNum = max(currNum, maxNum)

# for i in range(NUMCOLS):
#     maxNum = -1
#     for j in range(NUMROWS - 1, -1, -1):
#         currNum = treeStore[j][i] 
#         boolCoords[j][i] = boolCoords[j][i] or (currNum > maxNum)
#         maxNum = max(currNum, maxNum)

# for i in boolCoords:
#     for j in i:
#         if j:
#             score += 1

# print(score)



# Check
# treeStore = initTreeStore.copy()
# for i in range(NUMROWS):
#     for j in range(NUMCOLS):
#         currNum = treeStore[i][j] 
#         if currNum > largestBottomCords[i][j] or currNum > largestLeftCords[i][j] or currNum > largestRightCords[i][j] or currNum > largestTopCords[i][j]:
#             score += 1
#         else:
#             print(f"{i=} {j=}")

# print("~~~~")
# print(score)
# for i in initTreeStore:
#     print(i)
# print("~~~~")

# for i in largestTopCords:
#     print(i)
# print()
# for i in largestBottomCords:
#     print(i)

def exploreRight(row, col, prev):
    if row < 0 or row > NUMROWS - 1 or col < 0 or col > NUMCOLS - 1:
        return 0
    else:
        if treeStore[row][col] >= prev:
            return 1
        else:
            return 1 + exploreRight(row, col + 1, prev)
            
def exploreLeft(row, col, prev):
    if row < 0 or row > NUMROWS - 1 or col < 0 or col > NUMCOLS - 1:
        return 0
    else:
        if treeStore[row][col] >= prev:
            return 1
        else:
            return 1 + exploreLeft(row, col - 1, prev)

def exploreUp(row, col, prev):
    if row < 0 or row > NUMROWS - 1 or col < 0 or col > NUMCOLS - 1:
        return 0
    else:
        if treeStore[row][col] >= prev:
            return 1
        else:
            return 1 + exploreUp(row - 1, col, prev)

def exploreDown(row, col, prev):
    if row < 0 or row > NUMROWS - 1 or col < 0 or col > NUMCOLS - 1:
        return 0
    else:
        if treeStore[row][col] >= prev:
            return 1
        else:
            return 1 + exploreDown(row + 1, col, prev)

def bfs(row, col):
    return exploreDown(row + 1, col, treeStore[row][col]) * exploreLeft(row, col - 1, treeStore[row][col]) * exploreRight(row, col + 1, treeStore[row][col]) * exploreUp(row - 1, col, treeStore[row][col])

for i in range(NUMROWS):
    for j in range(NUMCOLS):
        score = max(score, bfs(i, j))
print(score)