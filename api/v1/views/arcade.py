# arcade.py
from flask import Blueprint, Flask, render_template, json

arcade_blueprint = Blueprint('arcade', __name__)

app = Flask(__name__)

@arcade_blueprint.route('/game')
def get_game():
    pass



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
