import tkinter
from random import randint
import time

oval_id = None
x, y, r = 10, 20, 10
scores = 0
dx, dy = 4, 2


def tick():
    global x, y, dx, dy
    time_label.after(200, tick)
    time_label['text'] = time.strftime("%H:%M:%S")
    if oval_id is not None:
        x += dx
        y += dy
        if x + r >= 639 or  x - r <= 0:
            dx = -dx
        canvas.coords(oval_id, (x - r, y - r, x + r, y + r))



def start_game():
    global oval_id
    if oval_id is None:
        oval_id = canvas.create_oval(x-r, y-r, x+r, y+r, fill="green")
    else:
        print("Игра ещё не началась")


def delete_ball():
    global oval_id
    canvas.delete(oval_id)
    oval_id = None


def click_handler(event):
    global x, y, r, label, scores_label, scores
    print(event.x, event.y)
    if oval_id is not None:
        if ((event.x-x)**2 + (event.y-y)**2) <= r**2:
            print("Попал")
            scores += 1
            scores_label["text"] = "Ваши очки: " + str(scores)
            r = randint(10, 30)
            x = randint(0+r, 639-r)
            y = randint(0+r, 639-r)

        canvas.coords(oval_id, (x-r, y-r, x+r, y+r))


root = tkinter.Tk("Игра - лопни шарик")
root.geometry("640x480")

buttons_panel = tkinter.Frame(bg="gray", width=640)

button_start = tkinter.Button(buttons_panel, text="Start", command=start_game)
button_start.pack(side=tkinter.LEFT)

button_stop = tkinter.Button(buttons_panel, text="Stop", command=delete_ball)
button_stop.pack(side=tkinter.LEFT)

buttons_panel.pack(side=tkinter.TOP, anchor="nw", fill=tkinter.X)

time_label = tkinter.Label(buttons_panel, font='sans 20')
time_label.pack(side=tkinter.LEFT)

scores_label = tkinter.Label(buttons_panel, text="Ваши очки: 0")
scores_label.pack(side=tkinter.RIGHT)

canvas = tkinter.Canvas(root, bg="lightgray")
canvas.pack(side=tkinter.TOP, anchor="nw", fill=tkinter.BOTH, expand=1)
canvas.bind("<Button>", click_handler)

time_label.after_idle(tick)

root.mainloop()
