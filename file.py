import turtle
screen = turtle.Screen()
screen.title("Italy Regions Game")
screen.setup(width=700, height=780)
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()