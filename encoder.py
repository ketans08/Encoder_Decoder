# encoder
import string
import random

salt = int(input("Enter Salting Constant: "))
num = int(input("Enter Iterative constantP: "))
a = input("ENTER STRING:")
l1 = []
l2 = []
while a != "":
    m = 0
    for i in range(len(a)):
        k = "".join(random.choices(string.ascii_lowercase, k=salt))
        if m == i:
            l1.append(k)
        n = a[i]
        c = ord(n)
        if n != " ":
            e = chr(c - num)
        else:
            l1.append(k)
            e = chr(c)
            m = i + 1
        l1.append(e)
        if i == len(a) - 1:
            l1.append(k)
    l2.append("".join(l1))
    l1.clear()
    a = input("\t\t\t")
for each in l2:
    print(each, end="\n")
