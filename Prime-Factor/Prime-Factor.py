n = int(intput("Enter a number: "))

list_of_factors = []
for i in range(1, n + 1):
    if (n % i == 0):
        list_of_factors.append(i)


for i in list_of_factors:
    counter = 0
    for j in range(1, i + 1):
        if (i % j == 0):
            counter = counter + 1

    if counter == 2:
        print(i, "is a prime factor of", n)
