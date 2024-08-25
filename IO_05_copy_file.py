with open("log.txt") as f:
    content = f.read()

with open("new_log.txt", "w") as f:
    f.write(content)