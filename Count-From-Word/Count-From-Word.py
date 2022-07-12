word = "MISSISSIPPI"
dict = {}

for i in word:
    # dict[i] = 1 if not i in dict.keys() else (dict[i] + 1)
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)
