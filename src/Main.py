#from Functions import *
import csv
import json
from Professor import Professor
from Student import Student



# def menu():
#     print("*******************************MAIN MENU*********************************")
#     print("Please, choose option: ")
#     print("-------------------------------------------------------------------------")
#     print("1. Log into the system")
#     print("2. Registration")
#     print("3. Leave the aplication")
#     print("-------------------------------------------------------------------------")


#     try: 
#         print("")
#         option = int(input("Choose your option: "))
#         if option == 1 :
#             log()
#             menu()
            
#         elif option == 2 :
#             register()
#             menu()
        
#         elif option == 3 :
#             print("-------------------------------------------------------------")
#             print("You left the aplication.")
#             exit() 
        
#         else:
#             print("-------------------------------------------------------------")
#             print("Wrong enter! Please, try again.")
#             menu()
    
#     except ValueError:
#         print("-------------------------------------------------------------")
#         print("Wrong enter. Please, try again.")
#         menu() 


# def log():

#     professors =[]
#     with open("data/professors.csv", "r", encoding="utf-8") as f:
#         for line in f:
            
#             line= line.split(";")
#             code = int(line[0])
#             password = line[1]
#             name= line[2]
#             surname = line[3]
#             email = line[4]
#             consultation = line[5]
#             professor = Professor(code,password,name,surname,email,consultation) 
#             professors.append(professor)

#     students = json.loads(open('data/students.json', encoding="UTF-8").read())
#     students_array = []
#     for s in students:
#         student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
#         students_array.append(student)
       
#     try:
#         print("-------------------------------------------------------------")
#         code = int(
#             input("Please, enter your professor code or student card number: "))
#         print("-------------------------------------------------------------")
#         password = input("Please, enter your password: ")
        
        
#         for i in range(len(students_array)):
#             if students_array[i].student_card_number == code and students_array[i].password == password:
#                 print("-------------------------------------------------------------")
#                 students_array[i].stud()
#                 return

#         for i in range(len(professors)):  
#             if professors[i].code == str(code) and professors[i].password == password:
#                 print("-------------------------------------------------------------")
#                 professors[i].prof()
#                 return

#         print("-------------------------------------------------------------")
#         print("Wrong password or code. Please, try again.")
#         print("-------------------------------------------------------------")
        

#     except ValueError:
#         print("-------------------------------------------------------------")
#         print("Wrong entry. Please try again.")
#         menu()
# menu()


professors =[]
with open("data/professors.csv", "r", encoding="utf-8") as f:
    for line in f:
        
        line= line.split(";")
        code = line[0]
        password = line[1]
        name= line[2]
        surname = line[3]
        email = line[4]
        consultation = line[5]
        professor = Professor(code,password,name,surname,email,consultation) 
        professors.append(professor)

# students = json.loads(open('data/students.json', encoding="UTF-8").read())
# students_array = []
# for s in students:
#     student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
#     students_array.append(student)

print(professors)
#print(students_array)








