/**
* To make all entries in the add recipes form as caps form input corrections 
* https://stackoverflow.com/questions/19606178/make-first-character-of-each-word-capital-in-input
*/

jQuery.noConflict();
jQuery(document).ready(function($) {
  $('.form-caps').keyup(function(event) {
    let textBox = event.target;
    let start = textBox.selectionStart;
    let end = textBox.selectionEnd;
    // converts first letter of string to uppercase and the rest there after are lowercase
    textBox.value = textBox.value.charAt(0).toUpperCase() + textBox.value.slice(1).toLowerCase();
    textBox.setSelectionRange(start, end);
  });
});

/**
 * @function
 * This anonymous functions adds an extra form field for the recipe prep and ingredients steps
 * gotten from: https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form
 */

$(document).ready(function() {
    let max_fields      = 20;
    let wrapper         = $(".container1");
    let add_button      = $(".add_form_field");
    let x = 1;

    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            // when the add button is cliked below html content will get added for each click, delete button included
            $(wrapper).append('<div class="centering-text py-3">'+
            '<input class="bg-transparent form-control-recipe step-form"'+
            'maxlength="100" type="text" name="recipe_prep" id="recipe_prep">'+
            '<button class="delete btn btn-danger step-btn">'+
            '<i class="far fa-trash-alt"></i></button></div>');
        }
        else
        {
            alert('You Reached the limit of fields!')
        }
    });
        // delete button to remove the form input when clicked
        $(wrapper).on("click",".delete", function(e){
        e.preventDefault(); $(this).parent('div').remove(); x--;
        })
});

$(document).ready(function() {
    let max_fields      = 20;
    let wrapper         = $(".container2");
    let add_button      = $(".add_form_feed");
 
    let x = 1;
    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            $(wrapper).append('<div class="centering-text py-3">'+
            '<input class="bg-transparent form-control-recipe step-form"'+
            'maxlength="18" type="text" id="ingredients" name="ingredients">'+
            '<button class="delete btn btn-danger step-btn">'+
            '<i class="far fa-trash-alt"></i></button></div>');
        }
        else
            {
        alert('You Reached the limits')
        }
    });
    
    $(wrapper).on("click",".delete", function(e){
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

/**
 * @scrollToTop
 * This function shows the button when the user scrolls down 80px from top of document
 * @topPage
 * This function scrolls to the top of the page when the button is clicked
 */

let mybutton = document.getElementById("topBtn");

window.onscroll = function() {scrollToTop()};

function scrollToTop() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    mybutton.style.display = "block";
        } else {
    mybutton.style.display = "none";
        }
}

function topPage() {
    document.body.scrollTo({top: 0, behavior: 'smooth'});
    document.documentElement.scrollTo({top: 0, behavior: 'smooth'});
    }

$(document).ready(function() {
    $('#topBtn').click(function(){
        topPage();
    });
});

/**
 * @openSearchBar
 * These functions open the nav search bar by increasing the width of the overlay
 * @closeSearchBar
 * This function closes the nav search bar by decreasing the width of the overlay
 */

function openSearchBar() {
    console.log('called');
    let searchBar = document.getElementById("overlaySearchBar");
    if (searchBar) {
        searchBar.style.width = "100%";
    }
    }

function openSearchBarSmall() {
    document.getElementById("overlaySearchBar").style.width = "100%";
    }

function closeSearchBar() {
    document.getElementById("overlaySearchBar").style.width = "0%";
    }

$(document).ready(function() {

$('#navSearchOpen').click(function(){
       openSearchBar();
    });

$('#navSearchOpenSmall').click(function(){
       openSearchBarSmall();
    });

$('#navSearchClose').click(function(){
       closeSearchBar();
    });
});

/**
 * @goBackPage
 * This function target the back button and just goes back one page
 * in the browser's history when clicked
 */

$(document).ready(function() {

function goBackPage() {
    window.history.back();
    }

$('#backButton').click(function(){
       goBackPage();
    });
});