# Main game file

import zork


itemList = []
roomnum = 0
alive = True
list_status = []


def PrintOutput(s):
    print("OUTPUT", s)
def Removeitem(itemList,item):
    itemList.remove(item)
    return itemList

while alive:
    if roomnum == 0:
        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        field_input = input("What do you do? ")

        list_status = zork.Field(field_input,itemList)
        if field_input[0:8].lower() == ("put down"):
            if field_input[9:].lower() in itemList:
                itemList = Removeitem(itemList,field_input[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
            print(itemList)
        else:
            alive = list_status[0]
            roomnum = list_status[1]
            print(itemList)
        continue
    
    if roomnum == 1:
        print("---------------------------------------------------------")
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("You can see a white house in the distance to the south and something shining in the north.")
        north_house_inp = input("What do you do? ")
         
        list_status = zork.NorthofHouse(north_house_inp,itemList)
        if north_house_inp[0:8].lower() == ("put down"):
            if north_house_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,north_house_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue

    if roomnum == 2:
        print("---------------------------------------------------------")
        print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        forest_inp = input("What do you do? ")

        list_status = zork.SouthwestLoop(forest_inp,itemList)
        if forest_inp[0:8].lower() == ("put down"):
            if forest_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,forest_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue

    if roomnum == 3:
        print("---------------------------------------------------------")
        print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print("There is an open grating, descending into darkness.")
        grating_inp = input("What do you do? ")

        list_status = zork.EastLoop(grating_inp,itemList)
        if grating_inp[0:8].lower() == ("put down"):
            if grating_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,grating_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 4:
        print("---------------------------------------------------------")
        print("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print("There also seems to be a small path leading south.")
        print("There is a skeleton of a human male in one corner.")
        cave_inp = input("What do you do? ")

        list_status = zork.GratingLoop(cave_inp,itemList)
        if cave_inp[0:8].lower() == ("put down"):
            if cave_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,cave_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 5:
        print("---------------------------------------------------------")
        print("You have entered a mud-floored room.")
        print("Lying half buried in the mud is an old trunk, bulging with jewels.")
        last_inp = input("What do you do? ")

        list_status = zork.EndOfGame(last_inp,itemList)
        if last_inp[0:8].lower() == ("put down"):
            if last_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,last_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 6:
        print("---------------------------------------------------------")
        print("You are behind the white house.")
        print("In the west corner of the house there is a small window which is slightly ajar.")
        back_inp = input("What do you do? ")

        list_status = zork.BackOfHouse(back_inp,itemList)
        if back_inp[0:8].lower() == ("put down"):
            if back_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,back_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 7:
        print("---------------------------------------------------------")
        print("You find yourself in a dimly lit kitchen with dust covering the floor.")
        print("A lantern rests on the kitchen island.")
        print("a set of stairs leads up to another room")
        kitchen_inp = input("What do you do? ")
        
        list_status = zork.KitchenRoom(kitchen_inp,itemList)
        if kitchen_inp[0:8].lower() == ("put down"):
            if kitchen_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,kitchen_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 8:
        print("---------------------------------------------------------")
        print("This is the attic it is very dark and small.")
        print("The only exit is the staircase leading down.")
        attic_inp = input("What do you do? ")

        list_status = zork.AtticRoom(attic_inp,itemList)
        if attic_inp[0:8].lower() == ("put down"):
            if attic_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,attic_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 9:
        print("---------------------------------------------------------")
        print("There is a giant door leading to what looks like many passages.")
        print("This seems to be the entrance to the maze.")
        print("Heading south will lead you in.")
        maze_entrance_inp = input("What do you do? ")

        list_status = zork.MazeEntranceRoom(maze_entrance_inp,itemList)
        if maze_entrance_inp[0:8].lower() == ("put down"):
            if maze_entrance_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,maze_entrance_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 10:
        print("---------------------------------------------------------")
        print("It is pitch black.")
        print("You hear noises in the dark")
        maze_interior_inp = input("What do you do? ")

        list_status = zork.MazeInteriorRoom(maze_interior_inp,itemList)
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
    if roomnum == 11:
        print("---------------------------------------------------------")
        print("This is the armory it is old and torn up with soot covering everything")
        print("It seems to be looted")
        print("There is a longsword in the corner it has rust but still seems sharp")
        armory_inp = input("What do you do? ")

        list_status = zork.ArmoryRoom(armory_inp,itemList)
        if armory_inp[0:8].lower() == ("put down"):
            if armory_inp[9:].lower() in itemList:
                itemList = Removeitem(itemList,armory_inp[9:].lower())
        if len(list_status) == 3:
            itemList.append(list_status[2])
            alive = list_status[0]
            roomnum = list_status[1]
        else:
            alive = list_status[0]
            roomnum = list_status[1]
        continue
    
        





