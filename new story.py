print("you spawn in a forest")
print("Do you go Left, Right, or forward")
a = input("Left Right or Forward")
print("you choose" + a)
if a == "Forward" or "3" or "forward" or "third":
    print("you don't look where your going and fall into a lake")
    print("But you only lose 80 out of 100 health")
    print("you see a cave nearby")
    print("1: You can get out of the water")
    print("2: go into the cave")
    print("3: Stay where you are")
b = input("What do you do")
if a == "Left":
    print("You walked left and found a odd tree with a rock's on the branches.")
    print("the rock hates you and dies and falls on your head")
    print("ʘ‿ʘ")
    exit()
if a == "Right" or "right" or "2":
    print("you walk right and walk into a tree, thats a lot of damage")
    print("oof")
    exit()
if b == "Go into Cave" or "Cave" or "2":
    print("you go into the cave and fall into an endless voic, you die")
    exit()
if b == "3" or "Stay where you Are" or "Stay" or "stay":
    print("are you dumb?")
    print("you die from hypothermia")
    exit()
if b == "Get out of water" or "Observe" or "Help" or "2":
    print("You get out of the water and don't die")
    print("you gain 10 iq points and 2 hp")
    print("you are currently at 22 hp")
    print("you see a house")
    print("you can do:")
    print("1: Go into the House")
    print("2: Burn down the house bc your a savage")
    print("3: Knock on the door")
c = input("What do you do?")
if c == "1":
    print("you go into the house and get shot, you die")
    exit()
if c == "2":
    print("You burn down all the items inside the house and someone shoots you and you die")
    exit()
if c == "3":
    print("the door opens and a man with a gun dies")
    print("you get a gun, food, and a bunch of plastic bags")
    print("what do you do?")
    print("you can do")
    print("1: Create a giant plastic bag with all the plastic bags")
    print("2: Eat")
    print("3:")
else:
    print("you win")