import os


tasks = []


def addTask():
    os.system('cls')
    taskEnd = False

    while taskEnd != True:
        userEntry = input("Add your task, or type end to quit: ").lower()
        if userEntry == "end":
            taskEnd = True
        else:
            tasks.append(userEntry)

    print("Ok, got it!")
    os.system('cls')
    initialMenu()


def modifyTask():
    os.system('cls')
    taskEnd = False

    for index in range(len(tasks)):
        print(f'{index + 1} - {tasks[index]}')

    while taskEnd != True:

        userItemEntry = input(
            "\nChoose the item for modify or type cancel: ").lower()
        if userItemEntry == "cancel":
            break
        userModifyEntry = input(
            "Type what you want to add: ").lower()
        tasks[int(userItemEntry) - 1] = userModifyEntry
        userEnd = input(
            "Do you want to modify another one? (Y or N): ").lower()

        if userEnd == "n":
            taskEnd = True
        else:
            modifyTask()

    print("Ok, got it!")
    os.system('cls')
    initialMenu()


def deleteTask():
    os.system('cls')
    taskEnd = False

    while taskEnd != True:
        userItemEntry = (
            input("Choose the item you want to delete or type cancel: ")).lower()
        if userItemEntry == "cancel":
            break
        del tasks[int(userItemEntry)]
        userEnd = input(
            "Do you want to delete another item? (Y or N): ").lower()

        if userEnd == "n":
            taskEnd = True
        else:
            deleteTask()
    print("Ok, got it!")
    os.system('cls')
    initialMenu()


def showTask():
    print("Here your tasks:\n")
    for index in range(len(tasks)):
        print(f'{index + 1} - {tasks[index]}')
    input("\nPress enter to return to main menu ")
    initialMenu()


def initialMenu():
    os.system('cls')
    print("Welcome to your today tasks. Here you can write down your daily activities and consult later!")

    print("Here what you can do: \n\n1 - Add a task \n2 - Modify a task \n3 - Delete a task \n4 - Show tasks \n5 - Exit")

    userChoose = int(input("Choose an option: "))

    if userChoose == 1:
        addTask()
    if userChoose == 2:
        modifyTask()
    if userChoose == 3:
        deleteTask()
    os.system('cls')
    if userChoose == 4:
        showTask()
    if userChoose == 5:
        os.system('cls')


initialMenu()
