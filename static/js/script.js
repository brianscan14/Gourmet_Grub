// To make all entries in the add recipes form as caps form input corrections 
// https://stackoverflow.com/questions/19606178/make-first-character-of-each-word-capital-in-input


jQuery.noConflict();
jQuery(document).ready(function($) {
  $('.form-caps').keyup(function(event) {
    let textBox = event.target;
    let start = textBox.selectionStart;
    let end = textBox.selectionEnd;
    textBox.value = textBox.value.charAt(0).toUpperCase() + textBox.value.slice(1).toLowerCase();
    textBox.setSelectionRange(start, end);
  });
});

/**
 * @function
 * This anonymous function adds an extra form field for the recipe prep and ingredients steps
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
            $(wrapper).append('<div><input type="text" name="recipe_prep"/><a href="#" class="delete">Delete</a></div>');
        }
        else
        {
            alert('You Reached the limit of fields!')
        }
        });
        
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
            $(wrapper).append('<div><input type="text" id="ingredients" name="ingredients"/><a href="#" class="delete">Delete</a></div>');
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

$(document).ready(function() {

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
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

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
  document.getElementById("overlaySearchBar").style.width = "100%";
}

function openSearchBarSmall() {
  document.getElementById("overlaySearchBar").style.width = "100%";
}

function closeSearchBar() {
  document.getElementById("overlaySearchBar").style.width = "0%";
}

$('#navSearchOpen').click(function(){
       openSearchBar();
    });

$('#navSearchOpenSmall').click(function(){
       openSearchBarSmall();
    });

$('#navSearchClose').click(function(){
       closeSearchBar();
    });

function goBackPage() {
  window.history.back();
}

$('#backButton').click(function(){
       goBackPage();
    });