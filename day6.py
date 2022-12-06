# Day 6.
# Hopefully it's an easy one
# It was pretty easy, but I just folded for some reason
# Didn't need to make another function lol, didn't even use it
# 10 minutes for the first part, 20 seconds for the second part
# First part was message of length 4, Second Part was length of 14

from collections import deque 

score = 0

def checkArray(arr):
    if (len(arr) < 4 and len(set(arr)) != len(arr)):
        return False
    else:
        return True

with open('day6.in') as f:
    for line in f:
        line = line.rstrip()
        q = deque([])

        counter = 0
        for i in line:
            q.append(i)
            if (len(q) == 14 and len(set(q)) == len(q)):
                counter += 1
                break
            else:
                if (len(q) >= 14):
                    q.popleft()
            counter += 1

        score = counter
    
print(score)