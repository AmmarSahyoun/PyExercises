a = {1, 2, 3, 4}
b = {1, 2}

print("a is super set to b?", a.issuperset(b))
print("b is subset from a?", b.issubset(a))
print("\n#Dictionary")

user = {
    "name": "Ammar",
    "age": 44,
    "country": "Sweden",
    1: ["test", "html"],
    "name": "Deres",
    }
print(user)  # give new value to the same key
print(user['name'])
print("\ntwo- dimensional dictionary")
language ={
    "one":{
        "name":"html",
        "progress":"60%"
    },
    "two":{
        "name":"css",
        "progress":"50%"
    },
    "three":{
        "name":"Js",
        "progress":"30%"
    }
}
print(language['two']['progress'])
print(len(language['two'])) # length of dict
frameworkOne = {
    "name":"VuesJs",
    "progress":"50%"
    }
frameworkTwo = {
    "name":"Angular",
    "progress":"5%"
}
allFrameworks = {
    1:frameworkOne,
    2:frameworkTwo,
    }
print(allFrameworks)
print("=" * 50)

member = {
    "name": "Ammar"
          }
print(member)
member['age'] = 44
print(member)
member.update({"country": "Sweden"})
print("\n", member)
print(member.setdefault("name"))
print(member)
