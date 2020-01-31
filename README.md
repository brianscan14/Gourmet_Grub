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

to be added....soon

## Technologies (add links)

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
- More...

### Back End

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Python framework used to build the app.
- [Pymongo](https://api.mongodb.com/python/current/)
  - Sends the queries to the DB.
- more ....
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



## Testing

Link to file

## Deployment

### Run project locally:

Using a suitable IDE, stall (this project used Gitpod):

**PIP, Python 3, Git**, and a **MongoDB** account running locally on your laptop.

1. Clone a copy of the Github repo (Github url) by clicking the "clone" button, this will open the contents of the repo in a new workspace in the IDE. If Git is installed on your system, clone the repo with the following command: git clone "link to my repo"
2. Use the python virtual environment for the interpreter by entering the below command: pyth**on3 "name of your app file".py - incorrect?**
3. install all the required modules with the command: pip -r requirements.txt, this will also later be needed to setup the heroku app
4. In your local IDE create a file called env.py
5. in the env.py file create a MONGO_URI and MONGO_DB variable to link to your own database. Call the DB good_grubDB, with one collection called recipes.
6. You can now run the app with the command python3 app.py
7. You can visit the site at 

### Heroku Deployment:

1. Install Heroku using bash:
   nvm i v8
   npm install -g heroku
2. In bash, log into Heroku:
   heroku login -i
3. In bash, create a new app (replace <app_name> with a name of your own. It must be unique, so put your initials or nickname before it):
   heroku create <app_name>
4. New remote will be added. Check with the following in bash:
   git remote -v
5. Install gunicorn by typing the following in bash:
   pip3 install gunicorn
6. Create a name file named "Procfile" (without the quotes, and the first P must be uppercase).
7. Open Procfile in the editor and add the following line to it, and save. Replace the <your python file name without the .py> with the name of the file that holds the Flask app:
   web gunicorn <your python file name without .py>:app
8. In bash, create requirements file with:
   pip3 freeze --local > requirements.txt
9. If you ever use pip3 to install more packages after an initial deploy, you must re-generate the requirements.txt and commit/psuh to heroku
10. Using bash, commit everything:
    git add .
    git commit -m "<Commit Message>"
11. In bash, push to heroku using git push heroku master
12. Go to your Heroku account, find the app and open it. Click on setting and then "reveal config vars", set the following config vars:
    1. IP = 0.0.0.0
    2. PORT = 5000
    3. MONGO_URI = mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority

#### *Set up environment variables *

Make sure you are in the Heroku CLI (step 2 above).

1. To set a config variable, use:

   heroku config:set WHATEVER=VALUE

   So for example, to set the MONGO_URI:

   heroku config:set MONGO_URI= mongodb+srv://root:random123

2. To check all the config variables you have, use:
   heroku config 

## Credits

### Media

### Code

### Acknowledgements 

### Disclaimer

This website and its content are for educational purposes only