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

	module.exports = React.createClass({displayName: "module.exports",
		getInitialState: function () {
			return {
				name: ""
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
			this.setState({ ticket: e.target.value });
		},
		submit: function (e) {
			alert(
				"Name: " + this.state.name +
				"\nSurname: " + this.state.surname +
				"\nPhone: " + this.state.phone +
				"\nEmail: " + this.state.email +
				"\nTickets: " + this.state.ticket
				);
		},
		render: function () {
			return (
			React.createElement("div", null, 
				React.createElement("form", {action: "https://google.com", method: "post", className: "col-xs-6 col-xs-offset-3"}, 
					React.createElement("div", {className: "input-group"}, 
						React.createElement("input", {onChange: this.nameChange, value: this.state.name, type: "text", className: "form-control", placeholder: "Jmeno"})
					), 
					React.createElement("div", {className: "input-group"}, 
						React.createElement("input", {onChange: this.surnameChange, value: this.state.surname, type: "text", className: "form-control", placeholder: "Prijmeni"})
					), 
					React.createElement("div", {className: "input-group"}, 
						React.createElement("input", {onChange: this.phoneChange, type: "tel", value: this.state.phoneNumber, className: "form-control", placeholder: "Telefon"})
					), 
					React.createElement("div", {className: "input-group"}, 
						React.createElement("input", {onChange: this.emailChange, type: "email", value: this.state.email, className: "form-control", placeholder: "Email"})
					), 
					React.createElement("div", {className: "input-group"}, 
						React.createElement("input", {onChange: this.ticketChange, type: "number", value: this.state.ticketNumber, className: "form-control", placeholder: "Pocet listku"})
					), 

					React.createElement("button", {type: "submit", className: "btn-success", onClick: this.submit}, "Submit")
				)
			)
			)
		}
	});

/***/ },
/* 2 */
/***/ function(module, exports) {

	module.exports = React;

/***/ }
/******/ ]);