# This program will allocate Teams randomly from a list of names 
# 1. Import Modules
# 2. Create a list of every genius 
# 3. use random module to randomly shulffle the list 
# 4. Loop through the list and display each teams players 



import random 
# create a list of players stored in the players variable 
players = ["devon", "max", "braylen",
          "Ollie", "Xavier", "Avery" 
          "Carl", "Walter", "darren"
          "EJ", "Nahum", "Joaquain"
          "Marshawn", "Ja'dee","Isaiah",
          "Kenlon","Nishad","Kauri","kris",
          "Joseph", "Semaj", "tay","Taquari","jarmauri"]
         


def PickTeams(players):       #Create our function 
    random.shuffle(players)       # shuffle the list of players 
    Team1 = players[:len(players) // 2]     # Put the first halve of the list of players into team1
    teamCaptain1= Team1[random.randrange(0,12)]    # randomly assign a team captin 

    print("Team 1:")
    print("Team captain:"+ teamCaptain1 )
    for player in Team1:
     print(player)

team2 = players[len(players) // 2:]
teamCaptain2 = team2[random.randrange(0,12)]
print("TEAM 2")
print("Team 2 Captain: " + teamCaptain2 )
for player in team2:
    print(player)

PickTeams(players)