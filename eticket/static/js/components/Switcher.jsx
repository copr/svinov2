var React = require('react');

module.exports = React.createClass({
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
		<div>
			<form action="https://google.com" method="post" className="col-xs-6 col-xs-offset-3">
				<div className="input-group">
					<input onChange={this.nameChange} value={this.state.name} type="text" className="form-control" placeholder="Jmeno" />
				</div>
				<div className="input-group">
					<input onChange={this.surnameChange} value={this.state.surname} type="text" className="form-control" placeholder="Prijmeni"/>
				</div>
				<div className="input-group">
					<input onChange={this.phoneChange} type="tel" value={this.state.phoneNumber} className="form-control" placeholder="Telefon"/>
				</div>
				<div className="input-group">
					<input onChange={this.emailChange} type="email" value={this.state.email} className="form-control" placeholder="Email"/>
				</div>
				<div className="input-group">
					<input onChange={this.ticketChange} type="number" value={this.state.ticketNumber} className="form-control" placeholder="Pocet listku"/>
				</div>

				<button type="submit" className="btn-success" onClick={this.submit}>Submit</button> 
			</form>
		</div>
		)
	}
});