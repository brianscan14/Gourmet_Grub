// to make all entries in the add recipes form as caps
// form input corrections https://stackoverflow.com/questions/19606178/make-first-character-of-each-word-capital-in-input

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

// testing the add form function

$(document).ready(function() {
    let max_fields      = 20;
    let wrapper         = $(".container1");
    let add_button      = $(".add_form_field");
    let x = 1;

    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            $(wrapper).append('<div><input type="text" name="recipe_prep"/><a href="#" class="delete">Delete</a></div>'); //add input box
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
    var max_fields      = 10;
    var wrapper         = $(".container2");
    var add_button      = $(".add_form_feed");
 
    var x = 1;
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