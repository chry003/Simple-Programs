a = [4, 10, 3, 2, 6]

largest = a[0]
sec_largest = a[0]

for i in range(len(a)):
    if (largest < a[i]):
        largest = a[i]
        largest_index = i

    if (largest != a[i] and sec_largest < a[i]):
        sec_largest = a[i]

diff = largest - sec_largest
print(a[:largest_index] + [sec_largest, diff] + a[largest_index+1:])
