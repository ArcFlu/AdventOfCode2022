bruh = input()

currElf = 0
maxElf = 0

bruhArr = []

while bruh != "~":
    if bruh:
        currElf += int(bruh)
        maxElf = max(currElf, maxElf)
    else:
        bruhArr.append(currElf)
        currElf = 0
    
    bruh = input()

bruhArr.sort(reverse=True)
answer = bruhArr[0] + bruhArr[1] + bruhArr[2]
print(answer)