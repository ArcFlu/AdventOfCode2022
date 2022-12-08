output = '''# AdventOfCode2022
 
Day 1-4 were done on December 4th.
First actual one done was Day 5.

Stats:

|Part|1|1|1|2|2|2|
|---|-----------|--------|-------|-----------|--------|-------|
'''
with open('README.md', 'w') as readme:
    with open('samplePaste.in') as f:
        for line in f:
            line = line.strip()
            arr = line.split(" ")
            while "" in arr:
                arr.remove("")
            
            output += "|"
            for i in arr:
                output += i + "|"
            output += "\n"
        readme.write(output)