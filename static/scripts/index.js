$(document).ready(function() {
    // execute a GET request to Status API
    $.get('http://localhost:5001/api/v1/status/', function(data) {
        // if the request is successful
        if (data.status === 'OK') {
            // add the class available to the DIV#api_status
            $('DIV#api_status').addClass('available');
        } else {
            // remove the class available to the DIV#api_status
            $('DIV#api_status').removeClass('available');
        }
    });
});

$(document).ready(function() {
    // Target the element where you want to display the recipes
    var recipesList = $('#recipes-list');

    // AJAX request
    $.ajax({
        url: '/recipes', // URL of the Flask route that fetches the API data
        method: 'GET',
        success: function(data) {
            // Assuming data is a list of recipe objects
            data.forEach(function(recipe) {
                recipesList.append('<li><a href="' + recipe.uri + '">' + recipe.label + '</a></li>');
            });
        }
    });
});
