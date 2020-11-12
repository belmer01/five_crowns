## Functions & variables ##

# capture each player's name
def player_name():
    for person in range(users):
        name = input("player's name?  ")
        players[name] = []

players = {}
rounds = range(3,14)

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
    print()
    print("Scores By Round")
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
    
    winner=min(players, key=lambda p:sum(players[p]))
   
    if score_spread == 0:
        print("There is a tie.")
    elif score_spread == 1:
        print(f"\nThe winner is {winner.title()} by {score_spread} point!")
    else:
        print(f"\nThe winner is {winner.title()} by {score_spread} points!")

    print()


## start of executable code ##
game_type = input("ongoing competition or single play?  ")

if game_type == 'single play':
    users = (input("how many players? "))
    while not users.isdigit():
        users = (input("how many players? "))
    users = int(users)
    
    player_name()
    scores()
    round_scores()
    final_scores()
    winner()
