from flask import Flask, render_template
from api.v1.views.arcade import arcade_blueprint
from api.v1.views.recipes import recipes_blueprint
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

app.register_blueprint(arcade_blueprint, url_prefix='/arcade')
app.register_blueprint(recipes_blueprint, url_prefix='/recipes')



@app.route('/api/v1/status/', methods=['GET'])
def get_status():
    # Your status logic here
    return jsonify({'status': 'OK'})

@app.route('/')
def home():
    return render_template('breakfast_arcade.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/arcade')
def arcade():
    return render_template('arcade_game.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
