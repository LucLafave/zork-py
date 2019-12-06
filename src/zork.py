import items


# Field 0
def Field(second,itemList):

    if second.lower() == ("take mailbox"):
        print("---------------------------------------------------------")
        print("It is securely anchored.")
        return [True,0]
    elif second.lower() == ("open mailbox"):
        print("---------------------------------------------------------")
        print("Opening the small mailbox reveals a leaflet.")
        return [True,0]
    elif second[0:4].lower() == ("take"):
        return [True,0,items.pick_up(second[5:],0)]
    elif second.lower() == ("go north"):
        return [True,1]
    elif second.lower() == ("open door"):
        print("---------------------------------------------------------")
        print("The door cannot be opened.")
        return [True,0]
    elif second.lower() == ("take boards"):
        print("---------------------------------------------------------")
        print("The boards are securely fastened.")
        return [True,0]
    elif second.lower() == ("look at house"):
        print("---------------------------------------------------------")
        print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        return [True,0]
    elif second.lower() == ("go east"):
        print("---------------------------------------------------------")
        print("You walk around to the back of the house")
        return [True,6]
    elif second.lower() == ("go southwest"):
        return [True,2]
    elif second.lower() == ("read leaflet"):
        if items.useItem('leaflet', itemList):
            print("---------------------------------------------------------")
            print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
            return [True,0]
        else:
            return [True,0]
    elif second.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif second[0:8].lower() == ("put down"):
        if second[9:].lower() in itemList:
            items.put_down(second[9:],0)
            return[True,0]
        else:
            return[True,0]
    else:
        print("---------------------------------------------------------")
        return [True,0]
    

# North of House 1
def NorthofHouse(north_house_inp, itemList):
    
    if north_house_inp.lower() == ("go south"):
        return [True,0]
    elif north_house_inp.lower() == ("go north"):
        return [True,11]
    elif north_house_inp.lower() == ("swim"):
        print("---------------------------------------------------------")
        print("You don't have a change of clothes and you aren't here on vacation.")
        return [True,1]
    elif north_house_inp.lower() == ("fish"):
        print("---------------------------------------------------------")
        print("You spend some time fishing.")
        print("You gain a fish.")
        return [True,1,items.pick_up("fish",1)]
    elif north_house_inp[0:4].lower() == ("take"):
        return [True,1,items.pick_up(north_house_inp[5:],1)]
    elif north_house_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif second[0:8].lower() == ("put down"):
        if second[9:].lower() in itemList:
            items.put_down(second[9:],1)
            return[True,1]
        else:
            return[True,1]
    else:
        print("---------------------------------------------------------")
        return [True,1]

# Southwest Loop 2
def SouthwestLoop(forest_inp, itemsList):
    
    if forest_inp.lower() == ("go west"):
        print("---------------------------------------------------------")
        print("You would need a machete to go further west.")
        return [True,2]
    elif forest_inp.lower() == ("go north"):
        print("---------------------------------------------------------")
        print("The forest becomes impenetrable to the North.")
        return [True,2]
    elif forest_inp.lower() == ("go south"):
        print("---------------------------------------------------------")
        print("Storm-tossed trees block your way.")
        return [True,2]
    elif forest_inp.lower() == ("go east"):
        return [True,3]
    elif forest_inp[0:4].lower() == ("take"):
        return [True,2,items.pick_up(forest_inp[5:],2)]
    elif forest_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif forest_inp[0:8].lower() == ("put down"):
        if forest_inp[9:].lower() in itemList:
            items.put_down(forest_inp[9:],2)
            return[True,2]
        else:
            return[True,2]
    else:
        print("---------------------------------------------------------")
        return [True,2]
	

# East Loop and Grating Input 3
def EastLoop(grating_inp, itemList):

    if grating_inp.lower() == ("go south"):
        if items.useItem('longsword', itemList):
            print("---------------------------------------------------------")
            print("You killed the ogre")
            print("You are entering the cave he was guarding")
            return [True,5]
        else:
            print("You see a large ogre and turn around.")
            return [True,3]   
    elif grating_inp.lower() == ("descend grating"):
        return [True,4]
    elif grating_inp[0:4].lower() == ("take"):
        return [True,3,items.pick_up(grating_inp[5:],3)]
    elif grating_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif grating_inp[0:8].lower() == ("put down"):
        if grating_inp[9:].lower() in itemList:
            items.put_down(grating_inp[9:],3)
            return[True,3]
        else:
            return[True,3]
    else:
        print("---------------------------------------------------------")
        return [True,3]
    
# Grating Loop and Cave Input 4
def GratingLoop(cave_inp, itemList):

    if cave_inp.lower() == ("descend staircase"):
        return [True,5]
    elif cave_inp.lower() == ("take skeleton"):
        print("---------------------------------------------------------")
        print("Why would you do that? Are you some sort of sicko?")
        return [True,4]
    elif cave_inp.lower() == ("smash skeleton"):
        print("---------------------------------------------------------")
        print("Sick person. Have some respect mate.")
        return [True,4]
    elif cave_inp.lower() == ("light up room"):
        if items.useItem("lantern", itemList):
            print("---------------------------------------------------------")
            print("You light up the room and see runes on the walls.")
            print("They are unintelligible")
            return [True,4]
        else:
            print("---------------------------------------------------------")
            print("You would need a torch or lamp to do that.")
            return [True,4]
    elif cave_inp.lower() == ("break skeleton"):
        print("---------------------------------------------------------")
        print("I have two questions: Why and With What?")
        return [True,4]
    elif cave_inp.lower() == ("go down staircase"):
        return [True,5]
    elif cave_inp.lower() == ("go south"):
        return [True,9]
    elif cave_inp.lower() == ("scale staircase"):
        return [True,5]
    elif cave_inp[0:4].lower() == ("take"):
        return [True,4,items.pick_up(cave_inp[5:],4)]
    elif cave_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif cave_inp[0:8].lower() == ("put down"):
        if cave_inp[9:].lower() in itemList:
            items.put_down(cave_inp[9:],4)
            return[True,4]
        else:
            return[True,4]
    else:
        print("---------------------------------------------------------")
        return [True,4]

#Back of house 6    
def BackOfHouse(back_inp, itemList):
    if back_inp.lower() == ("go south"):
        return [True,0]
    elif back_inp.lower() == ("go west"):
        print("---------------------------------------------------------")
        print("Opening a rickety window you climb into the house")
        return [True,7]
    elif back_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif back_inp[0:4].lower() == ("take"):
        return [True,6,items.pick_up(back_inp[5:],6)]
    elif back_inp[0:8].lower() == ("put down"):
        if back_inp[9:].lower() in itemList:
            items.put_down(back_inp[9:],6)
            return[True,6]
        else:
            return[True,6]
    else:
        print("---------------------------------------------------------")
        return [True,6]

#Kitchen 7
def KitchenRoom(kitchen_inp, itemList):
    if kitchen_inp.lower() == ("go up"):
        return [True,8]
    elif kitchen_inp.lower() == ("go east"):
        return [True,6]
    elif kitchen_inp[0:4].lower() == ("take"):
        return [True,7,items.pick_up(kitchen_inp[5:],7)]
    elif kitchen_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif kitchen_inp[0:8].lower() == ("put down"):
        if kitchen_inp[9:].lower() in itemList:
            items.put_down(kitchen_inp[9:],7)
            return[True,7]
        else:
            return[True,7]
    else:
        print("---------------------------------------------------------")
        return [True,7]

#Attic 8
def AtticRoom(attic_inp, itemList):
    if attic_inp.lower() == ("go down"):
        return [True,7]
    elif attic_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif attic_inp[0:4].lower() == ("take"):
        return [True,8,items.pick_up(attic_inp[5:],8)]
    elif attic_inp[0:8].lower() == ("put down"):
        if attic_inp[9:].lower() in itemList:
            items.put_down(attic_inp[9:],8)
            return[True,8]
        else:
            return[True,8]
    else:
        print("---------------------------------------------------------")
        return [True,8]

#Maxe Entrance 9  
def MazeEntranceRoom(maze_entrance_inp, itemList):
    if maze_entrance_inp.lower() == ("go south"):
        print("---------------------------------------------------------")
        print("You head deeper into the maze.")
        return [True, 10]
    if maze_entrance_inp.lower() == ("go north"):
        return [True,4]
    elif maze_entrance_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif maze_entrance_inp[0:4].lower() == ("take"):
        return [True,9,items.pick_up(maze_entrance_inp[5:],9)]
    elif maze_entrance_inp[0:8].lower() == ("put down"):
        if maze_entrance_inp[9:].lower() in itemList:
            items.put_down(maze_entrance_inp[9:],9)
            return[True,9]
        else:
            return[True,9]
    else:
        print("---------------------------------------------------------")
        return [True,9]
    
def MazeInteriorRoom(maze_interior_inp, itemList):
    if maze_interior_inp.lower() == ("go north"):
        return [True, 9]
    else:
        if items.useItem("lantern",itemList):
            print("---------------------------------------------------------")
            print("You see the grue and flee before you are killed")
            return [True, 9]
        else:
            print("---------------------------------------------------------")
            print("You die.")
            print("---------------------------------------------------------")
            return [False,0]
    
def ArmoryRoom(armory_inp, itemList):
    if armory_inp.lower() == ("go south"):
        return [True,1]
    elif armory_inp.lower() == ("take longsword"):
        print("---------------------------------------------------------")
        print("You take the longsword")
        return [True,11,items.pick_up('longsword',11)]
    elif armory_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif armory_inp[0:4].lower() == ("take"):
        return [True,11,items.pick_up(armory_inp[5:],11)]
    elif armory_inp[0:8].lower() == ("put down"):
        if armory_inp[9:].lower() in itemList:
            items.put_down(armory_inp[9:],11)
            return[True,11]
        else:
            return[True,11]
    else:
        print("---------------------------------------------------------")
        return [True,11]
    
                              
# End of game 5
def EndOfGame(last_inp,itemList):
    
    if last_inp.lower() == ("open trunk"):
        print("---------------------------------------------------------")
        print("You have found the Jade Statue and have completed your quest!")
        # Exit loop at the end of game
        exit_inp = input("Do you want to continue? Y/N ")
        if exit_inp.lower() == ("n"):
            return [False,5]
        else:
            return [True,0]
    elif last_inp.lower() == ("kick the bucket"):
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        return [False,0]
    elif last_inp[0:4].lower() == ("take"):
        return [True,5,items.pick_up(last_inp[5:],5)]
    elif last_inp[0:8].lower() == ("put down"):
        if last_inp[9:].lower() in itemList:
            items.put_down(last_inp[9:],5)
            return[True,5]
        else:
            return[True,5]
    else:
        print("---------------------------------------------------------")
        return [True,4]	
    
