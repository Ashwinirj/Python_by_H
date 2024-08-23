words = ["Donkey", "donkey", "bad", "gande"]

with open("file.txt") as f:
    data = f.read()
    # print(data)
    
for word in words:
    data = data.replace(word,"#####")

with open("file.txt", "w") as f:
    f.write(data)

    