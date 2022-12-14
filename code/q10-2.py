file = open("../data/q10", "r")

cycle = 0
pause = False
col = 0
row = 0
sprite = 1


while True:

    cycle += 1

    if row > 5 and col > 39:
        break

    if col >= (sprite - 1) and col <= (sprite + 1):
        print("#", end="")

    else:
        print(".", end="")

    col += 1

    if col > 39:
        row += 1
        col = 0
        print()

    if pause:
        sprite += amount
        pause = False
        continue

    line = file.readline()

    if not line.strip():
        break

    data = line.strip().split()

    if data[0] == "noop":
        continue
    elif data[0] == "addx":
        amount = int(data[1])
        pause = True


file.close()
