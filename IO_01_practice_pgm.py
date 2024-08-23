with open("file.txt") as f:
    data = f.read()
    print(type(data))
    if "Twinkle" in data:
        print("Found")
    else: 
        print("Not Found")

