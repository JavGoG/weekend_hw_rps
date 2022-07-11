from models.player import Player

player_1 = Player ("Pepe", "Scissors")
player_2 = Player ("Juan", "Rock")
choices = ["Rock", "Paper", "Scissors"]

players = [player_1, player_2]

def add_player(player):
        players.append(player)

    
class Game:

    
    def who_will_win(player1, player2):
        if player1.choice == player2.choice or player1 == None or player2 == None:
            return "Draw!"
        if player1.choice == "Rock" & player2.choice == "Scissors":
            return f"Wins {player1.name}!"
        elif player1.choice == "Rock" & player2.choice == "Paper":
            return f"Wins {player2.name}!"
        elif player1.choice == "Paper" & player2.choice == "Scissors":
            return f"Wins {player2.name}!"
        elif player1.choice == "Paper" & player2.choice == "Rock":
            return f"Wins {player1.name}!"
        elif player1.choice == "Scissors" & player2.choice == "Rock":
            return f"Wins {player2.name}!"
        elif player1.choice == "Scissors" & player2.choice == "Paper":
            return f"Wins {player1.name}!"

    

        


