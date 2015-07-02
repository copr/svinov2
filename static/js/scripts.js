$(document).ready(function(){ 
  var touch   = $('#resp-menu');
  var menu  = $('.menu');
 
  $(touch).on('click', function(e) {
    e.preventDefault();
    menu.slideToggle();
  });
  
  $(window).resize(function(){
    var w = $(window).width();

    // breakpoint
    if(w > 767 && menu.is(':hidden')) {
      menu.removeAttr('style');
    }
  });

  $('.to-clamp').succinct({
      size:450
  });
});

function handleCalendar() {
    var calendar = new Calendar();
    document.googleIds.forEach(function(id) {
	calendar.loadEvents(id);
    });
}

function redirect(url) {
    window.location.href = url;
}
