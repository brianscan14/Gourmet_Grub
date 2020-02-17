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
    """
    Returns home page of the app which contains the search bar
    """
    return render_template('pages/index.html', active_home='active')

@APP.route('/recipes')
def recipes():
    """
    Returns all the recipes in the DB to the page. Returns 6 recipes per page
    and uses pagination to give better viewing experience. Done by the DB to
    improve loading times as it only loads 6 recipes at a time, not all at
    once. Returns null page if DB is empty.
    """
    recipies = MONGO.db.recipies.find()
    curent_page = int(request.args.get('curent_page', 1))
    total_docs = MONGO.db.recipies.count_documents({})
    total_recipes = MONGO.db.recipies.find().skip((curent_page - 1)*6).limit(6)
    num_pages = range(1, int(total_docs / 6) + 2)

    if recipies.count() > 0:
        return render_template("pages/recipies.html", recipies=total_recipes,
        curent_page=curent_page, num_pages=num_pages, total=total_docs,
        active_recipes='active', page_title='/All Recipes')

    return render_template('pages/searchnull.html', query='recipes',
    page_title='/No Results')

@APP.route('/search/recipes')
def search_recipe():
    """
    Uses regex to handle the search form input entered, or 'query', ignores
    case and searches the DB fields recipe name and ingredients for any
    matches of the strings entered, doesn't have to be exact full word. If
    there is a match then it returns the matching recipe cards in an ew page.
    If there are no results then user it redirected to a 'null' results page.
    """
    rec_search_query = request.args['query']
    query = {'$regex': 
    re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = MONGO.db.recipies.find({
        '$or': [
            {'recipe_name': query},
            {'ingredients': query}]
        }).sort([('views', -1)])

    if results.count() > 0:
        return render_template('pages/searchrecipe.html',
        query=rec_search_query, results=results, page_title='/Recipe Search')

    return render_template('pages/searchnull.html',
    query=rec_search_query, results=results, page_title='/No Results')

@APP.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """
    Uses the recipe's unique id form the mongoDB to id it and return it.
    """
    recipies = MONGO.db.recipies.find_one_and_update(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"views": int(1)}}, new=True)

    return render_template('pages/recipe.html', recipe=recipies,
    page_title='/Recipe')

@APP.route('/add', methods=["GET", "POST"])
def add():
    """
    Add recipe page to allow the user to add a new recipe they like
    to the DB, this brings you to the form to do so with the GET
    request by using a conditional statment.
    If it is a POST request then it inserts the recipe that the user
    has just created on the add recipe page into the DB with the below
    structure, prep and ingredient steps use getlist to iterate through
    the steps in each. Once inserted the user is then returnd to a
    thank you page to inform them they were successsfull, also showing
    them the recipe they just inserted.
    """
    recipies = MONGO.db.recipies
    if request.method == 'GET':
        return render_template('pages/addrecipe.html',
        recipies=MONGO.db.recipies.find(), title='Add Recipe',
        active_add='active', page_title='/Add')

    this_recipe = recipies.insert_one(
        {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_prep': request.form.getlist('recipe_prep'),
        'recipe_desc': request.form.get('recipe_desc'),
        'cuisine_name': request.form.get('cuisine_name'),
        'image': request.form.get('image'),
        'ingredients': request.form.getlist('ingredients'),
        'meal_type': request.form.get('meal_type'),
        'calories': int(request.form.get('calories')),
        'duration': int(request.form.get('duration')),
        'views': int(1)
    })
    ret = recipies.find_one({"_id": this_recipe.inserted_id})
    return render_template('pages/thankyou.html', recipe=ret,
    title='Thank you for inserting below recipe', page_title='/Congrats')


@APP.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    """
    Edit page that uses the recipe selected's unique id and returns
    it in the form format ready to be edited. Conditional
    statement used to return the edit page itself if it is a GET
    request, and else if it's a POST it post it to the mongoDB.
    Sends the updated recipe to the mongoDB and then returns you
    to the page that shows all the recipes. $set operator used to
    fix a bug that reset the recipe views field to 0 when the user
    edited a recipe.
    """
    if request.method == 'GET':
        this_recipe = MONGO.db.recipies.find_one({"_id": ObjectId(recipe_id)})
        return render_template('pages/editrecipe.html',
        recipe=this_recipe, title='Edit Recipe', page_title='/Edit')

    recipies = MONGO.db.recipies
    recipies.update_one({'_id': ObjectId(recipe_id)},
    {'$set': {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_prep': request.form.getlist('recipe_prep'),
        'recipe_desc': request.form.get('recipe_desc'),
        'cuisine_name': request.form.get('cuisine_name'),
        'image': request.form.get('image'),
        'ingredients': request.form.getlist('ingredients'),
        'meal_type': request.form.get('meal_type'),
        'calories': int(request.form.get('calories')),
        'duration': int(request.form.get('duration'))}
    })
    return redirect(url_for('recipes'))

@APP.route('/delete/<recipe_id>')
def delete(recipe_id):
    """
    Deletes the recipe from the DB once the 'delete' button is clicked.
    """
    MONGO.db.recipies.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))

@APP.route('/cuisines')
def cuisines():
    """
    Returns all the cuisnes in the DB but avoids duplicates of the same ones
    by using 'distinct', returns null page if DB is empty.
    """
    null_recipes = MONGO.db.recipies.find()

    if null_recipes.count() > 0:
        return render_template('pages/cuisines.html', active_cuisines='active',
        recipies=MONGO.db.recipies.find().distinct("cuisine_name"),
        page_title='/Cuisines')

    return render_template('pages/searchnull.html',
    active='active', query='cuisines', page_title='/No Results')

@APP.route('/search/cuisines')
def search_cuisines():
    """
    Below function uses regex to search the DB for all the recipes that contain
    the cuisine name that is the title of the card when the button is clicked.
    The button has the value of the cuisine and this function uses that as the
    'query' value to return the matching recipes. No needs for 0 results page
    here as the previous page wouldn't populate in first place if there was
    no recipes.
    """
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query),
    re.IGNORECASE)}
    results = MONGO.db.recipies.find({'cuisine_name': query})
    return render_template('pages/searchcuisines.html',
    query=rec_search_query, results=results, page_title='/Results')

@APP.route("/meals", methods=['GET', 'POST'])
def meals():
    """
    Allows user to search for recipes that match 1 of 3 meal types from a
    dropdown. Requested meal type value is gotten from the form input value
    which is one of the 3 options, and returns all recipes in the DB that
    match this meal type. If there are no matches then the 'null' results
    page is returned instead. The first conditional statement determines if
    it is a POST request, this will return the meal results. There is a
    nested statement within this one to return results if there are any or
    else return the null page. If the page is a GET request then the page
    to search the values is returned.
    """
    recipies = MONGO.db.recipies
    if request.method == 'POST':
        requested_meal_type = request.form.get("meal_type")
        recipies = MONGO.db.recipies.find({
            "meal_type": requested_meal_type}).sort([('views', -1)])

        if recipies.count() > 0:
            return render_template("pages/mealresults.html",
            recipies=recipies, query=requested_meal_type,
            page_title='/Meals')

        else:
            return render_template('pages/searchnull.html',
            query=request.form.get("meal_type"), page_title='/No Results')

    return render_template("pages/findmeals.html", active_meals='active',
    page_title='/Search Meals')

@APP.errorhandler(404)
def not_found(e):
    """
    Error handler for any 404 errors with the page, returns the
    template to redirect them back to the home page with a button click.
    """
    return render_template("pages/error404.html", page_title='/404 Error')

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
