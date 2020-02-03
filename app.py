import os
import re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env
    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template('pages/index.html')

@app.route('/get_recipies')
def get_recipies():
    curent_page = int(request.args.get('curent_page', 1))
    total_docs = mongo.db.recipies.count_documents({})
    total_recipes = mongo.db.recipies.find().skip((curent_page - 1)*6).limit(6)
    num_pages = range(1, int(total_docs / 6) + 2)

    return render_template("pages/recipies.html", recipies=total_recipes, 
    curent_page=curent_page, num_pages=num_pages, total=total_docs)

@app.route('/search_recipe', methods=["GET", "POST"])
def search_recipe():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = mongo.db.recipies.find({
        '$or': [
            {'recipe_name': query},
            {'ingredients': query}]})

    if results.count() > 0:
        return render_template('pages/searchrecipe.html', 
        query=rec_search_query, results=results)
        
    else:
        return render_template('pages/searchnull.html', 
        query=rec_search_query, results=results)

@app.route('/recipe_selected/<recipe_id>')
def recipe_selected(recipe_id):
    recipies = mongo.db.recipies.find_one({'_id': ObjectId(recipe_id)})
    return render_template('pages/recipe.html', recipe=recipies)

@app.route('/add_recipe')
def add_recipe():
    return render_template('pages/addrecipe.html', 
    recipies=mongo.db.recipies.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipies = mongo.db.recipies
    this_recipe = recipies.insert_one(
        {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_prep': request.form.getlist('recipe_prep'),
        'recipe_desc': request.form.get('recipe_desc'),
        'cuisine_name': request.form.get('cuisine_name'),
        'tools': request.form.get('tools'),
        'image': request.form.get('image'),
        'ingredients': request.form.getlist('ingredients'),
        'meal_type': request.form.get('meal_type'),
        'calories': request.form.get('calories'),
        'duration': request.form.get('duration')
    })
    ret = recipies.find_one({"_id": this_recipe.inserted_id})
    return render_template('pages/thankyou.html', recipe=ret)

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipeDB = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.recipies.find()
    return render_template('pages/editrecipe.html', 
    recipe=recipeDB, recipies=all_cuisine) 

@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST']) 
def update_recipe(recipe_id): 
    recipies = mongo.db.recipies
    recipies.update( {'_id': ObjectId(recipe_id)}, 
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_prep': request.form.getlist('recipe_prep'),
        'recipe_desc': request.form.get('recipe_desc'),
        'cuisine_name': request.form.get('cuisine_name'),
        'tools': request.form.get('tools'),
        'image': request.form.get('image'),
        'ingredients': request.form.getlist('ingredients'),
        'meal_type': request.form.get('meal_type'),
        'calories': request.form.get('calories'),
        'duration': request.form.get('duration')
    })
    return redirect(url_for('get_recipies'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('get_recipies'))

@app.route('/get_cuisines')
def get_cuisines():
    return render_template('pages/cuisines.html',
    recipies=mongo.db.recipies.find().distinct("cuisine_name"))

@app.route('/search_cuisines')
def search_cuisines():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = mongo.db.recipies.find({'cuisine_name': query})
    return render_template('pages/searchcuisines.html', 
    query=rec_search_query, results=results)


@app.route("/find_meals", methods=['GET', 'POST'])
def find_meals():
    recipies = mongo.db.recipies
    if request.method == 'POST':
        requested_meal_type = request.form.get("meal_type")
        recipies = mongo.db.recipies.find({"meal_type": requested_meal_type})

        if recipies.count() > 0:
            return render_template("pages/mealresults.html", recipies=recipies)

        else:
            return render_template('pages/searchnull.html', query=request.form.get("meal_type"))
        
    return render_template("pages/findmeals.html")

@app.route("/meal_results")
def meal_results():
    return render_template('pages/mealresults.html')

@app.route("/thankyoupage")
def thankyoupage():
    return render_template('pages/thankyou.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)