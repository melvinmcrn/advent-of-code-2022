file = open("../data/q3", "r")


def getCharacterScore(cha):
    if ord(cha) >= ord("a"):
        return ord(cha) - ord("a") + 1
    else:
        return ord(cha) - ord("A") + 1 + 26


score = 0

while True:
    item1, item2, item3 = file.readline(), file.readline(), file.readline()

    if not item1 or not item2 or not item3:
        break

    for c in item1:
        if c in item2 and c in item3:
            score += getCharacterScore(c)
            break


print("Score:", score)

file.close()
