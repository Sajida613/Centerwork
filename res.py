#student result program

#get student information

name = input("Enter student name: ")
roll_number = int(input("Enter roll number:"))
#get marks of eacth subjucts
math = int(input("Enter the marks: "))
eng = int(input("Enter the marks: "))
urdu = int(input("Enter the marks: "))
science = int(input("Enter the marks: "))
sindhi = int(input("Enter the marks: "))

#culcalate total marks and percentage

total_marks = math+eng+urdu+science+sindhi
percentage = (total_marks / 500)*100

#determine grade

if percentage >= 80:
  grade = "A"
elif percentage >= 70:
  grade = "B"
elif percentage >= 60:
  grade = "C"
elif percentage >= 50:
  grade = "D"
else: 
  grade = "F"

  #DISPLAY RESULT
print("Student Name:,name")
print("Roll Number:,roll_number")
print("English marks:,eng")
print("Urdu marks:,urdu")
print("Sindhi marks:,sindhi")
print("Science marks:,science")
print("math marks:,math")
print("Total marks:,total_marks")
print("Percentage:,percentage") 
print("Grade:,grade")  
  

  # IF CHECK STUDENT PASS OR FAIL
if percentage >= 40:
  print("Result : Pass")
else:
  print("Result : Fail")
    


  

  
