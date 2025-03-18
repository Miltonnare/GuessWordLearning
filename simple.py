students={
    123:{
    "Name":"Evans Mulemba",
    "Age":26,
    "Gender":"Male",
    "County":"Machakos",
    "Status":"Single"
}
}
students_id={123}
def addStudents():

    details=int(input("Enter the Students ID:  "))
    if details in students_id:
        print("The Student ID Already exists!\n")
        return

    name=input("Enter Students Name: \n")
    age=int(input("Enter the Age: \n"))
    gender=input("Enter the Gender: \n")
    county=input("Which County are you from: \n")
    status=input("Your marital Status: \n")
    
    students[details]={
        "Name":name,
        "Age":age,
        "Gender":gender,
        "County":county,
        "Status":status
    }
    students_id.add(details)


    print("Students DETAILS ARE ADDED SUCCESFULLY : \n")

def retrieve():
    studentId=int(input("Enter ID to Search: "))
    if studentId in students_id:
        print("Student Details are: \n")
        for key, value in students[studentId].items():
            print(f"{key}: {value}")

    else:
        print(f"No Students found with the ID {studentId}")
    
def displayStudents():
    print("\n The Students Details Are: \n")
    for students_id , reveals in students.items():
        print(f"\n ID{students_id}")
        for key,value in reveals.items():
            print(f"{key}: {value}")

def main():
    while True:
        print("\n STUDENT MANAGEMENT SYSTEM \n")
        print("1. ADD STUDENTS")
        print("2. VIEW STUDENT")
        print("3. DISPLAY")
        print("4. EXIT")

        choice=int(input("\n Enter your Choice: \n"))
        if choice==1:
            addStudents()
        elif choice==2:
            retrieve()
        elif choice==3:
            displayStudents()
        elif choice==4:
            print("Thanks for the Attempts. Goodbye!")
            break
        else:
            print("Invalid Choice!Try Again")

main()
    




