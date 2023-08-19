# arcade.py
from flask import Blueprint, Flask, render_template, json, send_from_directory

arcade_blueprint = Blueprint('arcade', __name__)

app = Flask(__name__)

@arcade_blueprint.route('/game', strict_slashes=False)
def get_game():
   return render_template('p5game.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
