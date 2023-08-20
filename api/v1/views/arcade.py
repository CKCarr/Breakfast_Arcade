# arcade.py
from flask import Blueprint, render_template


arcade_blueprint = Blueprint('arcade', __name__)

@arcade_blueprint.route('/game', strict_slashes=False)
def get_game():
   return render_template('p5game.html')

