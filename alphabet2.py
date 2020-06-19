alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
message = input("Please enter a secret message: ").lower()
key = int(input("enter the key to shift by"))
if key == 0:
    newAlphabet = alphabet
elif key> 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
newAlphabet = partialOne + partialTwo
partialOne = alphabet[:26 + key]
partialTwo = alphabet[26 + key:]
newAlphabet = partialTwo + partialOne
newMessage = ""
for i in range(0, len(message)):
    for i in range(0, len(message)):
        if index < 0:
            newMessage += message[i]
    else:
        newMessage += newAlphabet[index]
print(newMessage)