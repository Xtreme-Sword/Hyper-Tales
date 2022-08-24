print("HYPER TALES\n")
H=input()
if H=="hehe":
    print("Horny mode is on, enjoy :)")
    Horny= "True"
start= str(input("Hello? Are You there? "))
if start == "yes" or "y" or "yass" or "yiss" or "yep" or "yup":
    print("Very well, then we shall start")
else:
    print("haha...silly one, I like that")
player= str(input("I will tell you a story.\n A story about an adventurer called (Insert your name):") or "Player")
world= str(input(player+"...Sounds...Special.\n But no story can be made out of just one being. This story is also about a world, one called...(insert World's name)") or "Earth")
print(world+"...What a beautiful place. One where fictions were true, where people can be whatever they wanted. Mages, cooks, librarians, warriors, even just normal people.\n They had peace, yet they had wars. had good lives, yet had misery. Sound a lot like Your own world, doesn't it", player+"?")
print("But let us not get sidetracked, shall we? This is the story of", player+". Of their adventures")
ch_class= str(input("They were a...(Select a class to be)\n >Mage\n >Librarian\n >Warrior\n >Cook\n >Musician\n >Cleaning Person\n >Citizen\n") or "Citizen")
if ch_class =="citizen":
        print("A",ch_class,"And lived like that their whole life, not really paying much attention to their surrounding problems\n ")
else:
        print("A",ch_class, "And had been so for several years\n ")
print("On an uneventful day, where not much was happening", player+" Decided to take on an adventure.\n They had heard about legends of a cave, one that spiraled those who dared enter it into madness.\n 'I can take it', They said, after packing up everything, and set off into their adventure")
print("After days of traveling, following maps, and hiking, they arrived. 'So it's true...' they sighed, relieved their hard work had payed off.", "'"+player, "the one who proved the legends true', they chanted, dreaming of what'd happen once they came back")
def RoomB1toJ1(txt1,txt2): #All Rooms in the Front(Bottom) of the dungeon, exactly to the left and right of the entrance, excluding the corners of the dungeon
    txt1="You go through the door"
    txt2="This room also has 3 doors, one Right, One Left and one North" 
    print(txt1)
    print(txt2)
def RoomB11toJ11(txt1,txt2): #Rooms in the top of the dungeon
    txt1="You go through the door"
    txt2="This room has three doors, one to the South one to the East and one to the Left"
def RoomK2toK10(txt1,txt2): #Rooms in the Rightmost side of the dungeon
    txt1="You go through the door"
    txt2="This room has three doors, one to the South one to the North and one to the Left"    
def RoomB2toB10(txt1,txt2): #Rooms in the Leftmost side of the dungeon
    txt1="You go through the door"
    txt2="This room has three doors, one to the North, one to the South and one to the Right"
def RoomBL(txt1,txt2): #Room in the Bottom Left corner
    txt1="You go through the door"
    txt2="This room has 2 doors, one to the North and one to the East"
def RoomTL(txt1,txt2): #Room in the Top Left corner
    txt1="You go through the door"
    txt2="This room has 2 doors, one to the South and one to the East"
def RoomTR(txt1,txt2): #Room in the Top Right corner
    txt1="You go through the door"
    txt2="This room has 2 doors, one to the South and one to the West"
def RoomBR(txt1,txt2): #Room in the Bottom Right Left corner
    txt1="You go through the door"
    txt2="This room has 2 doors, one to the North and one to the East"
def RoomEN(txt1,txt2): #Entrance Room to the dungeon
    txt1="You go in through the entrance, before you is a broad room"
    txt2="This room has 2 doors, one to the West and one to the East, along with a massive gate up front"
def FinalRoom(txt1,txt2,greetings): #The Final Room
    txt1="You go through the massive gate, It has stairs leading up into what looks like a throne room"
    txt2="There, sat upon a massive throne, was a creature.\n One You'd never laid eyes upon. One that combined the beauty of birds.\n the mightyness of scaled ones.\n and the fluffyness of the furred animals and citizens roaming in the outside world "
    greetings="Why hello fellow traveler. Alas, You've found me.\n I had hoped to stay hidden for longer, but it seems that won't go all that much further now, will it?"
    
    
    
    
    
    
    
    
    