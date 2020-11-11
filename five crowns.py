# The app will have 2 choices when launching:
# ongoing competition or single play

from functions import *

game_type = input("ongoing competition or single play?  ")

if game_type == 'single play':
    people()
    player_name()
    scores()
    round_scores()
    final_scores()
    winner()
