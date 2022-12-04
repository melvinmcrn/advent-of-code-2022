file = open("../data/q4", "r")


count = 0

for line in file.readlines():
    work1, work2 = line.strip().split(",")

    start1, stop1 = [int(e) for e in work1.strip().split("-")]
    start2, stop2 = [int(e) for e in work2.strip().split("-")]

    if (start1 >= start2 and stop1 <= stop2) or (start2 >= start1 and stop2 <= stop1):
        count += 1


print("Count:", count)

file.close()
