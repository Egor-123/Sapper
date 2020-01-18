import tkinter as tk
root = tk.Tk()


def init_game():
    game_area_size = input_element.get()

    if game_area_size == '':
        return

    game_area_size = int(game_area_size)
    start_game(game_area_size)


def start_game(size):
    input_element.destroy()
    start_button.destroy()

    for i in range(size ** 2):
        button = tk.Button(root, width=2, height=1)
        buttons_list.append(button)

    for g in range(len(buttons_list)):
        row_num = g // size + 1
        column_num = g % size
        button = buttons_list[g]
        button.grid(row=row_num, column=column_num)


input_element = tk.Entry(root)
start_button = tk.Button(root, width=5, height=1, text='start', command=init_game)

root.title('Сапёр')
root.minsize(480, 360)
root.resizable(width=True, height=True)

buttons_list = []
input_element.grid(row=0, column=0)
start_button.grid(row=0, column=1)

root.mainloop()
