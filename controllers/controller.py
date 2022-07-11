from flask import render_template,redirect, request
from app import app
from models.game import players, add_player
from models.player import Player
from models.game import Game

@app.route('/')
def index():
    return render_template('choose.html', players=players)

# @app.route("/play/new")
# def adding_player():
#         return render_template("add_player.html")


@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    winner = game.who_will_win()
    print(winner)
    return redirect("choose.html")

