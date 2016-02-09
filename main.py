import tkinter as tk


PROGRAM_NAME = 'Wordcafe'

root = tk.Tk()
root.geometry('800x600')
root.title(PROGRAM_NAME)

# menu icons
new_file_icon = tk.PhotoImage(file='icons/new_file.gif')
open_file_icon = tk.PhotoImage(file='icons/open_file.gif')
save_file_icon = tk.PhotoImage(file='icons/save.gif')
cut_icon = tk.PhotoImage(file='icons/cut.gif')
copy_icon = tk.PhotoImage(file='icons/copy.gif')
paste_icon = tk.PhotoImage(file='icons/paste.gif')
undo_icon = tk.PhotoImage(file='icons/undo.gif')
redo_icon = tk.PhotoImage(file='icons/redo.gif')


menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', accelerator='Ctrl+N',
                      compound='left', image=new_file_icon, underline=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O',
                      compound='left', image=open_file_icon, underline=0)
file_menu.add_command(label='Save', accelerator='Ctrl+S',
                      compound='left', image=save_file_icon, underline=0)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S')
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4')
menu_bar.add_cascade(label='File', menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y',
	compound='left', image=redo_icon)


view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)


about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)


root.config(menu=menu_bar)


root.mainloop()
