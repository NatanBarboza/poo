from people import People
from student import Student
from worker import Worker

people = People("Natan", 19, 1.8, 70.5)
student = Student("João", 20, 1.75, 80)
worker = Worker("José", 35, 1.9, 90)

print(people.role)
print(student.role)
print(student.height)
print(worker.role)