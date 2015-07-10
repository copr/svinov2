function Calendar() {
    gapi.client.setApiKey('AIzaSyDZVBv9Ralzvv-bbdEuWbMQCcrr4B-cYwM');
    this.events = Array();
}

Calendar.prototype.loadEvents = function(calendarId, maxResults) {
    var request = gapi.client.request({
	'path': 'calendar/v3/calendars/' + calendarId + '/events',
	'params': {
	    'maxResults': 7,
	    'orderBy': 'startTime',
	    'singleEvents': true,
	    'timeMin': (new Date()).toISOString(),
	    'showDeleted': false
	}
    });
    request.then(function(resp) {
	resp.result.items.forEach(function(i) {
	    if (typeof i.start.date === 'undefined') {
		var date = new Date(i.start.dateTime);
	    } else {
		var date = new Date(i.start.date);
	    }
	    $('.calendar img').remove();
	    var li = $('<li></li>').text(date.getDate() + '. ' + (parseInt(date.getMonth()) + 1) + '. ' + (parseInt(date.getFullYear())) +
				' | ' + i.summary)
		          .click(function() {window.open(i.htmlLink);})
                          .appendTo('.calendar ul');
	    var a = $("<a></a>", {'href': i.htmlLink, 'target': '_blank'}).appendTo(li);
	    $('<i></i>', {'class': 'fa fa-info'}).appendTo(a);
	    // $('.calendar ul').append("<li>" + date.getDate() + '. ' + (parseInt(date.getMonth()) + 1) + '. ' + 
	    // 			     (parseInt(date.getFullYear())) + ' | ' + i.summary + /*' | ' + i.location + */ 
	    // 			     '<a href=' + i.htmlLink + " target='_blank'><i class='fa fa-info'</a>" + '</li>');
	});
    });
};


Calendar.prototype.getEvents = function() {
    return this.events.sort(function(a,b) {
	if (typeof a.start.date === "undefined") {
	    aa = new Date(a.start.dateTime);
	} else {
	    aa = new Date(a.start.date);
	}
	if (typeof b.start.date === "undefined") {
	    bb = new Date(b.start.dateTime);
	} else {
	    bb = new Date(b.start.date);
	}
	return aa < bb;
    });
}
