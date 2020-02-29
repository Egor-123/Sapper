import tkinter as tk
from tkinter import messagebox
import area_data
root = tk.Tk()

min_game_area_size = 4
max_game_area_size = 10

restart_button = None
game_area_data = []
buttons_list = []

def init_game(start_button, input_element):
    global game_area_data

    game_area_size = input_element.get()

    if game_area_size == '':
        return

    game_area_size = int(game_area_size)
    game_area_size = get_correct_size(game_area_size)

    game_area_data = area_data.init_game_area_data(game_area_size)
    game_mines_count = area_data.get_mines_count(game_area_size)
    game_area_data = area_data.set_mines_data(game_area_data, game_mines_count)

    input_element.destroy()
    start_button.destroy()

    start_game(game_area_size)

def get_correct_size(n):
    if n < min_game_area_size:
        return min_game_area_size
    elif n > max_game_area_size:
        return max_game_area_size
    return n


def restart_game():
    global restart_buttond

    if restart_button:
        restart_button.destroy()
    for button in buttons_list:
        button.destroy()

    buttons_list.clear()

    start()

def check_winnig():
    for el in game_area_data:
        if not el:
            return

    messagebox.showinfo('Уведомление', 'Победа!')
    restart_game()


def on_cell_click(number):
    if game_area_data[number] == '☠':
        messagebox.showinfo('Уведомление', 'Вы проиграли!')
        restart_game()
        return

    print(buttons_list)
    game_area_data[number] = '✓'
    buttons_list[number].config(state='disabled', text='✓')
    check_winnig()

def start_game(size):
    global game_area_data, restart_button

    for i in range(size ** 2):
        button = tk.Button(root, width=4, height=2, text=game_area_data[i], command=lambda number=i: on_cell_click(number))
        buttons_list.append(button)

    for g in range(len(buttons_list)):
        row_num = g // size + 1
        column_num = g % size
        button = buttons_list[g]
        button.grid(row=row_num, column=column_num)

    restart_button = tk.Button(root, width=4, height=2, text='R', command=lambda: restart_game())
    restart_button.grid()


def start():
    input_element = tk.Entry(root)
    start_button = tk.Button(root, width=5, height=1, text='start', command=lambda: init_game(start_button, input_element))

    input_element.grid(row=0, column=0)
    start_button.grid(row=0, column=1)

root.title('Сапёр')
root.minsize(480, 360)
root.resizable(width=True, height=True)



start()
root.mainloop()
