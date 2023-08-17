from flask import Flask, render_template
from api.v1.views.arcade import arcade_blueprint
from api.v1.views.recipes import recipes_blueprint
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.register_blueprint(arcade_blueprint, url_prefix='/arcade')
app.register_blueprint(recipes_blueprint, url_prefix='/recipes')

@app.route('/')
def main_page():
    return render_template('breakfast_arcade.html')

@app.route('/api/v1/status/', methods=['GET'])
def get_status():
    # Your status logic here
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
