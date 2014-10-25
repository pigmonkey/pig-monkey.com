$(document).ready(function() {
    $('<a href="#" title="Toggle navigation menu" id="toggle-nav"><img src="http://pig-monkey.com/static/images/nav.png" alt="#"></a>').insertAfter('.site-title');
    $('#toggle-nav').css('display', 'none');
    function hideNav(){
        // Hide the navigation menu if the viewport is less than X.
        if($('#top nav li:first-child').css('float') == 'none') {
            $('#top nav').slideUp(900);
            $('#toggle-nav').fadeIn(900);
        // Otherwise, show the navigation menu.
        } else {
            $('#top nav').show();
            $('#toggle-nav').css('display', 'none');
        }
    }


    hideNav();
    // Hide (or show) the navigation on window resize.
    $(window).resize(hideNav);

    // Toggle the navigation.
    $('a#toggle-nav').click(function() {
        $('#top nav').slideToggle(400);
        return false;
    });
});
