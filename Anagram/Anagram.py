s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1_lst = []
for i in s1:
    s1_lst.append(i)

s2_lst = []
for i in s2:
    s2_lst.append(i)

for i in range(len(s1_lst) - 1, -1, -1):
    if (s1_lst[i] in s2_lst):
        idx = s2_lst.index(s1_lst[i])
        s1_lst.pop(i)
        s2_lst.pop(idx)
    else:
        print("They are not anagrams.")
        break

if (not len(s1_lst) and not len(s2_lst)):
    print("They are anagrams.")
