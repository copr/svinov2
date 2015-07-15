$(document).ready(function(){ 
  var touch = $('#resp-menu');
  var menu = $('ul.menu');
 
  $(touch).on('click', function(e) {
    e.preventDefault();
    if (!menu.hasClass('active-menu')) {
      menu.addClass('active-menu');
    } else {
      menu.removeClass('active-menu');
    }
  });
  
  $(window).resize(function(){
    var w = $(window).width();

    // breakpoint
    if(w > 767 && menu.is(':hidden')) {
      menu.removeAttr('style');
    }
  });

    $('.to-clamp').succinct({
	size:350
    });


  $('.menu li.section').hover(function() {
      $(this).next().addClass("hiden");
      $(this).prev().addClass("hiden");
  }, function() {
      $(this).next().removeClass("hiden");
      $(this).prev().removeClass("hiden");
  });


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

function getTime(event) {
    if (typeof event.start.dateTime === 'undefined') {
	return '';
    }
    date = new Date(event.start.dateTime);
    hours = date.getHours();
    minutes = date.getMinutes();
    if (parseInt(minutes) < 10) {
	minutes = "0" + minutes;
    }
    return hours + ":" + minutes;
}
