# Camp Cleanup
# 15 min for first attempt
# 2 min for first attempt fix
# 5 minutes for second part
# total: 22 minutes

# score = 0
# with open('day4.in') as f:
#     for line in f:
#         line = line.rstrip()

#         ranges = line.split(',')
#         firstRange = list(map(int, ranges[0].split('-')))
#         secondRange = list(map(int, ranges[1].split('-')))

#         firstStr = ""
#         for i in range(firstRange[0], firstRange[1] + 1):
#             firstStr += str(i)
        
#         secondStr = ""
#         for i in range(secondRange[0], secondRange[1] + 1):
#             secondStr += str(i)

#         # print(firstStr)
#         # print(secondStr)
#         # print()

#         if firstStr in secondStr or secondStr in firstStr:
#             score += 1


# pt 1 attempt 2
# took two minutes to refactor solution
# score = 0
# with open('day4.in') as f:
#     for line in f:
#         line = line.rstrip()

#         ranges = line.split(',')
#         firstRange = list(map(int, ranges[0].split('-')))
#         secondRange = list(map(int, ranges[1].split('-')))

#         f1 = firstRange[0]
#         f2 = firstRange[1]

#         s1 = secondRange[0]
#         s2 = secondRange[1]

#         if f1 >= s1 and f2 <= s2:
#             score += 1
#         elif s1 >= f1 and s2 <= f2:
#             score += 1

# Pt 2: if there is overlap at all
# 5 minutes
score = 0
with open('day4.in') as f:
    for line in f:
        line = line.rstrip()

        ranges = line.split(',')
        firstRange = list(map(int, ranges[0].split('-')))
        secondRange = list(map(int, ranges[1].split('-')))

        f1 = firstRange[0]
        f2 = firstRange[1]

        s1 = secondRange[0]
        s2 = secondRange[1]

        if f1 <= s2 and f1 >= s1 or s1 <= f2 and s1 >= f1:
            score += 1

print(score)