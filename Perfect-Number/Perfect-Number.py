n = int(input("Enter a number: "))

list_of_factors = []
for i in range(1, n + 1):
    if (n % i == 0):
        list_of_factors.append(i)

if ((sum(list_of_factors) - n) == n):
    print("It's a perfect number.")
else:
    print("It's not a perfect number.")
