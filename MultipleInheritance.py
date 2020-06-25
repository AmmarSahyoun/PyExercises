# class BaseOne:
#     def __init__(self):
#         print("Base One Constructor")
#
#     def function1(self):
#         print("Function One active")
#
#
# class BaseTow:
#     def __init__(self):
#         print("Base Two")
#
#     def function2(self):
#         print("Function Tow active")
#
# class Derived(BaseOne, BaseTow):
#     pass
#
# myVAr = Derived()
# # Mro : method resulotion order
# # print(Derived.mro())
# myVAr.function1()
# myVAr.function2()
# print('---------------------')
# class Base:
#     def __init__(self):
#         print("this is BASE class")
#
# class DerivedOne(Base):
#     pass
#
# class DerivedTow(DerivedOne):
#         pass
# amm = DerivedTow()
# print('--- PROTECTED & Private attribute, Encapsulation- Getter & Setter')
class Member:
    def __init__(self, name, age):
        self._name = name  # this attribute is protected'_'
        self.__age = age    # this attribute is private'__'
    def getInfo(self):
       return f"{self._name} has { self.__age} years old"
    def get_age(self):  # Getter
        return  self._name
    def get_age(self):
        return  self.__age
    def set_age(self, newAge):
        self.__age = newAge

one = Member("Ahmed", 39)
print(one._name)
name = "Ammar"  # did not chane the name cause its protected'_'
print(one._name)
print(one.getInfo())
print(one.get_age())
one.set_age(58)
print(one.getInfo())