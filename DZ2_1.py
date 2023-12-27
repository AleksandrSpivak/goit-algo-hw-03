import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()

    for angle in [120, 120, 120]:
        koch_curve(t, order, size)
        t.right(angle)

    window.mainloop()


if __name__ == "__main__":
    recursion = input("Input recursion level\n")
    if recursion.isdigit():
        recursion = int(recursion)
        if recursion >= 0:
            draw_koch_curve(recursion)
        else:
            print("Wrong input")    
    else:
        print("Wrong input")
