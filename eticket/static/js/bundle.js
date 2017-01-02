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
				ticketNumber: 1,
				errors: [],
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
		ticketChange: function (e) {
			if (e.target.value < 1 || e.target.value === "") {
				this.setState({ ticketNumber: 1 })
			} else {
				this.setState({ ticketNumber: e.target.value });
			}
		},
		validate: function (e) {
			var val = e.target.value;
			e.target.parentElement.classList.remove('has-success', 'has-error','empty');
			if (val) {
				e.target.parentElement.classList.add('has-success')
			} else {
				e.target.parentElement.classList.add('has-error','empty');
			}
		},
		submit: function (e) {
			$("div.empty").each(function () {
				e.preventDefault();
				alert("Vypl� vsechna pole!");
				return false;
			});

	},
		render: function () {
		return (
			React.createElement("div", null, 
				React.createElement("div", null, 
					React.createElement("h3", null, "Udalost: ",  Udalost[0].fields.name), 
					React.createElement("h3", null, "Cena: ", this.state.ticketNumber * Udalost[0].fields.price, " Kc")
				), 
				React.createElement("form", {action: "https://google.com", method: "post", className: "col-xs-6 col-xs-offset-3"}, 
					React.createElement("div", {className: "form-group empty"}, 
						React.createElement("input", {onChange: this.nameChange, onBlur: this.validate, value: this.state.name, type: "text", className: "form-control", placeholder: "Jmeno"}), 
						React.createElement(Error, {field: this.state.empty})
					), 
					React.createElement("div", {className: "form-group empty"}, 
						React.createElement("input", {onChange: this.surnameChange, isValid: "false", onBlur: this.validate, value: this.state.surname, type: "text", className: "form-control", placeholder: "Prijmeni"})
					), 
					React.createElement("div", {className: "form-group empty"}, 
						React.createElement("input", {onChange: this.phoneChange, isValid: "false", onBlur: this.validate, type: "tel", value: this.state.phoneNumber, className: "form-control bfh-phone", "data-format": "+420 ddd ddd ddd", placeholder: "Telefon"})
					), 
					React.createElement("div", {className: "form-group empty"}, 
						React.createElement("input", {onChange: this.emailChange, isValid: "false", onBlur: this.validate, type: "email", value: this.state.email, className: "form-control", placeholder: "Email"})
					), 
					React.createElement("div", {className: "form-group empty"}, 
						React.createElement("input", {onChange: this.ticketChange, isValid: "false", onBlur: this.validate, type: "number", value: this.state.ticketNumber, className: "form-control", placeholder: "Pocet listku"})
					), 

					React.createElement("button", {type: "submit", onClick: this.submit, className: "btn-success"}, "Submit")
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