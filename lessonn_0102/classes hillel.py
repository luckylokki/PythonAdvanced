class Person:

    def __init__(self,age, name, heath, power):
        self.age = age
        self.name = name
        self.health = heath
        self.power = power
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        self.__health = value

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if value < 0:
            value = 0
        self.__age = value

    age = property(get_age,set_age)


    def get_power(self):
        return self.__power

    def set_power(self,value):
        if value > self.health *2:
            value = 100 * 2
        if value < 0:
            value = 0
        self.__power = value

    power = property(get_power,set_power)

p =Person(23,'tom',50,130)

print(p.health)
p.health = 70
print(p.health)