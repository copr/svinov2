

function Calendar() {
    gapi.client.setApiKey('AIzaSyDZVBv9Ralzvv-bbdEuWbMQCcrr4B-cYwM');
    this.events = Array();
}

Calendar.prototype.loadEvents = function(calendarIds, maxResults)  {
    if(typeof calendarIds === 'undefined') {
	$('.calendar img').remove();
	return;
    }
    var requests = Array();
    
    for( i = 0; i < calendarIds.length; i++) {
	requests[i] = gapi.client.request({
	    'path': 'calendar/v3/calendars/' + calendarIds[i] + '/events',
	    'params': {
		'maxResults': maxResults,
		'orderBy': 'startTime',
		'singleEvents': true,
		'timeMin': (new Date()).toISOString(),
		'showDeleted': false
	    }
	});
    }
    var batch = gapi.client.newBatch();
    for ( var i = 0; i < calendarIds.length; i++) {
	batch.add(requests[i], i);
    }
    batch.then(function(resp) {	
	handleResponse(resp, calendarIds.length);
    }, function() {
	console.log('selhali jsme');
    });
}

function handleResponse(resp, length) {
    events = Array();
    for (var id in resp.result) {
	events = events.concat(resp.result[id].result.items);
    }
    events.sort(function(a,b) {
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
	return aa > bb;
    });
    $('.calendar img').remove();
    addEventsToDom(events, 7);
}

function addEventsToDom(events, numOfResults) {
    var sliced = events.slice(0, numOfResults);
    sliced.forEach(function(ev) {
	if (typeof ev.start.date === 'undefined') {
	    var date = new Date(ev.start.dateTime);
	} else {
	    var date = new Date(ev.start.date);
	}
	var rectangle = $('<div></div>').addClass('rectangle');
	var span = $('<span></span>').text(date.getDate() + '. ' + (parseInt(date.getMonth()) + 1) + '. ' + date.getFullYear()
				     + ' ' + getTime(ev) + ' | ' + ev.summary);
	var li = $('<li></li>')
	    .append(span)
	    .click(function() {window.open(ev.htmlLink);})
	    .appendTo('.calendar ul');
	$('.alt-calendar').removeClass('hidden');
	// rectangle.prependTo(li);
	var a = $("<a></a>", {'href': ev.htmlLink, 'target': '_blank'}).appendTo(li);
	$('<i></i>', {'class': 'fa fa-info'}).appendTo(a);
    });
}

Calendar.prototype.loadEventsss = function(calendarIds, maxResults) {
    if (typeof calendarIds === 'undefined') {
	this.events.sort(function(a,b){
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
	    return aa > bb;
	});
	$('.calendar img').remove();
        this.events.forEach(function(i) {
	    if (typeof i.start.date === 'undefined') {
		var date = new Date(i.start.dateTime);
	    } else {
		var date = new Date(i.start.date);
	    }
	    var li = $('<li></li>').text(date.getDate() + '. ' + (parseInt(date.getMonth()) + 1) + '. ' + date.getFullYear()
					 + ' ' + getTime(i) + ' | ' + i.summary)
		.click(function() {window.open(i.htmlLink);})
		.appendTo('.calendar ul');
	    var a = $("<a></a>", {'href': i.htmlLink, 'target': '_blank'}).appendTo(li);
	    $('<i></i>', {'class': 'fa fa-info'}).appendTo(a);
	});
	return;
    }
    calendarId = calendarIds.pop();
 
    var f1 = this.addEvent;
    var f = this.loadEvents;
};

Calendar.prototype.addEvent = function(i) {
    this.events.push(i);
}
    


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
