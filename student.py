from people import People

class Student(People):
    def __init__(self, name: str, age: int, height: float, weight: float):
        super().__init__(name, age, height, weight)
        self.__role = "Student"

    @property
    def role(self):
        return self.__role