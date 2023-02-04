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
elif selectMenu == 2:
    student = input("Input a student name which is you want update it: ")
    isExisting = students.count(student.lower())
    if isExisting == 1: # If inputted data is available on datastore
        idx = student.index(student) # Get index number in datastore 
        newStudentName = input("Input a new student name for update it: ")
        students[idx] = newStudentName.lower()
        print("List a new students data after updated: {0}".format(students))
        exit()
    else:
        print("Sorry, {0} is not found from datastore".format(student))
        exit()
elif selectMenu == 3:
    student = input("Input a student name which is you want to delete it: ")
    isExisting = students.count(student.lower())
    if isExisting == 1: # If inputted data is available on datastore
        idx = students.index(student) # Get index number in datastore
        students.pop(idx)
        print("List a new students data after updated: {0}".format(students))
        exit()
    else:
        print("Sorry, {0} is not found from datastore".format(student))
        exit()