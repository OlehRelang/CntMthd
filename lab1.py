from tkinter import *
import math


def relative_error(x, X):
    return abs(x - X)/X


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def first_task(n, x1, n1, n2, x2):
    dfx1 = relative_error(x1, n**(1/2))
    dfx2 = relative_error(x2, n1/n2)
    result = (f" Рівність √{n} = {x1} більш точніша." if dfx1 < dfx2 else f"{n1}/{n2} = {x2} більш точніша.")
    res.config(text="Відповідь: " + result)


def short(x, dx):
    power = int(math.log10(dx)) - 1
    ddx = 5 * 10 ** power
    if ddx > dx:
        power += 1
    else:
        ddx *= 10
        power += 2

    n_round = round(x, -power)
    while dx + abs(n_round - x) > ddx:
        power += 1
        ddx *= 10
        n_round = round(n_round, -power)
    return n_round


def lng(x, dx):
    absx = x * dx * 0.01
    power = int(math.log10(absx))
    ddx = 10 ** power
    n_round = round(x, -power)
    while absx + abs(x - n_round) > ddx:
        power += 1
        ddx *= 10
        n_round = round(n_round, -power)

    return n_round


def second_task(num1, dx1, num2, dx2):
    result1 = str(short(num1, dx1))
    result2 = str(lng(num2, dx2))
    res2_1.config(text="a) Відповідь: " + result1)
    res2_2.config(text="б) Відповідь: " + result2)


def third_a(x):
    power = -1 * (len(str(x)[str(x).find('.'):]) - 1)
    dx = 5 * 10 ** (power - 1)
    ddx = dx / x
    ctr = int(math.log10(ddx)) - 2
    ddx = round_up(ddx, -ctr)
    pddx = ddx * 100
    result = f"{ddx:8f}" + "(" + str(pddx) + "%)"
    return f"{dx:4f}", result


def third_b(x):
    power = -1 * (len(str(x)[str(x).find('.'):]) - 1)
    dx = 10 ** power
    ddx = dx / x
    ctr = int(math.log10(ddx)) - 2
    res1 = round_up(ddx, -ctr)
    res2 = res1 * 100
    result = f"{res1:8f}" + "(" + str(res2) + "%)"
    return str(dx), result


def third_task(x1, x2):
    rs1 = third_a(x1)
    rs2 = third_b(x2)
    res3_1.config(text="a) Відповідь: " + "Δx = " + rs1[0] + " δx = " + str(rs1[1]))
    res3_2.config(text="б) Відповідь: " + "Δx = " + rs2[0] + " δx = " + str(rs2[1]))


root = Tk()
root.title("Чисельні методи, Лаб№1")

# Завдання 1
frame1 = LabelFrame(root, text="Завдання 1. Визначити яка рівність точніша.", padx=50, pady=50)
botomframe1 = Frame(frame1)
frame1.pack(padx=10, pady=10)
botomframe1.pack(side=BOTTOM)

Label(frame1, text="Sqrt(").pack(side='left', pady=15)
n = Entry(frame1, width=3)
n.pack(side='left', pady=15)
Label(frame1, text=")  =  ").pack(side='left', pady=15)
x1 = Entry(frame1, width=6)
x1.pack(side='left', pady=15)
n1 = Entry(frame1, width=3)
n1.pack(side='left', padx=(60, 0), pady=15)
Label(frame1, text="/").pack(side='left', pady=15)
n2 = Entry(frame1, width=3)
n2.pack(side='left', pady=15)
Label(frame1, text=" = ").pack(side='left', pady=15)
x2 = Entry(frame1, width=6)
x2.pack(side='left', pady=15)

res = Label(botomframe1, text="Відповідь: ")
res.pack()
Button(botomframe1, text="Обрахувати", command=lambda: first_task(float(n.get()), float(x1.get()), float(n1.get()),
                                                                  float(n2.get()), float(x2.get()))
       ).pack(pady=(10, 0))

# Завдання 2
frame2 = LabelFrame(root, text="Завдання 2. Округлити сумнівні цифри числа, залишивши вірні знаки.", padx=50, pady=50)
botomframe2 = Frame(frame2)
frame2.pack(padx=10, pady=10)
botomframe2.pack(side=BOTTOM)

Label(frame2, text="a) x = ").pack(side="left", pady=15)
num2_1 = Entry(frame2, width=6)
num2_1.pack(side="left", pady=15)
Label(frame2, text="Δx = ").pack(side="left", pady=15)
dx2_1 = Entry(frame2, width=10)
dx2_1.pack(side="left", pady=15)
Label(frame2, text="б) x = ").pack(side="left", padx=(60, 0), pady=15)
num2_2 = Entry(frame2, width=10)
num2_2.pack(side="left", pady=15)
Label(frame2, text="δx = ").pack(side="left", pady=15)
dx2_2 = Entry(frame2, width=8)
dx2_2.pack(side="left", pady=15)
Label(frame2, text="%").pack(side="left", pady=15)

res2_1 = Label(botomframe2, text="a) Відповідь: ")
res2_1.pack(pady=5)
res2_2 = Label(botomframe2, text="б) Відповідь: ")
res2_2.pack(pady=5)
Button(botomframe2, text="Обрахувати", command=lambda: second_task(float(num2_1.get()), float(dx2_1.get()),
                                                                   float(num2_2.get()), float(dx2_2.get()))
       ).pack(pady=(10, 0))


# Завдання 3
frame3 = LabelFrame(root, text="Завдання 3. Знайти граничні абсолютні та відносні похибки чисел,\n "
                               "якщо вони мають лише вірні цифри", padx=50, pady=50)
botomframe3 = Frame(frame3)
frame3.pack(padx=10, pady=10)
botomframe3.pack(side=BOTTOM)

Label(frame3, text="a) x = ").pack(side="left", pady=15)
num3_1 = Entry(frame3, width=10)
num3_1.pack(side="left", pady=15)
Label(frame3, text="б) x = ").pack(side="left", padx=(60, 0), pady=15)
num3_2 = Entry(frame3, width=10)
num3_2.pack(side="left", pady=15)

res3_1 = Label(botomframe3, text="a) Відповідь: ")
res3_1.pack(pady=5)
res3_2 = Label(botomframe3, text="б) Відповідь: ")
res3_2.pack(pady=5)
Button(botomframe3, text="Обрахувати", command=lambda: third_task(float(num3_1.get()), float(num3_2.get()))
       ).pack(pady=(10, 0))

Button(root, text="Вихід", command=root.quit).pack(side=BOTTOM, pady=20)

root.mainloop()
