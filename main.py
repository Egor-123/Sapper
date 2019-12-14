import tkinter as tk
root = tk.Tk()

from tkinter import messagebox
messagebox.showinfo("Сапёр",)

root.title('Сапёр')
root.minsize(480,360)
root.resizable(width = True, height = True)

#input =

size = 10
buttons_list = []
#вынести в отдельную функци
def size():
    for i in range(size**2):
        button = tk.Button(root, width=2, height=1)
        buttons_list.append(button)

for g in range(len(buttons_list)):
    row_num = g // size + 1
    column_num  = g % size
    button = buttons_list[g]
    button.grid(row=row_num, column=column_num)



root.mainloop()
