file = open("../data/q3", "r")


def getCharacterScore(cha):
    if ord(cha) >= ord("a"):
        return ord(cha) - ord("a") + 1
    else:
        return ord(cha) - ord("A") + 1 + 26


score = 0

for line in file.readlines():
    data = line.strip()

    item1, item2 = data[: len(data) // 2], data[len(data) // 2 :]

    for c in item1:
        if c in item2:
            score += getCharacterScore(c)
            break


print("Score:", score)

file.close()
