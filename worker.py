from people import People

class Worker(People):
    def __init__(self, name:str, age:int, height:float, weight:float):
        super().__init__(name, age, height, weight)
        self.__role = "Worker"

    @property
    def role(self):
        return self.__role