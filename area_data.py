from random import randint

coefficient = 4

def init_game_area_data(game_area_size):
    return [None for i in range(game_area_size**2)]

def get_mines_count(game_area_size):
    return game_area_size**2 // coefficient

def set_mines_data(game_area_data, mines_count):
    game_area_length = len(game_area_data)

    for i in range(mines_count):
        random_cell = randint(0, game_area_length - 1)
        print(random_cell)
        game_area_data[random_cell] = 'x'

    return game_area_data

