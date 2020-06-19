import random
import string
def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Your authentication code is",)
print(randomString(6))
input("would you like to begin the program?")

r = randomString(6)

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

y = IPAddr

w = ["120.37.208.89", "112.111.189.4", "91.207.116.175", "91.200.13.43", "91.232.96.36", "220.250.52.66", "91.207.7.141", "91.218.114.206"]


print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)

username = input("Enter a username:")
password = input("enter a password")

x = username
y = IPAddr
z = hostname

print("welcome to user authentication")
class accounts:
    def __init__(self, username, password):
        self.username = username
        self.password = password
username = input("enter a username")
if username == x:
    print("correct username")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
else:
    print("Incorrect")
    exit()
    password = input("password")
if IPAddr == y:
    print("IP scanned")
if IPAddr == w:
    print("service has been denied")
input("enter a password")
if password == password:
    print("need verification code, a code has been sent to your email and will be needed to enter your account/")

else:
    print("wrong password")
    exit()
g = input("Code")

if g == randomString(6) or r:
    print("you have logged in")
else:
    print("incorrect code")
    print("try again in 30 seconds")
    exit()
print("Thanks for using the program")
import time
time.sleep(15)
print("User will be logged out in 30 seconds")
import time
time.sleep(30)
exit()
#end of code

