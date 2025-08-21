from pydantic import BaseModel

class Student(BaseModel):
    name : 'nitish'

new_student = {name: 'sau'}

student= Student(**new_student)
print(student) 