from flask import Flask, render_template
from api.v1.views.arcade import arcade_blueprint
from api.v1.views.recipes import recipes_blueprint
from dotenv import load_dotenv
from flask import jsonify
from flask_cors import CORS
import sys
import os
print(sys.path)

port = int(os.environ.get("PORT", 5000))
host = os.environ.get("HOST", '0.0.0.0')
load_dotenv()  # Load environment variables from .env file

app = Flask(__name__, static_url_path='/static')

CORS(app)  # Enable CORS for all routes

app.register_blueprint(arcade_blueprint, url_prefix='/arcade')

app.register_blueprint(recipes_blueprint, url_prefix='/recipes')

# Test environment variables
# @app.route('/test_env')
# def test_env():
#    return jsonify({'APP_ID': os.environ.get('EDAMAM_APP_ID'),
#                    'APP_KEY': os.environ.get('EDAMAM_APP_KEY')})

@app.route('/api/v1/status/', methods=['GET'], strict_slashes=False)
def get_status():
    # Your status logic here
    return jsonify({'status': 'OK'})

@app.route('/', strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/contacts', strict_slashes=False)
def contacts():
    return render_template('contacts.html')

@app.route('/arcade', strict_slashes=False)
def arcade():
    return render_template('arcade_game.html')

@app.route('/recipes', strict_slashes=False)
def recipes():
    return render_template('static_recipes.html')


if __name__ == '__main__':
    app.run(host=host, port=port, debug=False)
