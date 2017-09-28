list1 = ["aaa", "bbb", "ccc"]
list2 = [1, 2, 3, 4, 5, 6]

print(list1[1])
print(list2[1:3])

list1[1] = "ddd"
print(list1[1])

del list1[1]
print(list1)

print(len(list1))

print(list1 + list2)

print("aaa" in list1)
print(10 in list2)

for x in list2:
    print(x)

list1.append("zzz")
print(list1)

list1.reverse()
print(list1)
