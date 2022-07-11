# class Bomzh:
#     def __init__(self,name):
#         self.health = 100
#         self.name = name
#
#     def buhich(self,bottle):
#         if self.health <= 0:
#             print('добухался')
#             return
#         self.health -= bottle
#
#     def workout(self,hour):
#         if self.health <= 0:
#             print('добухался')
#             return
#         self.health += hour
#
#
# petrovich = Bomzh(name='Petrovich')
# petrovich.buhich(bottle=100)
# petrovich.buhich(bottle=100)
#
# print(petrovich.health)

# class Stack:
#
#     def __init__(self):
#         self.lst = []
#
#     def add(self,element):
#         self.lst.append(element)
#
#     def get(self):
#         return self.lst.pop()
#
# item = Stack()
#
# item.add(5)
# item.add(4)
# item.add(3)
#
# print(item.get())
# print(item.get())
# print(item.get())

class Person:

    def __init__(self, name, heath):

        self.name = name
        self.health = heath
        self.counter_health = 0#сколько раз я смотрел здоровье
        # if heath >0 and heath <= 100:
        #     self.__health = heath
        #     print(self.__health)
        # else:
        #     raise Exception('error')

    def get_health(self):
        self.counter_health += 1
        return self.__health

    def set_health(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        self.__health = value

    halala = property(get_health, set_health)


p = Person('tm', 5000)
p.halala = 70
print(p.halala)
