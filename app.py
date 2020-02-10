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
    return render_template('pages/index.html')

@APP.route('/get_recipies')
def get_recipies():
    """
    Returns all the recipes in the DB to the page. Returns 6 recipes per page
    and uses pagination to give better viewing experience. Done by the DB to
    improve loading times as it only loads 6 recipes at a time, not all at once.
    """
    curent_page = int(request.args.get('curent_page', 1))
    total_docs = MONGO.db.recipies.count_documents({})
    total_recipes = MONGO.db.recipies.find().skip((curent_page - 1)*6).limit(6)
    num_pages = range(1, int(total_docs / 6) + 2)

    return render_template("pages/recipies.html", recipies=total_recipes,
    curent_page=curent_page, num_pages=num_pages, total=total_docs)

@APP.route('/search_recipe', methods=["GET", "POST"])
def search_recipe():
    """
    Uses regex to handle the search form input entered, or 'query', ignores
    case and searches the DB fields recipe name and ingredients for any
    matches of the strings entered, doesn't have to be exact full word. If
    there is a match then it returns the matching recipe cards in an ew page.
    If there are no results then user it redirected to a 'null' results page.
    """
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = MONGO.db.recipies.find({
        '$or': [
            {'recipe_name': query},
            {'ingredients': query}]})

    if results.count() > 0:
        return render_template('pages/searchrecipe.html',
        query=rec_search_query, results=results)

    return render_template('pages/searchnull.html',
    query=rec_search_query, results=results)

@APP.route('/recipe_selected/<recipe_id>')
def recipe_selected(recipe_id):
    """
    Uses the recipe's unique id form the mongoDB to id it and return it.
    """
    recipies = MONGO.db.recipies.find_one({'_id': ObjectId(recipe_id)})
    return render_template('pages/recipe.html', recipe=recipies)

@APP.route('/add_recipe')
def add_recipe():
    """
    Add recipe page to allow the user to add a new recipe they like
    to the DB, this brings you to the form to do so.
    """
    return render_template('pages/addrecipe.html',
    recipies=MONGO.db.recipies.find())

@APP.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """
    Inserts the recipe that the user has just created on the add recipe
    page into the DB with the below structure, prep and ingredient steps
    use getlist to iterate through the steps in each. Once inserted the
    user is then returnd to a thank you page to inform them they were
    successsfull, also showing them the recipe they just inserted.
    """
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
    """
    Edit page that uses the recipe selected's unique id and returns
    it in the form format ready to be edited.
    """
    recipeDB = MONGO.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = MONGO.db.recipies.find()
    return render_template('pages/editrecipe.html',
    recipe=recipeDB, recipies=all_cuisine)

@APP.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    """
    Posts the updated recipe to the mongoDB and then reurns you
    to the pge that shows all the recipes.
    """
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
    """
    Deletes the recipe from the DB once the 'delete' button is clicked.
    """
    MONGO.db.recipies.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipies'))

@APP.route('/get_cuisines')
def get_cuisines():
    """
    Returns all the cuisnes in the DB but avoids duplicates of the same ones
    by using 'distinct'.
    """
    return render_template('pages/cuisines.html',
    recipies=MONGO.db.recipies.find().distinct("cuisine_name"))

@APP.route('/search_cuisines')
def search_cuisines():
    """
    Below function uses regex to search the DB for all the recipes that contain
    the cuisine name that is the title of the card when the button is clicked.
    The button has the value of the cuisine and this function uses that as the
    'query' value to return the matching recipes.
    """
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = MONGO.db.recipies.find({'cuisine_name': query})
    return render_template('pages/searchcuisines.html',
    query=rec_search_query, results=results)


@APP.route("/find_meals", methods=['GET', 'POST'])
def find_meals():
    """
    Allows user to search for recipes that match 1 of 3 meal types from a
    dropdown. Requested meal type value is gotten from the form input value
    which is one of the 3 options, and returns all recipes in the DB that
    match this meal type. If there are no mtaches then the 'null' results
    page is returned instead.
    """
    recipies = MONGO.db.recipies
    if request.method == 'POST':
        requested_meal_type = request.form.get("meal_type")
        recipies = MONGO.db.recipies.find({"meal_type": requested_meal_type})

        if recipies.count() > 0:
            return render_template("pages/mealresults.html", recipies=recipies)

        else:
            return render_template('pages/searchnull.html',
            query=request.form.get("meal_type"))

    return render_template("pages/findmeals.html")

# @APP.route("/meal_results")
# def meal_results():
#     """
#     Content to be added.
#     """
#     return render_template('pages/mealresults.html')

# @APP.route("/thankyoupage")
# def thankyoupage():
#     """
#     Page returned with the recipe that was added and a 'Thank You'
#     heading, lets the user know they successfully added a recipe.
#     """
#     return render_template('pages/thankyou.html')

@APP.errorhandler(404)
def not_found(e):
    """
    Error handler for any 404 errors with the page, returns the
    template to redirect them back to the home page with a button click.
    """
    return render_template("pages/error404.html")

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
