import os
import re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env
    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'good_grubDB'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipies')
def get_recipies():
    return render_template("recipies.html", recipies=mongo.db.recipies.find())

@app.route('/search_recipe')
def search_recipe():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = mongo.db.recipies.find({'recipe_name': query})
    return render_template('search_recipe.html', query=rec_search_query, results=results)

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', recipies=mongo.db.recipies.find())

@app.route('/insert_recipe', methods=['POST']) 
def insert_recipe():
    recipies = mongo.db.recipies
    recipies.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipies'))

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipeDB = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.recipies.find()
    return render_template('edit_recipe.html', recipe=recipeDB, recipies=all_cuisine) 

@app.route('/update_recipe/<recipe_id>', methods=['POST']) 
def update_recipe(recipe_id): 
    recipies = mongo.db.recipies
    recipies.update( {'_id': ObjectId(recipe_id)}, 
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_prep':request.form.get('recipe_prep'),
        'cuisine_name': request.form.get('cuisine_name'),
        'tools': request.form.get('tools'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients'),
        'meal_type':request.form.get('meal_type')
    })
    return redirect(url_for('get_recipies'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('get_recipies'))

@app.route('/get_cuisines') 
def get_cuisines(): 
    return render_template('cuisines.html', 
    recipies=mongo.db.recipies.find())

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.recipies.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))

@app.route('/edit_cuisine/<cuisine_id>') 
def edit_cuisine(cuisine_id): 
    return render_template('edit_cuisine.html', 
    meal_types=mongo.db.recipies.find_one({'_id': ObjectId(cuisine_id)}))

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.recipies.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_cuisines'))

# @app.route('/insert_cuisine', methods=['POST']) 
# def insert_cuisine():
#     cuisine_doc = {'cuisine_name': request.form.get('cuisine_name')}
#     mongo.db.recipies.insert_one(cuisine_doc)
#     return redirect(url_for('get_cuisines'))

# @app.route('/add_cuisine')
# def add_cuisine():
#     return render_template('add_cuisine.html')

@app.route("/find_meals", methods=['GET', 'POST'])
def find_meals():
    recipies = mongo.db.recipies
    if request.method == 'POST':
        requested_meal_type = request.form.get("meal_type")
        
        recipies = mongo.db.recipies.find({"meal_type": requested_meal_type})
        return render_template("meal_results.html", recipies=recipies)
        
    return render_template("find_meals.html")

@app.route("/meal_results")
def meal_results():
    return render_template('meal_results.html')

@app.route('/search_cuisines')
def search_cuisines():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = mongo.db.recipies.find({'cuisine_name': query})
    return render_template('search_cuisines.html', query=rec_search_query, results=results)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)