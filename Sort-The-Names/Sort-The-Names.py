list_of_names = ["kjibrish", "yjibrish", "fjibrish", "zjibrish", "ajibrish"]


for i in range(len(list_of_names)):
    for j in range(i, len(list_of_names)):
        if (list_of_names[i] > list_of_names[j]):
            list_of_names[i], list_of_names[j] = list_of_names[j], list_of_names[i]

print(list_of_names)
