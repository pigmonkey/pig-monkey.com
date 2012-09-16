$(document).ready(function() {
    // Hide monthly archives and posts.
    $('#post-archive .monthly-archive').hide();
    $('#post-archive .monthly-posts').hide();
    // If a year link is clicked, toggle the year's months.
    $('#post-archive .year').click(function() {
        $(this).parent().next('#post-archive .monthly-archive').slideToggle(400);
        return false;
    });
    // If a month link is clicked, toggle the month's posts.
    $('#post-archive .month').click(function() {
        $(this).parent().next('#post-archive .monthly-posts').slideToggle(400);
        return false;
    });
});
