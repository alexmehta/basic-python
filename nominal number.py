y = int(input("enter a number"))
x = y
n = 0
while n != 0:
    n = (10 * n) + (n % 10)
    x = x // 10
if n == y:
    "Number is nominal"
else:
    "No"

