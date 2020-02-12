# GourmetGrub

This Flask website was created as a platform for users to have the capability to create recipes of interest to them and post them to the site. They are also able to edit other recipes on the page or even delete them if they desire. This website uses a Mongo backend and visitors have the ability to search recipes already on the site,  it searches the MongoDB for strings in titles or ingredients that match the search input value. They can also swift through all the recipes present on the recipe with ease.

## UX

The main goal of this website is to offer users a quick and simple way to store and easily access cooking recipes. The pages are kept sleek and interactive so as to allow the user to easily navigate around all the recipes on the site.  The navbar at the top enkeeps with this team and allows the users to navigate to each page with ease, decreasing to a menu icon on smaller screen sizes.

The search bar on the index page is grand and bold, taking up the entire screen and giving the users an effective option of search recipes straight away. They can then search by meal times or cuisines if they are less certain for what they are searching for. All recipes are encompassed by BS4 cards which give the important information that a user may be looking for without having to click the actual recipe, e.g. "cooking time". 

### User Stories

1. Being a new visitor to the website, I want to be easily navigate the site and find information I was looking for in one or two clicks.
2. The different recipes to be presented to be in a tidy and easily readable manner.
3. To be able to find a particular recipe quickly by searching the word or a character string when I know what I want.
4. To be able to search by a food type or even meal type when I am less sure of what recipe I desire.
5. When browsing through the different recipes I want important pieces of info like cuisine type to be presented to me without having to click into it.
6. The recipe I decide on to be easily readable and followable step by step.
7. As a user contributing to the site, I expect aa certain level of feedback to confirm that my work was submitted successfully, such as a thank you page.
8. If using this site on a mobile phone, as you more that likely would in a kitchen I expect this site to be mobile/tablet friendly and be just as responsive as a desktop site would be.

## Wireframes

This website was designed with two screen size ranges in mind:

1. Mobile
2. Tablet-Desktop

As a result of this the below wireframes consist largely of only 2 mockups drawings (contact & footer are the exceptions). 

- Navbar
  - xs screen
  - sm-xl screen

- Home
  - xs screen
  - sm-xl screen

- Cuisines
  - xs screen
  - sm-xl screen

- Meals
  - xs screen
  - sm-xl screen

- Meal / Cuisine search results
  - xs screen
  - sm-xl screen 

- Home/Navbar search results
  - xs screen
  - sm-xl screen

- Add/Edit Recipe
  - xs screen
  - sm-xl screen

- All Recipes
  - xs screen
  - sm-xl screen

- Single recipe Page
  - xs screen
  - sm-xl screen

- Null search results
  - xs-xl screen

- Thank you page
  - xs-xl screen

## Technologies

### Front End

- This project uses Html, JavaScript & CSS programming languages.
- [Bootstrap](https://getbootstrap.com/)
  - Used to make the website more responsive and streamline the grid layout.
- [jQuery](https://jquery.com/)
  - Used for the navbar, also the modal and to simplify DOM manipulation.
- [Popper.js](https://popper.js.org/)
  - A reference JS needed for the navbar & modal.
- [FontAwesome](https://fontawesome.com/)
  - The site used BootstrapCDN to provide icons from FontAwesome.
- [Autoprefixer](https://autoprefixer.github.io/)
  - Used to validate the CSS code for all browsers.
- [Jinga](http://jinja.palletsprojects.com/en/2.10.x/)
  - To display data from the backend in html

### Back End

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Python framework used to build the app.
- [Pymongo](https://api.mongodb.com/python/current/)
  - Sends the queries to the DB.
- [MongoDB Altas](https://www.mongodb.com/)
  - Database used for this project
- [PIP](https://pip.pypa.io/en/stable/installing/)
  - To install tools used in the project

## Features

#### *Elements on each page*

##### Navbar:



##### Footer:



#### Home Page

##### *Hero Image*



##### Search Bar



#### Add Recipe Page



#### Edit Recipe Page



#### Cuisines Page



#### Cuisine Search Results Page



#### Meal Search Results Page



#### Meal Types Page



#### All Recipes Page



#### Thank You Page



#### Single Recipe Page



#### Null Search Results Page



## Features to implement

## Information Architecture

### Database

As this is the MS3 of the course a NoSQL database is used, this project employs the NoSQL database MongoDB. Inner arrays were utilised in the data structure in order to iterate through the items in a list with relative ease.

### Data Types

Below are the different data types in the MongoDB:

- ObjectId
- String
- Integer
- Array

### Data Structure 

Below is the data base collection:

Recipes Collection

| Title              | DB Key       | Form Validation                           | Data type |
| ------------------ | ------------ | ----------------------------------------- | --------- |
| Recipe ID          | _id          | None                                      | ObjectId  |
| Recipe Name        | recipe_name  | text, `pattern=".{3,}", maxlength="16"`   | string    |
| Description        | recipe_desc  | text, `pattern=".{70,}", maxlength="150"` | string    |
| Image              | image        | url, `pattern="(.*?)\.(jpg|png|gif)$`     | string    |
| Cuisine            | cuisine_name | text, `pattern=".{3,}", maxlength="14"`   | string    |
| Meal Type          | meal_type    | option="breakfast, lunch, dinner"         | string    |
| Calories           | calories     | number, max="9999"                        | integer   |
| Duration           | duration     | number, max="999"                         | integer   |
| Views              | views        | number, max="999"                         | integer   |
|                    |              |                                           |           |
| Preparation Steps  | recipe_prep  |                                           | array     |
| *Step 1*           | 0            | text, `maxlength="100"`                   | integer   |
| *Step 2.*..etc.    | 1            | text, `maxlength="100"`                   | integer   |
| *Step 20*          | 2            | text, `maxlength="100"`                   | integer   |
|                    |              |                                           |           |
| Recipe Ingredients | ingredients  |                                           | array     |
| *Step 1*           | 0            | text, `maxlength="18"`                    | integer   |
| *Step 2*....etc.   | 1            | text, `maxlength="18"`                    | integer   |
| *Step 20*          | 2            | text, `maxlength="18"`                    | integer   |
|                    |              |                                           |           |

[JSON file showing recipes collection structure](https://github.com/brianscan14/Gourmet_Grub/blob/master/data/schema/recipes.json) 

## Testing

Link to file

## Deployment

### Run project locally:

Using a suitable IDE (this project used Gitpod), make sure these are installed:

**[PIP](https://pip.pypa.io/en/stable/installing/), [Python 3](https://www.python.org/downloads/), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)**

**[MongoDB](https://docs.atlas.mongodb.com/getting-started/)** account running locally on your laptop.

1. Clone a copy of the [Github repo](https://github.com/brianscan14/Gourmet_Grub) by clicking the "clone" button, this will open the contents of the repo in a new workspace in the IDE. If Git is installed on your system, clone the repo with the following command: 

   - `git clone https://github.com/brianscan14/Gourmet_Grub.git`

2. Use the python virtual environment (VI) for the interpreter by entering the below command:

   - `pip install virtualenv`

3. Specify a path, for example one being created in the local directory called 'montypython' is:

   - `virtualenv mypython`

4. Activate the VI by running the following command:

   1. Mac OS / Linus:
      - `source montypython/bin/activate`
   2. Windows:
      - `montypython\Scripts\activate`

   *Note: your commands may differ, depends on IDE used, check [python](https://docs.python.org/3/library/venv.html) docs if you are running into issues*

5. Upgrade pip if it is needed:

   - `pip install --upgrade pip`

6. Install all the required modules with the command: 

   - `pip -r requirements.txt`

   *This will also later be needed to setup the heroku app*

7. In your local IDE create a file called env.py

8. in the env.py file create a MONGO_URI and MONGO_DB variable to link to the database. Call the database 'good_grubDB', with one collection called 'recipies'.

9. You can now run the app with the command:

    - `python3 app.py`

10. You can visit the site at:

    - `http://0.0.0.0:8080/`

### Heroku Deployment:

Follow the below instructions to deploy GoodGrub to heroku:

1. Create a Procfile in the terminal with the command:
   - `echo web: python app.py > Procfile`.
2. In bash, create requirements file with:
   - `pip3 freeze --local > requirements.txt`
3. If you ever use pip3 to install more packages after an initial deploy, you must re-generate the requirements.txt and commit/push to heroku
4. Using bash, commit everything:
   - `git add`
   - `git commit -m "<Commit Message>"`
5. In bash, push to GitHub using: 
   - `git push -u origin master`
6. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Make sure to set the region to Europe when naming it.
7. From the heroku dashboard of your new app, click on "Deploy" > "Deployment method" and select GitHub.
8. Confirm the linking of the heroku app to the correct GitHub repository.
9. Go to your Heroku account, find the app and open it. Click on setting and then "reveal config vars", set the following config vars:
   - Check [Mongo site](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/) for how to get the URI value

| **Key**   | **Value**                                                    |
| --------- | ------------------------------------------------------------ |
| DEBUG     | FALSE                                                        |
| IP        | 0.0.0.0                                                      |
| PORT      | 5000                                                         |
| MONGO_URI | mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority |

13. Click 'deploy' in the heroku dashboard
14. Ensure the master branch is selected in the 'manual deployment' section of the page and click 'deploy branch'

## Credits

### Media

### Code

### Acknowledgements 

### Disclaimer

This website and its content are for educational purposes only