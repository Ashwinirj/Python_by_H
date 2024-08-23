# This will read the file and print it, once done will close the file without explicitly mentioning f.close()

with open("file.txt") as f:
    print(f.read())