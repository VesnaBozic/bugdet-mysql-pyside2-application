import json
class Student:
    def __init__(self, student_card_number,password,name,surname,email,grades=None):
        self.student_card_number = student_card_number
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
        if grades == None:
            self.grades = []
        else:
            self.grades = grades






