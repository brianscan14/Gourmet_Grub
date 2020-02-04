import os, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env
    
APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

MONGO = PyMongo(APP)

@APP.route("/")
def index():
    return render_template('pages/index.html')

@APP.route('/get_recipies')
def get_recipies():
    curent_page = int(request.args.get('curent_page', 1))
    total_docs = MONGO.db.recipies.count_documents({})
    total_recipes = MONGO.db.recipies.find().skip((curent_page - 1)*6).limit(6)
    num_pages = range(1, int(total_docs / 6) + 2)

    return render_template("pages/recipies.html", recipies=total_recipes, 
    curent_page=curent_page, num_pages=num_pages, total=total_docs)

@APP.route('/search_recipe', methods=["GET", "POST"])
def search_recipe():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = MONGO.db.recipies.find({
        '$or': [
            {'recipe_name': query},
            {'ingredients': query}]})

    if results.count() > 0:
        return render_template('pages/searchrecipe.html', 
        query=rec_search_query, results=results)
        
    else:
        return render_template('pages/searchnull.html', 
        query=rec_search_query, results=results)

@APP.route('/recipe_selected/<recipe_id>')
def recipe_selected(recipe_id):
    recipies = MONGO.db.recipies.find_one({'_id': ObjectId(recipe_id)})
    return render_template('pages/recipe.html', recipe=recipies)

@APP.route('/add_recipe')
def add_recipe():
    return render_template('pages/addrecipe.html', 
    recipies=MONGO.db.recipies.find())

@APP.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipies = MONGO.db.recipies
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

@APP.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipeDB = MONGO.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = MONGO.db.recipies.find()
    return render_template('pages/editrecipe.html', 
    recipe=recipeDB, recipies=all_cuisine) 

@APP.route('/update_recipe/<recipe_id>', methods=['GET', 'POST']) 
def update_recipe(recipe_id): 
    recipies = MONGO.db.recipies
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

@APP.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    MONGO.db.recipies.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('get_recipies'))

@APP.route('/get_cuisines')
def get_cuisines():
    return render_template('pages/cuisines.html',
    recipies=MONGO.db.recipies.find().distinct("cuisine_name"))

@APP.route('/search_cuisines')
def search_cuisines():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = MONGO.db.recipies.find({'cuisine_name': query})
    return render_template('pages/searchcuisines.html', 
    query=rec_search_query, results=results)


@APP.route("/find_meals", methods=['GET', 'POST'])
def find_meals():
    recipies = MONGO.db.recipies
    if request.method == 'POST':
        requested_meal_type = request.form.get("meal_type")
        recipies = MONGO.db.recipies.find({"meal_type": requested_meal_type})

        if recipies.count() > 0:
            return render_template("pages/mealresults.html", recipies=recipies)

        else:
            return render_template('pages/searchnull.html', query=request.form.get("meal_type"))
        
    return render_template("pages/findmeals.html")

@APP.route("/meal_results")
def meal_results():
    return render_template('pages/mealresults.html')

@APP.route("/thankyoupage")
def thankyoupage():
    return render_template('pages/thankyou.html')

@APP.errorhandler(404) 
def not_found(e): 
    return render_template("pages/error404.html")

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)