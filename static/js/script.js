// to make all entries in the add recipes form as caps
// form input corrections https://stackoverflow.com/questions/19606178/make-first-character-of-each-word-capital-in-input

jQuery.noConflict();
jQuery(document).ready(function($) {
  $('.form-caps').keyup(function(event) {
    var textBox = event.target;
    var start = textBox.selectionStart;
    var end = textBox.selectionEnd;
    textBox.value = textBox.value.charAt(0).toUpperCase() + textBox.value.slice(1).toLowerCase();
    textBox.setSelectionRange(start, end);
  });
});

// testing the add form function

$(document).ready(function() {
    var max_fields      = 20;
    var wrapper         = $(".container1");
    var add_button      = $(".add_form_field");
 
    var x = 1;
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