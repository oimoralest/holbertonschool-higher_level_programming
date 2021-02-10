/**
 * This script  toggles the class of the HTML tag HEADER when the user clicks on
 * the tag DIV#toggle_header
 */
$('DIV#toggle_header').click(() => {
  $('HEADER').toggleClass('green red');
});
