# The app will have 2 choices when launching:
# ongoing competition or single play

game_type = input("ongoing competition or single play?  ")
players = {}

if game_type == 'single play':
    users = (input("how many players? "))
    while users.isdigit() == False:
        users = (input("how many players? "))
    users = int(users)
    
    # capture each player's name and store in dict
    for person in range(users):
        name = input("player's name?  ")
        players[name] = []
        
    # The game has rounds 3-13
    rounds = range(3,14)

    # ask each player their score after each round and append to dict
    # also list running score after each round
    for round in rounds:
        for player in players:
            score = (input(f"{player.title()}'s round {round} score?  "))
            while score.isdigit() == False:
                score = (input(f"{player.title()}'s round {round} score?  "))
            players[player].append(int(score))
      
        print(f"\nScores after round {round}")
        for player, score in players.items():
            print(f"{player.title()}: {sum(score)}")
        print()
  
    # print out the scores for each round
    print()
    print("Scores By Round")
    print(players)
   
    # tell each player their final score
    for player, score in players.items():
        print(f"\n{player.title()}'s final score is {sum(score)}")

    # Announce the winner
    scores = []
    for player, score in players.items():
        scores.append(sum(score)) 
    
    scores.sort()
    score_spread = scores[1] - scores[0]
    
    winner=min(players, key=lambda p:sum(players[p]))
   
    if score_spread == 0:
        print()
    elif score_spread == 1:
        print(f"\nThe winner is {winner.title()} by {score_spread} point!")
    else:
        print(f"\nThe winner is {winner.title()} by {score_spread} points!")

    print()
