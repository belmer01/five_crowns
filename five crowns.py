## Functions & variables ##

players = {} 
rounds = range(3,14)
users = ""
champ = ""

# capture number of users
def people():
    users = (input("how many players? "))
    while not users.isdigit():
        users = (input("how many players? "))
    return int(users)

# capture each player's name
def player_name():
    for person in range(users):
        name = input("player's name?  ")
        players[name] = []

# capture player scores
def scores():
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

# print scores by round
def round_scores():
    print("\nScores By Round")
    print(players)

# tell each player their final score
def final_scores():
    for player, score in players.items():
        print(f"\n{player.title()}'s final score is {sum(score)}")

# announce the winner
def winner():
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

    users = people()   
    player_name()
    scores()
    round_scores()
    final_scores()
    winner()

if game_type == 'ongoing play':
    groups = {}
    group = input('is this a new group? (y/n) ')

    import json

    if group == 'y':
        group_name = input('group name? ')
        group_name = groups

        users = people()

        for person in range(users):
            name = input("player's name?  ")
            players[name] = []
            group_name[name] = []
              
        scores()
        round_scores()
        final_scores()
        champ = winner()

        group_name[champ].append(1)

        with open('groups.json', 'a') as f:
            json.dump({'group_name'}, f)
 
        for player, score in group_name.items():
            print(f"\n{player.title()}'s number of wins are {sum(score)}")

        print(group_name)