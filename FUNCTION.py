def remove_duplicates():
    t = ['a', 'b', 'c', 'd']
    t2 = ['a', 'c', 'd']
    for t in t2:
        t.append(t.remove())
    return t
list_of_numbers = [1,6,8,1,9,1,8,0]
list_of_strings = ["Blue feather", "Yellow feather", "Orange Feather", "Gray Feather"]
list_of_numbers.sort()
list_not = [0,1,2,3,4,5,6,7,8,9,10]
list_of_strings.sort()
print(list_of_strings)
print(list_of_numbers)
list_of_numbers.pop(1)
print(list_of_numbers)
list_of_strings.remove("Blue feather")
list_of_strings.append(list_not)
print(list_of_strings)
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list_of_strings)