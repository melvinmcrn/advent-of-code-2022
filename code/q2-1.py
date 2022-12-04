file = open("../data/q2", "r")

score = 0

winning_table = {"X": "C", "Y": "A", "Z": "B"}
draw_table = {"X": "A", "Y": "B", "Z": "C"}

for line in file.readlines():
    data = line.strip().split()

    if data[1] == "X":
        score += 1
    elif data[1] == "Y":
        score += 2
    elif data[1] == "Z":
        score += 3

    if winning_table[data[1]] == data[0]:
        score += 6
    elif draw_table[data[1]] == data[0]:
        score += 3


print("Score:", score)

file.close()
