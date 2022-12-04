file = open("../data/q1", "r")

current = 0
max = 0

for c in file.readlines():
    text = c.strip()

    if not text:
        if current > max:
            max = current
        current = 0
    else:
        current += int(text)

print("MAX:", max)

file.close()
