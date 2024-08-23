word = "Donkey"

with open("file.txt") as f:
    data = f.read()
    # print(data)
    
    new_data = data.replace(word,"#####")
    print(new_data)

with open("file.txt", "w") as f:
    f.write(new_data)
    

    