from fastapi import FastAPI
from database import mycursor, cursor2
app = FastAPI()


@app.get("/student")
def read_root():
    mycursor.execute("SELECT * FROM students")
    res = []
    for i in mycursor.fetchall():
        res.append({
            'Roll Number': i[0],
            'Name': i[1]
        })

    return res


@app.get("/student/{roll}")
def getStudent(roll: int):
    mycursor.execute(f"SELECT * FROM students WHERE roll_number = {roll}")
    res = []
    for i in mycursor.fetchall():
        res.append({
            'Roll Number': i[0],
            'Name': i[1]
        })

    return res


@app.get("/marks")
def getMarks():
    mycursor.execute("SELECT * FROM marks")
    res = []
    for m in mycursor.fetchall():
        roll_number = m[0]
        cursor2.execute(f"SELECT name FROM students WHERE roll_number = {roll_number}")
        stu = cursor2.fetchall()[0]


        res.append({
            "Student name" : stu[0],
            'Physics': m[1],
            'Chemistry': m[2],
            "Maths" : m[3],
            "Biology" : m[4]
        })

    return 
    

@app.get("/marks/{roll_no}")
def getMarks(roll_no : int):
    mycursor.execute(f"SELECT * FROM marks WHERE roll_number = {roll_no}")
    res = []
    for m in mycursor.fetchall():
        roll_number = m[0]
        cursor2.execute(f"SELECT name FROM students WHERE roll_number = {roll_number}")
        stu = cursor2.fetchall()[0]


        res.append({
            "Student name" : stu[0],
            'Physics': m[1],
            'Chemistry': m[2],
            "Maths" : m[3],
            "Biology" : m[4]
        })

    return res


# to run :  uvicorn main:app --reload
