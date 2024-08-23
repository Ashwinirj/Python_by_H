# readlines() will return the list of lines in the file and of type list

# f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# readline() will print each line in the file and returns line as str type 
f = open("file.txt")
# line1 = f.readline()
# print(line1, type(line1))

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()