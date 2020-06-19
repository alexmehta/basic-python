n = int(input("enter a number"))
temp = n
cal = 0
while n > 0:
    dig = n % 10
    cal = cal + dig ** 3
    n = n//10
if cal == temp:
    print("Correct")
else:
    print("no")