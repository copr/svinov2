var React = require('react');
var Error = require('./Error');
var Udalost = event;
var UdalostPole = eventField;


module.exports = React.createClass({
    getInitialState: function () {
	return {
	    name: "",
	    empty: false,
	    ticketNumber: "",
	    phone: "",
	    errors: [],
	    note:"",
	    conditions: false,
	}
    },
    nameChange: function (e) {

	this.setState({ name: e.target.value });

    },
    surnameChange: function (e) {
	this.setState({ surname: e.target.value });
    },
    phoneChange: function (e) {
	this.setState({ phone: e.target.value });
    },
    emailChange: function (e) {
	this.setState({ email: e.target.value });
    },
    noteChange: function (e) {
	this.setState({ note: e.target.value });
    },
    conditionsChange: function(e) {
	if (this.state.conditions) {
	    this.setState({ conditions: false });
	} else {
	    this.setState({ conditions: true });
	}
    },
    ticketChange: function (e) {
	if (e.target.value < 1 || e.target.value === "") {
	    this.setState({ ticketNumber: 1 })
	} else {
	    this.setState({ ticketNumber: e.target.value });
	}
    },
    validate: function (e) {
	var val = e.target.value;
	//  classList neni podporovany v IE 
	// 	e.target.parentElement.classList.remove('has-success', 'has-error','empty'); nefachci v IE
	$(e.target.parentElement).removeClass("has-success has-error empty");
	if (val) {
	    $(e.target.parentElement).addClass("has-success");
	    // e.target.parentElement.classList.add('has-success')
	} else {
	    $(e.target.parentElement).addClass("has-error empty");
	    // e.target.parentElement.classList.add('has-error','empty');
	}
    },
    submit: function (e) {
	// je to hlavne kvuli resubmitu kdyz to nekdo zmackne rychle
	// tak by se to vickrat poslalo
	if (!$("input:checkbox").prop('checked')) {
	    e.preventDefault();
	    alert('Musíte souhlasit s obchodníma podmínkama');
	    return false;
	}
	$("form button").prop('disabled', true);
	if (this.state.phone.replace(' ', '').length < 13) {
	    console.log(this.state.phone);
	    e.preventDefault();
	    alert('Špatně zadané číslo');
	    $("form button").prop('disabled', false);
	    return false;
	}
	// kdyz je nejaky prazdny tak se musi povolit submit znovu
	k = true;
	$("div.empty").each(function (i) {
	    console.log($("div.empty"));
	    e.preventDefault();
	    alert("Vyplňte všechna povinná pole!");
	    $("form button").prop('disabled', false);
	    k = false;
	    return false;
	});
	if (!k) {
	    return;
	}
	// kdyz je nejaky nevalidni tak se musi povolit submit znovu
	$("input").each(function(i) {
	    console.log(i);
	    if (!$("input")[i].validity.valid) {
		$("form button").prop('disabled', false);
		return false;
	    }
	});
	$('form').submit();
    },
    render: function () {
	// proc onBlur?
	return (
	    <div>
		<div>
		    <h3>Událost: { Udalost[0].fields.name}</h3>
		    <h3>Cena: {this.state.ticketNumber * Udalost[0].fields.price} Kc</h3>
		</div>
		<form action={ window.location.href } method="post" className="col-xs-6 col-xs-offset-3" id="idecko">
		    <div className="form-group empty">
			<input onChange={this.nameChange} onBlur={this.validate} name="name"
			       value={this.state.name} type="text" className="form-control" placeholder="Jmeno" />
			<Error field={this.state.empty} />
		    </div>
		    <div className="form-group empty">
			<input onChange={this.surnameChange} isValid="false" onBlur={this.validate} name="surname"
			       value={this.state.surname} type="text" className="form-control" placeholder="Prijmeni" />
		    </div>
		    <div className="form-group empty">
			<input onChange={this.phoneChange} isValid="false" onBlur={this.validate} type="tel" name="phone_number"
			       value={this.state.phoneNumber} className="form-control bfh-phone" data-format="+420 ddd ddd ddd" placeholder="Telefon" />
		    </div>
		    <div className="form-group empty">
			<input onChange={this.emailChange} isValid="false" onBlur={this.validate} type="email" name="email"
			       value={this.state.email} className="form-control" placeholder="Email" />
		    </div>
		    <div className="form-group">
			<input onChange={this.ticketChange} isValid="false" onBlur={this.validate} type="number" name="number_of_tickets"
			       value={this.state.ticketNumber} className="form-control" placeholder="Pocet listku" />
		    </div>
		    <div className="form-group"> 
			<textarea form="idecko" onChange={this.noteChange} isValid="true" name="note"
				  value={this.state.note} className="form-control" placeholder="Poznámka - nepovinné" /> 
		    </div>
		    <div className="form-group">
			<input form="idecko" onChange={this.conditionsChange} type="checkbox" isValid="false" name="conditions"
			       value="conditions" checked={this.state.conditions}>
			    <a href="http://www.sdhsvinov.cz/Sbor/VOPeTicket/">Přečetl jsem si a souhlasím s všeobecnými obchodními podmínkami</a>
			</input>
		    </div>

		    <button type="submit" onClick={this.submit} className="btn-success">Odeslat</button>
		</form>
	    </div>
	)
    }
});
