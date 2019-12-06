# Items that exist in each room and the functions you can use to interact with them

#TODO Define items in each room
room0items = ['leaflet']
room1items = ['fish']
room2items = []
room3items = []
room4items = []
room5items = []
room6items = []
room7items = ['lantern']
room8items = []
room9items = []
room10items = []
room11items = ['longsword']

allItems = [room0items, room1items, room2items, room3items, room4items,room5items,room6items,room7items,room8items,room9items,room10items,room11items]

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the coom
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum]:
        allItems[roomNum].remove(itemName)
        return itemName
    else:
        print("Not a valid item to pick up")
        return -1

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    print("You put down the ", itemName)
    # TODO Add item to room item list
    allItems[roomNum].append(itemName) 
    return 0

def useItem(itemName,itemList):
    if itemName in itemList:
        print("You used the ", itemName)
        return True
    else:
        print('You do no have that item in inventory ')
        return False
def printroom():
    print(room0items)
