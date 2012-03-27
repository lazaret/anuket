/** jQuerry plugins and functions **/


// activate the Twitter Boostrapt dropdown menus
$(function(){
    $('.dropdown-toggle').dropdown();}
);


// two choice radio buttons toggle for OR/AND search forms
$(function(){
    $('.toggle-and').click(function(){
        var parent = $(this).parents('.btn-group');
        $('.active',parent).removeClass('active');
        $('.btn-success',parent).removeClass('btn-success');
        $(this).addClass('btn-success');
        $(this).addClass('active');
    });
    $('.toggle-or').click(function(){
        var parent = $(this).parents('.btn-group');
        $('.active',parent).removeClass('active');
        $('.btn-success',parent).removeClass('btn-success');
        $(this).addClass('btn-success');
        $(this).addClass('active');
    });
});
