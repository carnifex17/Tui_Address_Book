import sys, os, time, pickle, json
class AddressBook:
    book = {}
    def Banner():
        os.system('clear')
        print("""             _     _                     ____              _
    /\      | |   | |                   |  _ \            | |
   /  \   __| | __| |_ __ ___  ___ ___  | |_) | ___   ___ | | __
  / /\ \ / _` |/ _` | '__/ _ \/ __/ __| |  _ < / _ \ / _ \| |/ /
 / ____ \ (_| | (_| | | |  __/\__ \__ \ | |_) | (_) | (_) |   <
/_/    \\_\\__,_|\\__,_|_|  \\___||___/___/ |____/ \\___/ \\___/|_|\\_\\
Made by carnifex17""")
    def Add():
        name=input("Write a person, info of which you want to add: ")
        numb=input("Write down a number of {0}: ".format(name))
        AddressBook.book[name] = numb
    def Delete():
        name=input("Write a person, which you want to delete: ")
        if name in AddressBook.book:
            if input("Are you sure want to delete {0} Y/N: ".format(name)) == "Y":
                del AddressBook.book[name]
                i = 0
                while i < 3:
                    print(".", flush = True, end =" ")
                    i += 1
                    time.sleep(1)
                print("\nDeleting succesful")
            else:
                print("As you wish")
        else:
            print("Sorry, but this person didn\'t exist in out address book")
    def Change():
        name=input("Write a person, info of which you want to change: ")
        if name in AddressBook.book:
            newnumb=input("Write the number to which you want to change the current one: ")
            i = 0
            while i < 3:
                print(".", flush = True, end =" ")
                i += 1
                time.sleep(1)
            print("\nChanging succesful")
        else:
            print("Sorry, but this person didn\'t exist in out address book")
    def Show():
        for name, address in AddressBook.book.items():
            print('Name: {0} | Address: {1}'.format(name, address))
            print("_" * len('Name: {0} | Address: {1}'.format(name, address)))
    def Save():
        savename=input("How do you want to name this address book?:")
        with open('{0}.txt'.format(savename), 'w') as f:
            f.write(json.dumps(AddressBook.book))
        i = 0
        while i < 3:
            print(".", flush = True, end =" ")
            i += 1
            time.sleep(1)
        print("\nSaving succesful")
    def Load():
        savename=input("What address book do you want to load:")
        with open("{0}.txt".format(savename), "rb") as file:
            data = file.read()
            dict = json.loads(data)
            AddressBook.book=dict
            i = 0
            while i < 3:
                print(".", flush = True, end =" ")
                i += 1
                time.sleep(1)
            print("\nLoading succesful")
    def Commands():
        print("""With this tool you could manage address book just with this fancy TUI
Available commands for now is:
Commands
Clear
Add
Delete
Change
Save
Load
Show
""")
AddressBook.Banner()
while True:
    arg=input("> > > ")
    if(arg=="Add" or arg=="add"):#Done
        AddressBook.Add()
    elif(arg=="Delete" or arg=="delete"):#Done
        AddressBook.Delete()
    elif(arg=="Change" or arg=="change"):#Done
        AddressBook.Change()
    elif(arg=="Exit" or arg=="exit"):#Done
        exit()
    elif(arg=="Clear" or arg=="clear"):#Done
        AddressBook.Banner()
    elif(arg=="Save" or arg=="save"):#Done
        AddressBook.Save()
    elif(arg=="Load" or arg =="load"):#Done
        AddressBook.Load()
    elif(arg=="Show" or arg=="show"):#Done
        AddressBook.Show()
    elif(arg=="Commands" or arg=="commands"):
        AddressBook.Commands()
    else:
        print("To watch all possible commands just type \'Commands\'")
#P.S. This is my first full program/project and i think to add two features in next versions like:
#Checking for available address books and to delete address books, not just delete elements in it
#And VERY big thanks to my comrade Mykola (https://github.com/ProgrammerFox/)
