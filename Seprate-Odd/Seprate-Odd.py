list_of_values = [10, 20, 30, "test", 30.5, 20.2, 10.1]

list_of_ints = []
list_of_strs = []
list_of_floats = []

for i in list_of_values:
    if (type(i) == int):
        list_of_ints.append(i)

    if (type(i) == str):
        list_of_strs.append(i)

    if (type(i) == float):
        list_of_floats.append(i)

print(list_of_ints, list_of_strs, list_of_floats)
