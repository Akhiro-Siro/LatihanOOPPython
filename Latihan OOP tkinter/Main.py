import tkinter

main_window = tkinter.Tk()

lebel1 = tkinter.Label(main_window, text="Siro")
lebel2 = tkinter.Label(main_window, text="lebel2")

btn1 = tkinter.Button(main_window, text="btn 1")
btn2 = tkinter.Button(main_window, text="btn 2")


# methods positioning
lebel1.pack()
lebel2.pack()

btn1.pack()
btn2.pack()

# methods menmpilkan GUI
main_window.mainloop()
