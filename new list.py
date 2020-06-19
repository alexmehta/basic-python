def listhelper(x):
 list = []
 for i in x:
    if i not in list:
      list.append(i)
 return list
x = [1, 2, 3, 3, 4, 4, 4, 4, 4, 4,4,4,4,4,4,4,4,4,4,4,4]
print(listhelper(x))