import random
import csv
import matplotlib.pyplot as plt

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def get_avg_grade(self):
        avg_grade = 0
        for grade in self.data_sheet.get_grades_as_list():
            avg_grade += int(grade)
        final_avg = avg_grade / len(self.data_sheet.get_grades_as_list())
        return final_avg

    def get_study_progression(self):
        ECTS = 0
        for course in self.data_sheet.courses:
            ECTS += course.ECTS
        progression = ECTS/150
        return progression

class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def __repr__(self):
        return '%r' % (self.courses)

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades




class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    def __repr__(self):
        return '%r, %r, %r, %r, %r' % (self.name, self.classroom, self.teacher, self.ETCS, self.grade)


def generate_student(number):
    course_list = ['GameDev', 'Python', 'Security']
    names = ['David', 'Anders', 'Mathilde', 'Alberte', 'John', 'Morten', 'Emma']
    genders = ['Male', 'Female']
    grades = [0, 2, 4, 7, 10, 12]
    ECTS = [10, 20, 30, 40, 50, 60]

    for x in range(0, number):
        with open('/home/jovyan/python_handin_template/week3.csv', 'a') as file_object:
            course = Course(random.choice(course_list), 'Class E', 'Thomas', random.choice(ECTS), random.choice(grades))
            course1 = Course(random.choice(course_list), 'Class E', 'Thomas', random.choice(ECTS), random.choice(grades))
            course2 = Course(random.choice(course_list), 'Class E', 'Thomas', random.choice(ECTS), random.choice(grades))
            data_sheet = DataSheet([course, course1, course2])
            name = random.choice(names)
            student = Student(name, random.choice(genders), data_sheet, 'image_url')
            print(student)

            write_to_csv = 'Stud_name: {name}, course_name: {course_name}, gender: {gender}, teacher: {teacher}, ETCS: {ETCS}, classroom: {classroom}, grade: {grade}, image_url: {image_url}'.format(
                name=student.name, course_name=data_sheet, gender=student.gender, teacher=course.teacher, ETCS=course.ETCS, classroom=course.classroom, grade=course.grade, image_url=student.image_url)

            file_object.write(write_to_csv + '\n')

#generate_student(6)

def read_student_data():
    student_list = []
    with open('/home/jovyan/python_handin_template/week3.csv', 'r') as file_object:
        lines = file_object.readlines()
        for line in lines:
            name = line.split('Stud_name: ')[1].split(', course_name')[0]
            course_name = line.split('course_name: ')[1].split(', teacher')[0]
            gender = line.split('gender: ')[1].split(', teacher')[0]
            teacher = line.split('teacher: ')[1].split(', ETCS')[0]
            ETCS = line.split('ETCS: ')[1].split(', classroom')[0]
            classroom = line.split('classroom: ')[1].split(', grade')[0]
            grade = line.split('grade: ')[1].split(', image_url')[0]
            image_url = line.split('image_url: ')[1]

            course = Course(course_name, classroom, teacher, ETCS, grade)
            data_sheet = DataSheet([course])
            student = Student(name, gender, data_sheet, image_url)
            student_list.append(student)

    return student_list

#read_student_data()

def print_student_list():
    student_list = read_student_data()
    for student in student_list:
        print('Name: ' + student.name + ', img_url: ' + student.image_url + ', avg_grade: ' + str(student.get_avg_grade()))
    
print_student_list()

def sort_by_avg_grade():
    student_list = read_student_data()
    student_list.sort(key=lambda kv: kv.get_avg_grade())
    print('Sorted by grade:')
    for student in student_list:
        print('Name: ' + student.name + ', img_url: ' + student.image_url + ', avg_grade: ' + str(student.get_avg_grade()))

#sort_by_avg_grade()

def student_bar_chart():
    student_list = read_student_data()
    for student in student_list:
        plt.bar([student.name], [student.get_avg_grade()],width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

def study_progression_chart():
    student_list = read_student_data()
    progression = 0
    students = 0
    for student in student_list:
        for course in student.data_sheet.courses:
            if course.name == 'GameDev':
                progression += student.get_study_progression()
                students += 1
            if course.name == 'Security':
                progression += student.get_study_progression()
                students += 1
            if course.name == 'Python':
                progression += student.get_study_progression()
                students += 1
    plt.bar([progression], [students], width=0.5, align='center')
    plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
