$(document).ready(function() {
    // Hide yearly archives.
    $('#archives .article-archive').hide();
    // If a year link is clicked, toggle the year's archives.
    $('#archives .year').click(function() {
        $(this).parent().children('.article-archive').slideToggle(400);
        return false;
    });
});
