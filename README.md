# GourmetGrub

This Flask website was created as a platform for users to have the capability to create recipes of interest to them and post them to the site. They are also able to edit other recipes on the page or even delete them if they desire. This website uses a Mongo backend and visitors have the ability to search recipes already on the site,  it searches the MongoDB for strings in titles or ingredients that match the search input value. They can also swift through all the recipes present on the recipe with ease.

## UX

The main goal of this website is to offer users a quick and simple way to store and easily access cooking recipes. The pages are kept sleek and interactive so as to allow the user to easily navigate around all the recipes on the site.  The navbar at the top enkeeps with this team and allows the users to navigate to each page with ease, decreasing to a menu icon on smaller screen sizes.

The search bar on the index page is grand and bold, taking up the entire screen and giving the users an effective option of search recipes straight away. They can then search by meal times or cuisines if they are less certain for what they are searching for. All recipes are encompassed by BS4 cards which give the important information that a user may be looking for without having to click the actual recipe, e.g. "cooking time". 

### User Stories

1. As a new visitor to the website, I want to be easily navigate the site to find information I was looking for in one or two clicks when searching.
2. As a user, I want the different recipes to be presented to be in a tidy and easily readable manner when browsing them.
3. As a user, I want be able to find a particular recipe quickly by searching the word or a character string when I know what I want.
4. As a user, I want to be able to search by a food type or even meal type when I am less sure of what recipe I desire.
5. As a user I want to be able to know exactly what page I am currently on when browsing the site.
6. As a user, I want important pieces of info like cuisine type to be presented to me without having to click into it, when browsing through the different recipes.
7. As a user, I want the recipe I decide on to be easily readable and followable step by step when reading it.
8. As a user I want to be able to share this recipe on my social media platform when I am happy with the results of cooking it.
9. As a user contributing to the site, I expect a certain level of feedback to confirm that my work was submitted successfully, such as a thank you page.
10. As a user browsing the site, when there are no recipes matching my search I want a page returned confirming this, not just an empty page.
11. As a user, I want this site to be mobile/tablet friendly and be just as responsive as a desktop site would be when using this site on a mobile phone, as you more that likely would in a kitchen.

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

### Languages Used

- This project uses Python, Html, JavaScript & CSS programming languages.

### Front End

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
- [Jinja](http://jinja.palletsprojects.com/en/2.10.x/)
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

#### *Elements common to all pages*

##### Navbar:

The navbar can be divided into two type, small screen sizes and screen sizes above small. The pages consist of; home/search, cuisine, meals, add recipe and all recipes. There is a search icon on both screens for easier interaction with the user, when hovered over it will change colour to signify it is a clickable option. The nav header is the name of the page and this is in bolder and larger font to notify the users of this fact, when clicked it will bring them back to the home page. It is positioned at the top of the page for better recipe viewing experience, the 'active' class is also added to the current page by using jinja. The user can easily be returned to the navbar's location by clicking the up arrow which brings them to the top of the page.

*Small screen*:

The navbar is a burger icon with a vertical collapsible list of the pages when clicked to easily navigate the website. The pages pop done in a list form under the header and the user can can click one of these and they are brought to said page. The search icon is placed beside the header on this screen so the user can also call the search bar overlay from whatever page they are on to navigate recipes.

*Larger screen:*

For bigger screens the navbar is displayed as a list of titles of the pages in a horizontal fashion. Again, the overlay for searching can be called by clicking the search icon. However in larger screens this icon is pushed to the right corner of the nav. 

##### Footer:

The footer is a simple line of muted text at the bottom of the page that signifies to the users a to who the page was created by. It is fixed to the bottom of the page with CSS positioning. 

**Scroll Top button**

This button appears on all screen sizes but is mainly for use with the smaller screens as a handy means for the user to scroll to the top of the screen when clicked. It will appear after 80px of scrolling as an 'up' directional arrow which will allow the user to know its function. Once clicked it bring you back to the start of the page. It also changes colour on hover to notify the user that it is clickable and uses CSS to position itself at the bottom right of the screen, with a higher z-index to make sure it isn't covered by any html content.

**Search Icon**

The navbar uses a search icon in the shape of a magnifying glass which when clicked will call an overlay that covers the whole page. This overlay has less opacity to still show the user the page they were on, but in the 'background'. The overlay itself keeps to the pages colour scheme and consists of a search bar with a simple search button. This search bar searches the DB for recipe names or ingredients that match the sting searched.

**Color Scheme**

The pages utilises the below colour scheme across the entire page, there are slight variations on buttons or icons hover but mainly just opacity changes. This scheme stemmed from the [burger platter](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/) picture used as the body's background and is most apparent on the home page. [Coolors](https://coolors.co/) website was used for this where the picture is uploaded to the website and a colour scheme is generated form it. Items such as the spinach are used for the green colour for 'success' buttons and the red of the onions for the 'delete' button. This scheme is employed throughout the website and gives the user a more pleasant and immersive viewing experience. 

#### Home Page

##### Hero Image

The home page is covered by an image of a burger serving on a platter gotten from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/). It serves a purpose as the user immediately knows what the purpose of this site is from their initial arrival. It is used as the background picture for all pages and signifies the commencement of the website viewing experience for the user.

##### Search Bar

The search bar used here is similar in functionality to the one used in the navbar. It takes up a larger portion of the page and serves the purpose where the user can just search for a recipe straight off the bat if they do not wish to browse the page and just find exactly what they are looking for. Placeholder text is there to tell the user to 'search' and a button to initiate it. This will send the signal to the DB to search recipe names and ingredients that match the string and redirect to a results page. Regex is used to search for any matches of the string, not just exact matches, e.g. search for "chick" will return "chicken curry" matches or a stir fry that has "chicken" in its ingredients.

#### Add/Edit recipe page

speellcheck, recipe meal tye is slected onthe edit page, delete button too

#### Cuisines Page

The Cuisines page is a page which display all of the cuisines of the recipes that are in the DB at that time. The 'distinct 'method is used here to find the distinct values for the field across the collection, thereby avoiding having duplicates of them same field. The cards are displayed in a vertical list format and consist of the cuisine name as the title and a button which allows users to explore more recipes which contain this cuisine. By clicking this button the user is redirected to a cuisine results page which list all the recipes in the DB of this particular cuisine.

#### Meal Search page

This page is a simple container that contains the 3 meal options "breakfast, lunch and dinner" in a dropdown. There is a title to denote that the user can search recipes by their meal time type and the disabled select option tells the user to pick an option. Once this dropdown is clicked the the user is given the 3 options, when they select one they are redirected to the meal results page which contains the recipes that match this meal type. 

#### Cuisine/Meal/Search-bar results Page

The page that the user is redirected to after clicking the aforementioned cuisine, meal type or search bar input. This page consists of cards listed in rows which match the search criteria chosen prior. The card body itself changes in opacity/colour slightly when hovered over to tell the user they are on the card, with a view button to see the recipe in full which redirects them to the single recipe page. Within these cards there are little nuggets of information of which might assist the user in deciding which recipe they want to pick. The title is the recipe title and there is also a picture accompanied with it that is taken from the URL image field.

There is then a short description which is given a certain height and the text is hidden with CSS if it overflows this div. Below that then simply in bold the cuisine type is mentioned and views. The views for these cards are gotten by incrementing the 'views' field by and integer, '1' every time the recipe is viewed by itself. This is then relayed to the HTML by using jinja, which lets the user know its popularity. Jinja is also used to have the searched cuisine, meal type or search bar input as the title of the container just to remind the user what they are looking at. The cards are sorted in a descending order going by the 'views' field in the DB to show the most popular ones first.

#### All Recipes Page

This page uses a vertical version of the cards mentioned in the results pages, displaying the same information but in a vertical manner as the cards themselves are displayed as columns as opposed to rows.   On a smaller screen the cards are listed in a vertical format with the columns getting full width, one card displayed at a time and they can e scrolled through.  and The cards themselves highlight the same way as the results cards, only the views and cuisine type are displayed in muted text in the footer, with the views floated to the right. The user can then select the recipe by clicking on the button and is redirected to this recipe's single page.

Pagination is utilised on this page, the DB is accessed in the backend in a manner which means that only 6 recipes are loaded and displayed at a time to improve performance. The user can then click which page they desire to go to, with the page selected having the 'active' class on the pagination and unselected pages are a different colour. The recipes are again displayed in a descending order starting from the most popular ones to the least popular with the sort method, using the 'views' field.

#### Single Recipe Page

Here the recipe is displayed in full to the user and shows all its details. The title shows the name of the recipe, with the ingredients right aligned and listed on the left, and the image of the recipe on the right side. Some summary statistics are then shown of this particular which might be helpful to the user. They consist of "calories, duration and number of ingredients", the first two are fields form the DB but the ingredients number is gotten form getting the length of the number of items in the filed by using jinja. 

The steps are then outlined and separated by bottom borders, giving the user easy steps to follow in a sequence to created the recipe. Social media buttons are then positioned beside each other at the bottom of the page which allows the user to share the recipe on social media platforms if they wish to. This is then followed by an edit button which redirects the user to the edit page when clicked. On a smaller screen all items in the recipe page are given full screen width, with the summary stats under the picture still dividing their container in 3 parts.

#### Thank You Page

This page was created as a result from the user stories as a means to let the user know that the recipe they have just created has been entered onto the page correctly. It consists of a title saying 'thank you for adding the below recipe' and the proceeds to showcase the full recipe as seen in the single recipe page. This is a means of giving feedback to the user that they successfully added a recipe and serves its purpose well.

#### Error 404 Page

If any 404 errors occur while browsing the website the user will be directed to an 'error 404' page. This simply says to the user that some error has occurred with a heading stating this, and some smaller text explaining it. Instead of them having to use a back button on the browser they can just click the 'return to home page' button which appears, encouraging the user to stay on the webpage.

#### Null Result page

This page is for a more defensive methodology and is what the user is redirected to if there are no results for their search criteria or indeed no recipes in the collection at all. It is a simple container a with a header saying that there are no results, and some light hearted text offering the user the chance to contribute to the DB and create a recipe by clicking the button, in turn redirecting them to the add recipes page.

## Features to implement

login

rating/likes sytem

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
| Image              | image        | url, `pattern="(.*?)\.(jpg/png/gif)$`     | string    |
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

[Link to testing.md file](https://github.com/brianscan14/Gourmet_Grub/blob/master/testing/TESTING.md)

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

   *Note: your commands may differ, depends on IDE used, check [python](https://docs.python.org/3/library/venv.html) docs if you are running into issues*

4. Upgrade pip if it is needed:

   - `pip install --upgrade pip`

5. Install all the required modules with the command: 

   - `pip -r requirements.txt`

   *This will also later be needed to setup the heroku app*

6. In your local IDE create a file called env.py

7. in the env.py file create a MONGO_URI and MONGO_DB variable to link to the database. Call the database 'good_grubDB', with one collection called 'recipies'.

8. You can now run the app with the command:

    - `python3 app.py`

9. You can visit the site at:

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