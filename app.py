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
    return render_template('add_recipe.html', cuisine=mongo.db.cuisine.find())

@app.route('/insert_recipe', methods=['POST']) 
def insert_recipe():
    recipies = mongo.db.recipies
    recipies.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipies'))

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipeDB = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.cuisine.find()
    return render_template('edit_recipe.html', recipe=recipeDB, cuisine=all_cuisine) 

@app.route('/update_recipe/<recipe_id>', methods=['POST']) 
def update_recipe(recipe_id): 
    recipies = mongo.db.recipies
    recipies.update( {'_id': ObjectId(recipe_id)}, 
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_prep':request.form.get('recipe_prep'),
        'cuisine': request.form.get('cuisine'),
        'tools': request.form.get('tools'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients')
    })
    return redirect(url_for('get_recipies'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('get_recipies'))

@app.route('/get_cuisines') 
def get_cuisines(): 
    return render_template('cuisines.html', 
    cuisine=mongo.db.cuisine.find())

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))

@app.route('/edit_cuisine/<cuisine_id>') 
def edit_cuisine(cuisine_id): 
    return render_template('edit_cuisine.html', 
    cuizine=mongo.db.cuisine.find_one({'_id': ObjectId(cuisine_id)}))

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisine.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_cuisines'))

@app.route('/insert_cuisine', methods=['POST']) 
def insert_cuisine():
    cuisine_doc = {'cuisine_name': request.form.get('cuisine_name')}
    mongo.db.cuisine.insert_one(cuisine_doc)
    return redirect(url_for('get_cuisines'))

@app.route('/add_cuisine') 
def add_cuisine():
    return render_template('add_cuisine.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)