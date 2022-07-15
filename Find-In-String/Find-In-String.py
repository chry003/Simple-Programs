list_of_strings = ["no bun", "bug bun bug bun bug bug", "bunny bug", "buggy bug bug buggy"]
check = input("Enter a string: ")

dict_of_strings = {}

for i in range(len(list_of_strings)):
    counter = 0
    for j in range(len(list_of_strings[i].split())):
        if (list_of_strings[i].split()[j] == check):
            counter += 1

    dict_of_strings[i] = { counter: list_of_strings[i] }

for i in range(len(dict_of_strings)):
    for j in range(i, len(dict_of_strings)):
        _i = list(dict_of_strings[i].keys())[0]
        _j = list(dict_of_strings[j].keys())[0]

        if (_i < _j):
            dict_of_strings[i], dict_of_strings[j] = dict_of_strings[j], dict_of_strings[i]

list_of_strings = []
for i in range(len(dict_of_strings)):
    _i = list(dict_of_strings[i].keys())[0]
    list_of_strings.append(dict_of_strings[i][_i])

print(list_of_strings)
