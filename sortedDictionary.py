my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sortedByKeysAsc = dict(sorted(my_dict.items()))
print(sortedByKeysAsc)
sortedByKeysDesc = dict(sorted(my_dict.items(), reverse=True))
print(sortedByKeysDesc)

