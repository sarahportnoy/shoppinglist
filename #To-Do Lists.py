#To-Do Lists

#functions
Shoppinglist = []

#Adds items to shopping list
def add():
    x = input("What would you like to add?")
    Shoppinglist.append(x)
    print(Shoppinglist)

#Views items in shopping list
def View():
    print(Shoppinglist)

#Crosses out item on shopping list
def Mark():
    z = input("What would you like to mark?")
    y = Shoppinglist.index(z)
    Shoppinglist[y] = (z + " ✓")

#Removes items on shopping list
def Remove():
    a = input("What would you like to remove?")
    Shoppinglist.remove(a)

#Exits shopping list
def Exit():
    quit()

#remove all tasks from the to-do list
def clear():
    Shoppinglist.clear()
    print (Shoppinglist)

#sort the list alphabetically
def sort():
    Shoppinglist.sort()
    print (Shoppinglist)

#print the number of items on the to-do list
def items():
    print (len(Shoppinglist))

def Shop():
    print("1. Add Item \n2. View List \n3. Mark Item \n4. Remove Item \n5.Exit \n6. Clear List \n7. Sort List Alphabetically \n8. Print Number of Items on List")
    c = input("Choose Option:")
    if c == "5":
        quit()
    if c == "1":
        add()
    if c == "2":
        View()
    if c == "3":
        Mark()
    if c == "4":
        Remove()
    if c == "6":
        clear()
    if c == "7":
        sort()
    if c == "8":
        items()

#main
Shop()