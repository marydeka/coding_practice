filename = "random_text.txt"

with open(filename) as f:
    for line in f:
        print(line.rstrip())