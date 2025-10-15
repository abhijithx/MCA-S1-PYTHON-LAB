s1 = "hello"
s2 = "world"

list1 = list(s1)
list2 = list(s2)

list1[1], list2[1] = list2[1], list1[1]

result = ''.join(list1) + ''.join(list2)
print(result)

