var React = require('react');
var Error = require('./Error');
var Udalost = event;
var UdalostPole = eventField;


module.exports = React.createClass({
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
			alert("Vyplò vsechna pole!");
			return false;
		});

},
	render: function () {
	return (
		<div>
			<div>
				<h3>Udalost: { Udalost[0].fields.name}</h3>
				<h3>Cena: {this.state.ticketNumber * Udalost[0].fields.price} Kc</h3>
			</div>
			<form action="https://google.com" method="post" className="col-xs-6 col-xs-offset-3">
				<div className="form-group empty">
					<input onChange={this.nameChange} onBlur={this.validate} value={this.state.name} type="text" className="form-control" placeholder="Jmeno" />
					<Error field={this.state.empty} />
				</div>
				<div className="form-group empty">
					<input onChange={this.surnameChange} isValid="false" onBlur={this.validate} value={this.state.surname} type="text" className="form-control" placeholder="Prijmeni" />
				</div>
				<div className="form-group empty">
					<input onChange={this.phoneChange} isValid="false" onBlur={this.validate} type="tel" value={this.state.phoneNumber} className="form-control bfh-phone" data-format="+420 ddd ddd ddd" placeholder="Telefon" />
				</div>
				<div className="form-group empty">
					<input onChange={this.emailChange} isValid="false" onBlur={this.validate} type="email" value={this.state.email} className="form-control" placeholder="Email" />
				</div>
				<div className="form-group empty">
					<input onChange={this.ticketChange} isValid="false" onBlur={this.validate} type="number" value={this.state.ticketNumber} className="form-control" placeholder="Pocet listku" />
				</div>

				<button type="submit" onClick={this.submit} className="btn-success">Submit</button>
			</form>
		</div>
		)
}
});