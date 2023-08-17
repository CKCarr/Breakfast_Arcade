import os
from flask import Flask, render_template, json, Blueprint
import requests

APP_ID = os.environ.get('EDAMAM_APP_ID')
APP_KEY = os.environ.get('EDAMAM_APP_KEY')

recipes_blueprint = Blueprint('recipes', __name__)

app = Flask(__name__)

@recipes_blueprint.route('/recipes')
def get_recipes():
    base_url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "type": "public",
        "q": "breakfast",
        "mealType": "Breakfast",
        "field": ["uri", "label", "image", "source", "url", "shareAs"
                  "yield", "dietLabels", "healthLabels", "cautions",
                  "ingredientLines", "ingredients", "calories", "totalWeight",
                  "totalTime", "totalNutrients", "totalDaily", "digest"]
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    recipes = data.get('hits', [])

    return render_template('recipes.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
