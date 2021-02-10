/**
 * This script updates the text of the HTML tag HEADER to “New Header!!!” when
 * the user clicks on DIV#update_header
 */
$('DIV#update_header').click(() => {
  $('HEADER').text('New Header!!!');
});
