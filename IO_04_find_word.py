# with open("log.txt") as f:
    # data = f.read()
    # if "Python" in data:
    #     print( "Found")
    # else:
    #     print("not found")
    

with open("log.txt") as f:
    lines = f.readlines()
    lineno = 1
    # for line in lines:
    for line in lines:
        if 'Python' in line:
            print(f"found python at {lineno}")
            break
        lineno += 1

    else: 
        print(f"Not found")
    # line += 1

