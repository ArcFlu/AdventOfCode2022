# Compartments
# 11 minutes for part 1
# 8 minutes for part 2
# total: 19 min

score = 0

# pt 1
# with open('day3.in') as f:
#     for line in f:
#         line = line.rstrip()

#         halfPoint = len(line)//2
#         firstHalf = line[:halfPoint]
#         secondHalf = line[halfPoint:]

#         firstSet = set(firstHalf)


#         special = ""
#         for i in secondHalf:
#             if i in firstSet:
#                 special = i
#                 break
        
#         if i.isupper():
#             score += ord(i) - 64 + 26
#         else:
#             score += ord(i) - 96

# pt 2 - 8 minutes
arr = []
with open('day3.in') as f:
    for line in f:
        line = line.rstrip()
        arr.append(line)

special = ""

for i in range(0, len(arr), 3):
    firstSet = set(arr[i])
    secondSet = set()

    for j in arr[i + 1]:
        if j in firstSet:
            secondSet.add(j)
    
    for j in arr[i + 2]:
        if j in secondSet:
            special = j
            break
    

    # intersect = firstSet.intersection(set(arr[i + 1]), set(arr[i + 2]))
    # print(intersect.pop())
    # print(special)
    # special = intersect.pop()

    if special.isupper():
        score += ord(special) - 64 + 26
    else:
        score += ord(special) - 96

print(score)