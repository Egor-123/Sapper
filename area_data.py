from random import randint

coefficient = 4

def init_game_area_data(game_area_size):
    return [None for i in range(game_area_size**2)]

def get_mines_count(game_area_size):
    return game_area_size**2 // coefficient

def set_mines_data(game_area_data, mines_count):
    game_area_length = len(game_area_data)
    i = 1

    while i <= mines_count:
        random_cell = randint(0, game_area_length - 1)
        is_mine_in_ceil = game_area_data[random_cell] == '☠'

        if not is_mine_in_ceil:
            game_area_data[random_cell] = '☠'
            i = i + 1


    return game_area_data

def get_count_near_mines(game_area_data, game_area_size, number):
    right = 0
    left = 0
    top = 0
    top_left = 0
    top_right = 0
    bottom = 0
    bottom_left = 0
    bottom_right = 0

    can_right = number % game_area_size != game_area_size - 1
    can_left = number % game_area_size !=0
    can_top = number // game_area_size != 0
    can_bottom = number //game_area_size != game_area_size - 1

    if can_left:
        left = 1 if game_area_data[number - 1] == '☠' else 0

    if can_right:
        right = 1 if game_area_data[number + 1] == '☠' else 0

    if can_top:
        top = 1 if game_area_data[number - game_area_size] == '☠' else 0

    if can_top and can_left:
        top_left = 1 if game_area_data[number - game_area_size - 1] == '☠' else 0

    if can_top and can_right:
        top_right = 1 if game_area_data[number - game_area_size + 1] == '☠' else 0

    if can_bottom:
        bottom = 1 if game_area_data[number + game_area_size] == '☠' else 0

    if can_bottom and can_left:
        bottom_left = 1 if game_area_data[number + game_area_size - 1] == '☠' else 0

    if can_bottom and can_right:
        bottom_right = 1 if game_area_data[number + game_area_size + 1] == '☠' else 0

    return right + left + top + top_left + top_right + bottom + bottom_left + bottom_right