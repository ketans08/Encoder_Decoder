salt = int(input("Enter Salting Constant: "))
num = int(input("Enter Iterative constantP: "))
word = input("ENTER STRING:")
l0 = []
while word != "":
    # part 1
    l1 = []
    l2 = []
    for i in range(len(word)):
        if word[i] != " ":
            l1.append(word[i])
        else:
            l2.append("".join(l1))
            l1.clear()
    l2.append("".join(l1))
    # part 2
    l3 = []
    l4 = []
    o = len(l2)
    for a in range(o):
        h1 = str(l2[a])
        h2 = len(h1)
        for i in range(h2):
            if i < salt:
                continue
            elif (i >= salt) and (i < h2 - salt):
                l3.append(h1[i])
            else:
                break
        l4.append("".join(l3))
        l3.clear()
    # part 3
    l5 = []
    l6 = []
    for a in range(len(l4)):
        m1 = str(l4[a])
        m2 = len(m1)
        for b in range(m2):
            a1 = ord(m1[b])
            a2 = chr(a1 + num)
            l5.append(a2)
        l6.append("".join(l5))
        l5.clear()
    l0.append(" ".join(l6))
    l6.clear()
    word = input("\t\t\t")
for each in l0:
    print(each, end="\n")
