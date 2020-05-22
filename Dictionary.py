# mySkills = {
#     "html": "50%",
#     "css": "55%",
#     "jS": "10%",
#     "java": "50%",
#     'python': '50%'
# }
# print(mySkills['css'])
# print(mySkills.get('html'))
#
# for skill in mySkills:
#     print('{} and the value is {}'.format(skill, mySkills[skill]))
# ----------------------- list-----------------------------
# peoples = ['Ammar', 'Lubna', 'Lamis']
# skills = ['html', 'css', 'js']
# for name in peoples:
#     print(name)
#     for skill in skills:
#         print('-', skill)
# ---------------------------------------------------------

import tkinter

def parablola(x):
    y = x * x / 100
    return y

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x in range(-400, 400):
    y = parablola(x)
    plot(canvas, x, -y/4)

mainWindow.mainloop()