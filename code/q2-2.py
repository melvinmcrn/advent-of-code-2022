file = open("../data/q2", "r")

score = 0

winning_table = {"A": 2, "B": 3, "C": 1}
draw_table = {"A": 1, "B": 2, "C": 3}
lose_table = {"A": 3, "B": 1, "C": 2}

for line in file.readlines():
    data = line.strip().split()

    if data[1] == "X":
        score += lose_table[data[0]]
    elif data[1] == "Y":
        score += draw_table[data[0]]
        score += 3
    elif data[1] == "Z":
        score += winning_table[data[0]]
        score += 6


print("Score:", score)

file.close()
