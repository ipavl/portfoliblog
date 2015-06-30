/**
 * Highlight active navbar item based on path
 */
var highlight_menu = function(path) {
    $('.nav li').removeClass('active');
    $('.nav li:has(a[href="' + path + '"])').addClass('active');
};