import tkinter


def hello():
    print("Hello, world")


def bye(event):
    print("Good By")


root = tkinter.Tk()
button1 = tkinter.Button(master=root, text="НАЖМИ МЕНЯ")
button1.pack()
button1["command"] = hello

root.bind("<Key>", bye)

root.mainloop()
