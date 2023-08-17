import os
from flask import Blueprint, Flask, render_template, app, json
import requests


APP_ID = os.environ.get('EDAMAM_APP_ID')
APP_KEY = os.environ.get('EDAMAM_APP_KEY')

recipes_blueprint = Blueprint('recipes', __name__)

@recipes_blueprint.route('/recipes')
def get_recipes():
    base_url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "type": "user",
        "q": "breakfast",
        "field": ["uri", "label"]
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Assuming the recipes are stored in the "hits" key based on Edamam's documentation
    recipes = data.get('hits', [])

    return render_template('recipes.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
