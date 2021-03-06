## Functions & variables ##
players = {} 
rounds = range(3,14)
users = ""
champ = ""
import json
import os.path


def people():
    """capture the number of players"""
    users = (input("how many players? "))
    while not users.isdigit():
        users = (input("how many players? "))
    return int(users)

def player_name():
    """capture each player's name"""
    for person in range(users):
        name = input("player's name?  ")
        players[name] = []

def scores():
    """capture players' scores"""
    for round in rounds:
        for player in players:
            score = (input(f"{player.title()}'s round {round} score?  "))
            while not score.isdigit():
                score = (input(f"{player.title()}'s round {round} score?  "))
            players[player].append(int(score))
      
        print(f"\nScores after round {round}")
        for player, score in players.items():
            print(f"{player.title()}: {sum(score)}")
        print()

def round_scores():
    """list each player's score by round"""
    print("\nScores By Round")
    print(players)

def final_scores():
    """tell each player their final score"""
    for player, score in players.items():
        print(f"\n{player.title()}'s final score is {sum(score)}")

def winner():
    """announce the winner"""
    scores = []
    for player, score in players.items():
        scores.append(sum(score)) 
    
    scores.sort()
    score_spread = scores[1] - scores[0]
    
    champ=min(players, key=lambda p:sum(players[p]))
       
    if score_spread == 0:
        print("There is a tie.")
    elif score_spread == 1:
        print(f"\nThe winner is {champ.title()} by {score_spread} point!")
    else:
        print(f"\nThe winner is {champ.title()} by {score_spread} points!")

    return champ
    print()


## start of executable code ##
game_type = input("single play or ongoing play?  ")

if game_type == 'single play':

    #capture the number of players
    users = people()  

    #capture each player's name 
    player_name()

    #capture each player's scores
    scores()

    #list scores after each round
    round_scores()

    #list final scores
    final_scores()

    #announce the winner
    winner()

if game_type == 'ongoing play':
    groups = {}
    group = input('is this a new group? (y/n) ')

    if group == 'y':
        group_name = input('group name? ')
        groups[group_name] = {}

        users = people()

        for person in range(users):
            name = input("player's name?  ")
            players[name] = []
            groups[group_name][name] = []

        print(groups)      
        scores()
        round_scores()
        final_scores()
        champ = winner()

        groups[group_name][champ].append(1)
        stored_groups = []
        #groups_file = Path("C:\Users\502864\Five Crowns\five_crowns\groups.py")

        # if groups_file.is_file():
        with open('C:/Users/502864/Five Crowns/five_crowns/groups.json', 'a') as f:
            json.dump(groups, f)
        # else:
        #     with open('groups.json', 'a') as f:
        #         json.dumps(stored_groups, f)
        #         json.dumps(groups, f)
        print(groups)
 
        for player, score in groups[group_name].items():
            print(f"\n{player.title()}'s number of wins are {sum(score)}")

        print()
        with open('C:/Users/502864/Five Crowns/five_crowns/groups.json') as f:
            gps = f.read()
            print(gps)