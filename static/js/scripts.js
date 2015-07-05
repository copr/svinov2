$(document).ready(function(){ 
  var touch = $('#resp-menu');
  var menu = $('.menu');
 
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

//  $('.border').css('width', '100%').css('width', '+=1px'); // pokud nefunguje css calc 

});

function handleCalendar() {
    var calendar = new Calendar();
    document.googleIds.forEach(function(id) {
	calendar.loadEvents(id);
    });
    if (!document.googleIds.length) {
	$('.calendar img').remove();
    }
}

function redirect(url) {
    window.location.href = url;
}
