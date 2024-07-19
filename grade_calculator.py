
def assign_grade(score):
    if score >= '90':
        Grade='A'
    elif score >='80' and score<'90':
        Grade='B'
    elif score >='70' and score<'80':
        Grade='C'
    elif score >='60' and score< '70':
        Grade='D'
    elif score>='0' and score< '60':
        Grade='F'
    else:
        print("Invalid Score!")
        return None
    return Grade

def add_student(students):
    Student={"Name":"","Score":"","Grade":""}
    name=""
    while name=="":
        name=input("Enter Student Name:")
    Student["Name"]=name
    score=int(-1)
    while  isinstance(score,str) or int(score)<0 or int(score)>100:
        print(type(score))
        score=int(input("Enter Studnet's Score: "))
    Student["Score"]=score
    Student["Grade"]=assign_grade(Student["Score"])
    students.append(Student)

def display_students(students):
    for student in students:
        print(student["Name"],"has a score of",student["Score"], "and receives a grade of",student["Grade"])

def search_students(students):
    inp=input("Enter Student's Name: ").lower()
    for student in students:
        if student["Name"].lower() ==inp :
            print(student["Name"],"has a score of",student["Score"], "and receives a grade", student["Grade"])
            return True
    print("Not found!")
    return False
    

def main_menu():
    students=[]
    while True:
        print("Welcome to the Student Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Search for student")
        print("4. Exit\n")
        choice=input("Please enter your choice:")
        if choice=='1':
            add_student(students)
        elif choice=='2':
            display_students(students)
        elif choice=='3':
            search_students(students)
        else:
            break
            

#main_menu()
class CustomError(Exception):         
    def __init__(self, message):             
        self.message = message      
        try:         
            raise CustomError("This is a custom error.")     
        except CustomError as ce:         
            print(f"Custom error caught: {ce.message}")

x=CustomError("sfv")       


