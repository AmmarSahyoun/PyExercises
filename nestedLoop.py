# ---------------------Dictionary -----------------
# persons = {
#     "Ammar": {
#         "age": 45,
#         "gender": "male",
#         "live": "Sweden"},
#     "Lubna": {
#         "age": 40,
#         "gender": "female",
#         "live": "Sweden"},
#     "Rasha": {
#         "age": 38,
#         "gender": "Female",
#         "live": "Sweden"}
# }
# for name in persons:
#     print(name)
#     for attribute in persons[name]:
#         print("{} => {}".format(attribute, persons[name][attribute]))
#     print('-----------------')
# -------------------------------------------------------------
# mySkills = {
#     "Ammar": {
#         "html": "60%",
#         "css": "45%",
#         "js": "10%",
#         "java": "40"},
#     "MdAsfari": {
#         "html": "90%",
#         "css": "65%",
#         "js": "60%",
#         "java": "90"}
# }
# print(mySkills)
# print(mySkills.items())
# for key, value in mySkills.items():
#     print("{} => {}".format(key, value))
# print('-'*20)
#
# for key, value in mySkills.items():
#     print(key, "the progress is:")
#     for key2, value2 in value.items():
#         print("-{} => {}".format(key2, value2))

# -----------------packing   unpacking------------------------------------
# def greeting(*person):
#     for i in person:
#         print(f"Hello {i}")
#
# greeting("Lubna", "Ammar", "Lamis", "Rasha")
#
# def details(name, *par):
#     print(f"Hi {name} you have:")
#     for i in par:
#         print(i)
#
# details("Lubna", "kaj", "Deres")
# details("Ammar", "kaj", "Deres")
# ----------------------------------
mySkills = {
    "Ammar": {
        "html": "60%",
        "css": "45%",
        "js": "10%",
        "java": "40"},
    "MdAsfari": {
        "html": "90%",
        "css": "65%",
        "js": "60%",
        "java": "90"}
}
def conv(**par):
    for key, value in par.items():
        print(f"{key} => {value}")

conv(**mySkills)
