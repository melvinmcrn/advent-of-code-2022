file = open("../data/q1", "r")

current = 0
data = []

for c in file.readlines():
    text = c.strip()

    if not text:
        data.append(current)
        current = 0
    else:
        current += int(text)

print("TOTAL TOP 3:", sum(sorted(data, reverse=True)[:3]))

file.close()
