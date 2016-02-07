import tkinter as tk


root = tk.Tk()
# labels = tk.Label(root, text="Hello")
# button = tk.Button(root, text="Me is button")
# labels.pack()
# button.pack()
frame = tk.Frame(root, name='menu bar')
menubutton = tk.Menubutton(frame, text='file')
menu = tk.Menu(frame)



menubutton.pack()
menu.pack()
frame.pack()









root.mainloop()