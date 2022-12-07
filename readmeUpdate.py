with open('README.md', 'a') as readme:
    with open('samplePaste.in') as f:
        for line in f:
            line = line.strip()
            arr = line.split(" ")
            while "" in arr:
                arr.remove("")
            
            output = "|"
            for i in arr:
                output += i + "|"
            output += "\n"
            print(output)

            readme.write(output)