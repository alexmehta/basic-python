alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
def decode(message):
    for key in range(len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
        for i in range(len(message)):
            index = alphabet.find(message[i])
            if index < 0:
                attempt += message[i]
            else:
                attempt += newAlphabet[index]
    print("Key: " + str(key) + " - " + attempt)
decode(message)