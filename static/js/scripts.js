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

    // $('.to-clamp').succinct({
    // 	size:350
    // });
    // var elements0 = document.getElementsByClassName('to-clamp-title');
    var elements1 = document.getElementsByClassName('to-clamp');
    var elements2 = document.getElementsByClassName('to-clamp-big');

    // for (var i=0; i < elements0.length; i++) {
    // 	$clamp(elements0[i], {clamp: 2});
    // }

    for (var i=0; i < elements1.length; i++) {
	$clamp(elements1[i], {clamp: 8});
    }
    
    for (var i=0; i < elements2.length; i++) {
    	$clamp(elements2[i], {clamp: 10});
    }

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
    calendar.loadEvents(document.googleIds, 7);
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
