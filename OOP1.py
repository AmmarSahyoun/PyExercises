class Member:
    not_Allowed_names = ["fuck", "shit"]
    usersNumber = 0

    @classmethod
    def showCounts(cls):
        print(f"we have{ cls.usersNumber} Users in our system")

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        Member.usersNumber += 1

    def getFullName(self):
        if self.name in Member.not_Allowed_names:
            raise ValueError("------Name NOT allowed!------")
        else:
            return f"{self.name}{self.family}"

    def nameTitle(self):
        if self.age < 28:
            return f"Hello Mr {self.getFullName()}"
        elif self.age < 50:
            return f" MOUALllleM {self.getFullName()}"
        else:
            return f"{self.getFullName}"

    def getAllInfo(self):
        return f"{self.nameTitle()},your age is: {self.age}"


print(Member.usersNumber)
customer1 = Member('Patrik', ' Sax', 20)
customer2 = Member('Ammaroo', ' El Hoob', 45)
customer3 = Member("Anna", "Solok", 27)
customer6 = Member('shit', ' fuck', 25)

print('+++++++++++++++++\n')
print(customer1.getAllInfo())
print(customer2.getAllInfo())
print(customer3.getAllInfo() + '\n')
# print(Member.usersNumber)
# print(dir(Member))
Member.showCounts()

print('-----------------')
class Skill:

    def __init__(self):
        self.skills = ["HTML", "CSS", "Js"]

    def __str__(self):
        return f"my skills are:{self.skills}"

    def __len__(self):
        return len(self.skills)

profile = Skill()
print(profile)
print(profile.__class__)
print(len(profile))
#print(dir(str))
profile.skills.append("Java")
profile.skills.append("MySQL")
print(profile)