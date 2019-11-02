import tkinter as tk

root = tk.Tk()

root.title('Сапёр')
root.minsize(480,360)
root.resizable(width = True, height = True)

button_1 = tk.Button(root, width=2, height=1)
button_1.grid(row=1, column=0)
buttons_list = []
for i in range(10):
    # Здесь создаём кнопки и помещаем в список buttons_list
for g in range(# Проходимся по всем кнопкам);
    # Для каждой кнопки мы делаем grid с необходимами значениями row и column

root.mainloop()