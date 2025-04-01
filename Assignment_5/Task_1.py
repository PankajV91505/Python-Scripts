student ={
    "alice" : 85,
    "pankaj" : 68,
    "sachin" : 70,
    "aakash" : 80,
    "ramesh" : 90,
    "raj" : 85,
    "sanjay" : 95,
    "suresh" : 75,
    "sachin" : 80,
    
}

name = input("Enter the name of the student: ")
print("The marks of the student are: ", student.get(name, "Student not found"))