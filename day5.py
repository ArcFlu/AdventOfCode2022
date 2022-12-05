# Day 5
# Starting at midnight, right when it opens

# part 1 15 minutes
# score = 0

# bruh = input()

# arr = []

# while bruh != "~":
#     splitList = bruh.split(" ")
#     arr.append(splitList)
#     bruh = input()

# bruh = input()

# while bruh != "~":
#     splitList = bruh.split(" ")
#     newSplitList = [int(splitList[1]), int(splitList[3]) - 1, int(splitList[5]) - 1] 
#     numBoxes = newSplitList[0]
#     startLoc = newSplitList[1]
#     endLoc = newSplitList[2]

#     for i in range(numBoxes):
#         arr[endLoc].append(arr[startLoc].pop())

#     bruh = input()

# str = ""
# for i in arr:
#     str += i[-1]

# print(str)

# ~~~~~~~~~~~~~~~~~~~
# 2 minutes for second part

score = 0

bruh = input()

arr = []

while bruh != "~":
    splitList = bruh.split(" ")
    arr.append(splitList)
    bruh = input()

bruh = input()

while bruh != "~":
    splitList = bruh.split(" ")
    newSplitList = [int(splitList[1]), int(splitList[3]) - 1, int(splitList[5]) - 1] 
    numBoxes = newSplitList[0]
    startLoc = newSplitList[1]
    endLoc = newSplitList[2]

    # just had to add this so i can keep the boxes in order

    temp = []
    for i in range(numBoxes):
        temp.append(arr[startLoc].pop())
    temp.reverse()
    for i in temp:
        arr[endLoc].append(i)

    bruh = input()

str = ""
for i in arr:
    str += i[-1]

print(str)