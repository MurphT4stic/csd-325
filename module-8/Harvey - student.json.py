import json

def print_students(students):
 
    for student in students: 
        print(f"{student['L_Name']}, {student['F_Name']}: ID={student['Student_ID']}, email={student['Email']}") 
def load_students(filename):
    with open(filename,'r')as file:
        return json.load(file) 

def main():
    students=load_students('student.json')
    print("Original list")
    print_students(students)

    my_data={
        "F_Name":"Tabari",
        "L_Name":"Harvey",
        "Student_ID":"57082",
        "Email":"tabari193@gmail.com"
    }
    students.append(my_data)
    print("Updated Student list")
    print_students(students)

    with open('student.json','w')as file:
        json.dump(students,file, indent=4)
    print("student.json has been updated.")
if __name__ == "__main__": 
    main()   