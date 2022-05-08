class People:
    def __init__(self, name:str, age:int, height:float, weight:float):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__walk = False
        self.__eat = False
        self.__role = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def walk(self):
        return self.__walk

    def walk(self):
        if(self.__walk == False):
            self.__walk = True
            return print(f"{self.__name} is walking.")
        else:
            return print(f"{self.__name} is already walking.")

    def stop_walk(self):
        if(self.__walk == True):
            self.__walk = False
            return print(f"{self.__name} is stopping to walk.")
        else:
            return print(f"{self.__name} is already stopped.")

    @property
    def eat(self):
        return self.__eat

    def eat(self):
        if(self.__eat == False):
            self.__eat = True
            return print(f"{self.__name} is eating.")
        else:
            return print(f"{self.__name} is already eating.")

    def stop_eat(self):
        if(self.__eat == True):
            self.__eat = False
            return print(f"{self.__name} is stopping to eat.")
        else:
            return print(f"{self.__name} isn't eating.")

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        self.__role = new_role