#initialisling dictionary
student_grades = {  }

#Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    #[sajida] =100
    print(f"Added {name} with a {grade}")
    #Added sajida with a 100

#update astudent
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        # sajida = 200
        print(f"{name} with marks are updated {grade}")
        #sajida with marks are updated 200
    else:
         print(f"{name} is not found!") 

#delete a student
def delete_student(name):
    if name in student_grades:
          del student_grades[name]
          print(f"(name)has beensucessfully deleted")

    else:
          print(f"{name} is not found!")

#view all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
                print(f"{name} : {grade}")

    else:
           print("No students found/added")
# veiw all students
def main():
    while True:
        print('\n Students Grades Ganagment System')
        print("1. Add student")    
        print("2. Update student")             
        print("3. Delete student")             
        print("4. View student")             
        print("5. Exit ")    

        choice = int(input("Enter your choice = "))  
        if  choice == 1:
             name =  input("Enter your name = ")  
             grade = int(input("Enter your grade = ")) 
             add_student(name,grade)  

        elif choice == 2:
            name =  input("Enter your name = ")  
            grade = int(input("Enter your grade = ")) 
            update_student(name,grade)  

        elif choice == 3:
            name = input("Enter your name")    
            delete_student()   

        elif choice == 4:
            display_all_students()  

        elif choice == 5:
            print("Closing the program..") 
            break       

        else:
            print("invalid choice")





          
          