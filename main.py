students = ["ahmad", "bobby"]

print("Hello! Welcome to simple student data management app 'StudentPedia'")
print(students)
selectMenu = int(input("Select number for access a feature \n1. '1' for input new student data\n2. '2' for update existing student data\n3. '3' for delete existing student data\n:"))

if selectMenu != 1 | selectMenu != 2 | selectMenu != 3:
    exit() # Stop a runned process

if selectMenu == 1:
    newStudent = input("Input a new student name: ")
    isExisting = students.count(newStudent.lower())
    if isExisting == 1: # If inputted is already on datastore
        print("Sorry, {0} is already on datastore".format(newStudent))
        exit()
    else:
        students.append(newStudent.lower())
        print("List a new students: {0}".format(students))
        exit()