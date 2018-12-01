file = open("input.txt")
total = 0
for line in file:
    total += int(line)
print(total)
