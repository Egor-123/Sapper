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
        is_mine_in_ceil = game_area_data[random_cell] == 'x'

        if not is_mine_in_ceil:
            game_area_data[random_cell] = 'x'
            i = i + 1

    return game_area_data

