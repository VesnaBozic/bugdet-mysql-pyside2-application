from Professor import Professor
from Student import Student
from Subjects import Subject
import csv
import json

subjects_csv = open("data/subjects.csv", "r", encoding="utf-8")
next(csv.reader(subjects_csv, delimiter=','))
subjects = [] 
for row in csv.reader(subjects_csv, delimiter=','):
    if row != []:
        code = int(row[0])
        name = row[1]
        subject = Subject(code,name)
        subjects.append(subject)

def register():
    print("*************************REGISTRATION*********************") #registration menu
    print("Please, choose who do you want to register: ")
    print("----------------------------------------------------------")
    print("1. Professor")
    print("2. Student")
    print("3. Return to Main Menu")
    print("----------------------------------------------------------")

    while True: #we are using while loop in case if entry is wrong to be able to choose again and it will repeat until we choose one of 3 options
        try:
            select = int(input("Choose 1 , 2 or 3: "))
            if select == 1: #registration for new teachers 

                professors_csv = open("data/professors.csv",
                                     "r", encoding="utf-8")

                teachers = [] 
                for row in csv.reader(professors_csv, delimiter=';'):
                    if row != []:
                        teachers.append({
                            "code": row[0],
                            "password": row[1],
                            "name": row[2],
                            "surname": row[3],
                            "email": row[4],
                            "consultation": row[5]

                        })
                


                print("-------------------------------------------------------------")
                code = int(input("Please, enter your code: "))
                exists = False
                for t in teachers: #after new teacher input code we are checking does entered code exist in teachers list
                    if int(t["code"]) == code: #if exist, we ask him to try new code
                        print("-------------------------------------------------------------")
                        print("Code already exists. Try again.") 
                        exists = True
                        break
                if not exists: #if code doesn't exist we procced with entering other data
                    print("-------------------------------------------------------------")
                    password = input("Please, enter your password: ")
                    name = input("Please, enter your name: ")
                    surname = input("Please, enter your surname: ")
                    email = input("Please enter your email: ")
                    consultation = input(
                        "Please, enter your consultation time: ")
                    fields = [code, password, name,surname, email, consultation] #list with new teacher data

                    with open(r'data/professors.csv', 'a', newline='', encoding="utf-8") as f: #we are writing new teacher data into csv professors file
                        writer = csv.writer(f, delimiter=";")
                        writer.writerow(fields)
                        return

            elif select == 2: #registration for new students
                students = json.loads(open('data/students.json', encoding="UTF-8").read()) #we are reading direct from json students file
                print("-------------------------------------------------------------")
                student_card = int(input("Please, enter your student card number: "))
                exists = False
                for s in students: #checking if student card number already exists
                    if s["student_card_number"] == student_card: 
                        print("-------------------------------------------------------------")
                        print("Card number already exists. Try again.")
                        exists = True
                        break
                if not exists: #if doesn't exist ask for student data
                    print("-------------------------------------------------------------")
                    student_password = input("Please, enter your password: ")
                    student_name = input("Please, enter your name: ")
                    student_surname = input("Please, enter your surname: ")
                    student_email = input("Please, enter your email: ")
                    student = {
                        "student_card_number": student_card,
                        "password": student_password,
                        "name": student_name,
                        "surname": student_surname,
                        "email": student_email,
                        "grades": []
                    }
                    students = [] #creating students list
                    with open(r'data/students.json', 'r', newline='', encoding="utf-8") as f:
                        students = json.load(f) #this returns json object
                    students.append(student) #we append new student in students object
                    with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f: 
                        json.dump(students, f) #and we are dumping students file as a string in json file
                        return
            elif select == 3:
                return    
                    
            else:
                print("-------------------------------------------------------------")
                print("Wrong entry. Please, try again.")

        except ValueError:
            print("-------------------------------------------------------------")
            print("Wrong entry. Please try again.")
    register()


def print_data(professor):
    print("Name: " + professor.name)
    print("Surname: " + professor.surname)
    print("Email: "+ professor.email)
    print("Consulattion: "+ professor.consultation)



def add_grade(professor): #function with argument, parametar will be  teacher who is logged 

    print("-------------------------------------------------------------")
    
    student_name = input("Please, enter student name: ") #we are asking from professor to input student name
    print("-------------------------------------------------------------")
    with open("data/students.json") as json_file:
        students=json.load(json_file)
    students_array = []
    for s in students:
        student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
        students_array.append(student)
    exist = False
    counter=0
    for i in range(len(students_array)): #with for loop going through all students
        if student_name.lower() in students_array[i].name.lower(): # if entered just one letter we list all students with that letter in name
            counter +=1
            print(str(counter)+".", students_array[i].student_card_number,
                students_array[i].name, students_array[i].surname)
            exist = True
    if not exist:
        print("-------------------------------------------------------------")
        print("Students with this name does not exist.")
        return
    try:
        print("-------------------------------------------------------------")
        
        index_number = int(input("Please, enter student card number: ")) 
        print("-------------------------------------------------------------")
        for student in students_array:
            if student.student_card_number == index_number:
                counter = 0
                print("Here is the list of all subjects: ")
                print("")
                for subject in subjects: #we are printing all subjects
                    counter += 1
                    print(str(counter)+".", subject.code, subject.name)
                print("-------------------------------------------------------------")
                sub_code = int(input("Please, enter subject code: "))
                condition = True
                for s in subjects:
                    if int(s.code)==sub_code:
                        print("-------------------------------------------------------------")
                        grade = int(input("Please, enter student's grade: "))
                        if grade < 5 or grade > 10: #setting that professor can only enter valid grade
                            print("-------------------------------------------------------------")
                            print("Wrong entry!")
                        else:
                            for s in students_array:
                                if s.student_card_number == index_number: #appeding subject code that teacher entered, logged teacher's code and grade
                                    s.grades.append(
                                        {"subject_code": sub_code, "professor_code": int(professor.code), "grade": grade})
                            with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f:
                                json.dump(students_array, f)
                            print("-------------------------------------------------------------")
                            print("You added grade.")
                        condition = False
                if condition:            
                    for s in subjects:
                        if s.code != sub_code:
                            print("-------------------------------------------------------------")
                            print("That subject code doesn't exist.")
                            break
            

                    

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")



def delete_grade(professor):
    with open("data/students.json") as json_file:
        students=json.load(json_file)
    students_array = []
    for s in students:
        student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
        students_array.append(student)
    print("-------------------------------------------------------------")
    student_name = input("Please, enter student name: ")
    exist = False
    print("-------------------------------------------------------------")
    counter=0
    for i in range(len(students_array)):
        if student_name.lower() in students_array[i].name.lower(): #with lower() it doesn't matter if capital or small letter is entered
            counter+=1
            print(str(counter)+".", students_array[i].student_card_number,students_array[i].name, students_array[i].surname)
            exist = True
    if not exist:
        print("-------------------------------------------------------------") 
        print("This students do not exist.")
        return
    try:
        print("-------------------------------------------------------------")
        index_number = int(input("Please, enter student card number: "))
        print("-------------------------------------------------------------")
        for student in students_array:
            if student.student_card_number == index_number:
                counter = 0
                grades_indices = [] #here we will store indices of grades so that we can find right index of grade that professor want to delete
                original_index = -1 #we are setting it on -1, because we need to go from index 0 
                for g in student.grades:
                    original_index+=1
                    if g["professor_code"]==int(professor.code):
                        counter+=1
                        print("-------------------------------------------------------------")
                        print(str(counter)+".", g["subject_code"], g["grade"])
                        grades_indices.append(original_index) #here we are appending original indices of professors subjects in the list 
                        
                if len(grades_indices)>0:
                    try:
                        print("-------------------------------------------------------------")
                        number = int(input("Please enter number of grade: "))
                        if number < 1 and number > len(student.grades):
                            print("-------------------------------------------------------------")
                            print("Wrong entry. Please, try again.")
                        else:
                            student.grades.pop(grades_indices[number-1]) # pop() in-built function that removes item, we are using original index that we stored in list
                            with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f:
                                json.dump(students_array, f)
                            print("-------------------------------------------------------------")
                            print("You deleted grade.")
                            
                    except ValueError:
                        print("-------------------------------------------------------------")
                        print("Wrong entry. Please, try again.")
                else:
                    print("-------------------------------------------------------------")
                    print("This student doesn't have your grade.")
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")



def average_grade(professor):
    counter = 0
    print("-------------------------------------------------------------")
    print("Here is the list of all the subjects.")
    for subject in subjects:
        counter += 1
        print(str(counter)+".", subject.code, subject.name)
    try:
        number = int(input("Please, enter number of subject: "))
        if number < 1 or number > len(subjects):
            print("-------------------------------------------------------------")
            print("Wrong entry. Please, try again.")
        else:
            grades = []
            with open("data/students.json") as json_file:students=json.load(json_file)
            students_array = []
            for s in students:
                student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
                students_array.append(student)
            for s in students_array:
                for g in s["grades"]:
                    if g["subject_code"] == int(subjects[number-1].code) and g["professor_code"] == int(professor.code):
                        grades.append(g["grade"])
            print("-------------------------------------------------------------")
            print("Average grade of your subject is: " + "{:.2f}".format(sum(grades)/len(grades)))
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")
    except ZeroDivisionError:
        print("-------------------------------------------------------------")
        print("None of the students has your grade or you entered wrong subject code.")


def change_consultation_date(professor):
    professors = []
    with open("data/professors.csv", "r", encoding="utf-8") as f:
        for line in f:
            
            line= line.split(";")
            code = int(line[0])
            password = line[1]
            name= line[2]
            surname = line[3]
            email = line[4]
            consultation = line[5]
            professor = Professor(code,password,name,surname,email,consultation) 
            

            professors.append(professor)
            

    print("-------------------------------------------------------------")
    print("Your current time of consultation is: " + professor.consultation)
    print("-------------------------------------------------------------")
    new_consultation = input("Enter new consultation time: ")
    print("-------------------------------------------------------------")
    
    if new_consultation.strip() != "": #strip method removes spaces, so if professor just hit enter we don't change nothing
        professor.consultation = new_consultation  # memory of computer
        for prof in professors:
            if prof.code == professor.code:
                prof.consultation = new_consultation+"\n"  # memory of file
            else:
                prof.code = prof.code
        
    with open(r'data/professors.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
    for p in professors: 
        fields = str(p.code) +";" + p.password+";"+ p.name+";"+p.surname+";"+p.email+";"+p.consultation
        print(fields)
        with open("data/professors.csv", 'a+') as f:
            f.write(fields)
                
    print("You succesfully changed your consultation date.")


def prof(professor):
    print("-------------------------------------------------------------")
    print("Please, choose what you want to do: ")
    print("-------------------------------------------------------------")
    print("1. Add Student grade.")
    print("2. Delete Student grade.")
    print("3. Calculating the average grade for a subject.")
    print("4. Change of consultation date.")
    print("5. Return to Main Menu.")
    print("-------------------------------------------------------------")

    try:  # with try and except we are avoiding breaking of program if wrong value is entered
        print("-------------------------------------------------------------")
        option = int(input("Choose your option: "))
        print("-------------------------------------------------------------")
        if option == 1:
            add_grade(professor)
            prof(professor)

        elif option == 2:
            delete_grade(professor)
            prof(professor)

        elif option == 3:
            average_grade(professor)
            prof(professor)

        elif option == 4:
            change_consultation_date(professor)
            prof(professor)

        elif option == 5:
            return

        else:
            print("-------------------------------------------------------------")
            print("Wrong enter! Please, try again!")
            prof(professor)

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong enter! Please, try again!")
        prof(professor)


def calculate_av_grade(student): #function with parameter, on call of te function we pass logged student as argument

    grades = []
    for g in student.grades: #going through logged student grades
        grades.append(g["grade"]) #and appending them in grades list
    if(len(grades)>0):
        print("-------------------------------------------------------------")
        print("Your average grade is: " + "{:.2f}".format(sum(grades)/len(grades))) #we sum grades and divide with lenght of grades and format a result
    else:
        print("-------------------------------------------------------------")
        print("You don't have any grades yet.")



def exams(student):
    print("-------------------------------------------------------------")
    print("1. Passed exams")
    print("2. Failed exams")
    print("-------------------------------------------------------------")
    passed_exams = []
    for g in student.grades: #here we append passed exams in list so that later we can use it to know which are failed exams if the first option is 2
        if g["grade"] > 5:
            for s in subjects:
                if s.code == g["subject_code"]:
                    passed_exams.append(s)
    try:
        print("-------------------------------------------------------------")
        exam = int(input("Choose, your option: "))
        if exam == 1:
            print("-------------------------------")
            print("You have passed next exams: ")
            print("-------------------------------")
            for g in student.grades:
                if g["grade"] > 5:
                    for s in subjects:
                        if s.code == g["subject_code"]:
                            print(s.code, s.name)
                            passed_exams.append(s)
            if passed_exams == []:
                print("-------------------------------------------------------------")
                print("You haven't passed any exam.")
        elif exam == 2:
            print("-------------------------------")
            print("You haven't passed next exams: ")
            print("")
            for s in subjects:
                passed=False
                for p in passed_exams:
                    if s.code==p["code"]:
                        passed=True
                if not passed:
                    print(s.code, s.name)
        else:
            print("-------------------------------------------------------------")
            print("Wrong entry.")
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry.")


def professor_data(student):
    professors =[]
    with open("data/professors.csv", "r", encoding="utf-8") as f:
        for line in f:
            
            line= line.split(";")
            code = int(line[0])
            password = line[1]
            name= line[2]
            surname = line[3]
            email = line[4]
            consultation = line[5]
            professor = Professor(code,password,name,surname,email,consultation) 
            professors.append(professor)
                
    students = json.loads(open('data/students.json', encoding="UTF-8").read())
    students_array = []
    for s in students:
        student = Student(s["student_card_name"],s["password"],s["name"],s["surname"], s["email"],s["grades"])
        students_array.append(student)
    counter = 0 
    print("-------------------------------------------------------------")
    print("Here is list of your exams: ")
    for subject in subjects: #printing subjects codes and names
        counter +=1
        print(str(counter)+".", subject.code, subject.name) 
    print("-------------------------------------------------------------")
    sub_code = int(input("Please, enter subject code: "))
    print("-------------------------------------------------------------")
    for s in students_array: #checking are such code in students grades
        for g in s.grades:
            if g["subject_code"]==sub_code:
                for p in professors: # does the subject code match with teacher code if does print code and his name
                    if int(p.code)==g["professor_code"]:
                        print("")
                        print("-------------------------------------------------------")
                        print("Professor code is: " + p.code)
                        print("Professor's name is: " + p.name +" " + p.surname )
                        print("Email: " + p.email)
                        print("Consulation time is: " + p.consultation)
                        print("")
                        return
    print("-------------------------------------------------------------")
    print("Doesn't exist.")



def stud(student):
    print("----------------------------------------------")
    print("Please, choose what you want to do: ")
    print("1. Calculating the average grade.")
    print("2. Passed exams or non-passed exams display by student's choice.")
    print("3. Professor's data display.")
    print("4. Return to Main Menu.")
    print("-------------------------------------------------------------")

    try:  # with try and except block we are catching and hendling execeptions, if string value  is entered
        option = int(input("Choose your option: "))
        if option == 1:
            print("---------------------------------------")
            calculate_av_grade(student)
            stud(student)

        elif option == 2:
            print("----------------------------------------")
            exams(student)
            stud(student)

        elif option == 3:
            professor_data(student)
            stud(student)

        elif option == 4:
            return

        else:
            print("-------------------------------------------------------------")
            print("Wrong enter! Please, try again!")
            stud(student)

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong enter! Please, try again!")
        stud(student)
