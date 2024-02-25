while True:
    num_lollies = int(input("How many lollies? "))
    num_students = int(input("How many students? "))

    division = num_lollies / num_students
    per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    print("Division: ", division)
    print("Lollies pre student: ", per_student)
    print("Lollies left: ", lollies_left)
