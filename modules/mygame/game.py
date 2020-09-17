# game.py
# import the draw module
from mygame import draw

def play_game():
    print('we are playing a game with friends')
    return 'won!'

def main():
    result = play_game()
    draw.draw_game(result)
