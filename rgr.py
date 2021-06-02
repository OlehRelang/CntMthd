import numpy as np
from math import e


def third_task():
    a = -1
    b = 4

    while abs(a - b) > 0.01:
        print(f"{a} {b}", end=" ")
        x1 = round(b - (b - a)/1.618, 5)
        x2 = round(a + (b - a)/1.618, 5)
        print(f"{x1} {x2}", end=" ")
        fx1 = round(e**(x1 - 0.8) - 2.2*x1, 5)
        fx2 = round(e**(x2 - 0.8) - 2.2 * x2, 5)
        print(f"{fx1} {fx2}", end="\n")
        if fx1 < fx2:
            b = x2
        else:
            a = x1
        if abs(a - b) < 0.01:
            print(f"{a} {b}", end=" ")
            x1 = round(b - (b - a) / 1.618, 5)
            x2 = round(a + (b - a) / 1.618, 5)
            print(f"{x1} {x2}", end=" ")
            fx1 = round(e ** (x1 - 0.8) - 2.2 * x1, 5)
            fx2 = round(e ** (x2 - 0.8) - 2.2 * x2, 5)
            print(f"{fx1} {fx2}", end="\n")


def print_template(u, num):
    print(f"Template {num}: ")
    for i in range(16, 0, -4):
        print(f"{u[i - 4]} {u[i - 3]} {u[i - 2]} {u[i - 1]}")
    print("\n")


def second_task(u_prev, level=1):
    u = np.zeros(len(u_prev))

    u[0] = round(0.25*(17.889 + u_prev[1] + u_prev[4]), 4)
    u[1] = round(0.25*(u[0] + u_prev[2] + u_prev[5]), 4)
    u[2] = round(0.25*(u[1] + u_prev[3] + u_prev[6]), 4)
    u[3] = round(0.25*(3.2 + u[2] + u_prev[7]), 4)

    u[4] = round(0.25*(25.298 + u[0] + u_prev[5] + u_prev[8]), 4)
    u[5] = round(0.25*(u[1] + u[4] + u_prev[6] + u_prev[9]), 4)
    u[6] = round(0.25*(u[2] + u[5] + u_prev[7] + u_prev[10]), 4)
    u[7] = round(0.25*(4.8 + u[3] + u[6] + u_prev[11]), 4)

    u[8] = round(0.25*(30.984 + u[4] + u_prev[9] + u_prev[12]), 4)
    u[9] = round(0.25*(u[5] + u[8] + u_prev[10] + u_prev[13]), 4)
    u[10] = round(0.25*(u[6] + u[9] + u_prev[11] + u_prev[14]), 4)
    u[11] = round(0.25*(4.8 + u[7] + u[10] + u_prev[15]), 4)

    u[12] = round(0.25*(67.777 + u[8] + u_prev[13]), 4)
    u[13] = round(0.25*(24 + u[9] + u[12] + u_prev[14]), 4)
    u[14] = round(0.25*(16 + u[10] + u[13] + u_prev[15]), 4)
    u[15] = round(0.25*(11.2 + u[11] + u[14]), 4)

    if max(np.around(abs((u - u_prev)), decimals=4)) < 0.1:
        print_template(u, level)
        return
    else:
        print_template(u, level)
        second_task(u, level=level+1)


u0 = np.array([14.9512, 12.0134, 9.0756, 6.1378,
               21.1984, 17.0988, 12.9992, 8.8996,
               25.7472, 20.5104, 15.2736, 10.0368,
               29.2616, 22.7462, 16.2308, 9.7154
               ])

print_template(u0, 0)
second_task(u0)
