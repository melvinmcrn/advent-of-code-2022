file = open("../data/q6", "r")


def is_all_unique(word):
    word_set = set([c for c in word])
    if len(word) != len(word_set):
        return False
    else:
        return True


data = file.readline().strip()

cache_data = ""

for i in range(len(data)):
    cache_data += data[i]

    if len(cache_data) < 14:
        continue

    if is_all_unique(cache_data[-14:]):
        break


print("result:", len(cache_data))

file.close()
