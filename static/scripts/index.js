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
