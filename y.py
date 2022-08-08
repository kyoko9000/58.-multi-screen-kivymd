list_1 = [1, 2]
list_2 = ["y", "u"]
list_3 = [2, 0]

list = []
for i in range(1, 4):
    list.append(eval("list_{}".format(i)))
print(list)
