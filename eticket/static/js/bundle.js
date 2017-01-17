/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	/** @jsx React.DOM */'use strict'

	/*
	 * Entry point for MSL dashboard client, it just starts the app.
	 */

	var Switcher = __webpack_require__(1);

	ReactDOM.render(React.createElement(Switcher, null), document.getElementById('content'));


/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

	/** @jsx React.DOM */var React = __webpack_require__(2);
	var Error = __webpack_require__(3);
	var Udalost = event;
	var UdalostPole = eventField;


	module.exports = React.createClass({displayName: "module.exports",
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
		    React.createElement("div", null, 
			React.createElement("div", null, 
			    React.createElement("h3", null, "Událost: ",  Udalost[0].fields.name), 
			    React.createElement("h3", null, "Cena: ", this.state.ticketNumber * Udalost[0].fields.price, " Kc")
			), 
			React.createElement("form", {action:  window.location.href, method: "post", className: "col-xs-6 col-xs-offset-3", id: "idecko"}, 
			    React.createElement("div", {className: "form-group empty"}, 
				React.createElement("input", {onChange: this.nameChange, onBlur: this.validate, name: "name", 
				       value: this.state.name, type: "text", className: "form-control", placeholder: "Jmeno"}), 
				React.createElement(Error, {field: this.state.empty})
			    ), 
			    React.createElement("div", {className: "form-group empty"}, 
				React.createElement("input", {onChange: this.surnameChange, isValid: "false", onBlur: this.validate, name: "surname", 
				       value: this.state.surname, type: "text", className: "form-control", placeholder: "Prijmeni"})
			    ), 
			    React.createElement("div", {className: "form-group empty"}, 
				React.createElement("input", {onChange: this.phoneChange, isValid: "false", onBlur: this.validate, type: "tel", name: "phone_number", 
				       value: this.state.phoneNumber, className: "form-control bfh-phone", "data-format": "+420 ddd ddd ddd", placeholder: "Telefon"})
			    ), 
			    React.createElement("div", {className: "form-group empty"}, 
				React.createElement("input", {onChange: this.emailChange, isValid: "false", onBlur: this.validate, type: "email", name: "email", 
				       value: this.state.email, className: "form-control", placeholder: "Email"})
			    ), 
			    React.createElement("div", {className: "form-group"}, 
				React.createElement("input", {onChange: this.ticketChange, isValid: "false", onBlur: this.validate, type: "number", name: "number_of_tickets", 
				       value: this.state.ticketNumber, className: "form-control", placeholder: "Pocet listku"})
			    ), 
			    React.createElement("div", {className: "form-group"}, 
				React.createElement("textarea", {form: "idecko", onChange: this.noteChange, isValid: "true", name: "note", 
					  value: this.state.note, className: "form-control", placeholder: "Poznámka - nepovinné"})
			    ), 
			    React.createElement("div", {className: "form-group"}, 
				React.createElement("input", {form: "idecko", onChange: this.conditionsChange, type: "checkbox", isValid: "false", name: "conditions", 
				       value: "conditions", checked: this.state.conditions}, 
				    React.createElement("a", {href: "http://www.sdhsvinov.cz/Sbor/VOPeTicket/"}, "Přečetl jsem si a souhlasím se všeobecnýma obchodníma podmínka")
				)
			    ), 

			    React.createElement("button", {type: "submit", onClick: this.submit, className: "btn-success"}, "Odeslat")
			)
		    )
		)
	    }
	});


/***/ },
/* 2 */
/***/ function(module, exports) {

	module.exports = React;

/***/ },
/* 3 */
/***/ function(module, exports, __webpack_require__) {

	/** @jsx React.DOM */var React = __webpack_require__(2);

	module.exports = React.createClass({displayName: "module.exports",
		render: function () {
			var error;
			if (this.props.field) {
				error = "Povinne pole!";
			}
			return (React.createElement("div", null, 
						React.createElement("span", null, error)
			))
		}

	});

/***/ }
/******/ ]);