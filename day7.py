# Day 7

class ListNode:
    def __init__(self, parent=None):
        self.nextDirs = {}
        self.parentDir = parent
        self.filesSize = 0
        self.finalSize = 0

bruh = input().split(" ")
root = ListNode()
initRoot = root

while bruh:
    try:
        bruh = input().split(" ")
        # first I read in the input
        # then i check whether the first index is $, dir, or a file
        # If $, then do something based on the second command
        # If dir, add a node
        # Dir have children: either another dir, or a file

        if bruh[0] == "$":
            if bruh[1] == "cd":
                if bruh[2] == "..":
                    root = root.parentDir
                else:
                    root = root.nextDirs[bruh[2]]
            else: # it's ls, so ignore for now
                pass
        elif bruh[0] == "dir":
            root.nextDirs[bruh[1]] = ListNode(root)
        else:
            root.filesSize += int(bruh[0])
            # for now the sizes are only the files for that specific directory
            # i'll update the whole directory later after i get the full folder structure
    except:
        break

def updateFinal(root):
    retVal = root.filesSize
    for i in root.nextDirs:
        retVal += updateFinal(root.nextDirs[i])
    root.finalSize = retVal
    return retVal

def dfs(root, score):
    if (root.finalSize <= 100000):
        score += root.finalSize

    for i in root.nextDirs:
        score = dfs(root.nextDirs[i], score)
    return score

updateFinal(initRoot)

score = 0
score = dfs(initRoot, score)
print(score)

totalSpace = 70000000
necessarySpace = 30000000

currentSpace = totalSpace - initRoot.finalSize
minDelete = currentSpace + initRoot.finalSize

def dfsDelete(root, minDelete):
    if (currentSpace + root.finalSize >= necessarySpace):
        minDelete = min(minDelete, root.finalSize)
    for i in root.nextDirs:
        minDelete = dfsDelete(root.nextDirs[i], minDelete)

    return minDelete

minDelete = dfsDelete(initRoot, minDelete)
print(minDelete)