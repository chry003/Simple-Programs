n = 5 # int(input("Enter a number: "))


print("A.")
for i in range(n + 1):
    for j in range(i):
        print("*", end=" ")
    print("*")
