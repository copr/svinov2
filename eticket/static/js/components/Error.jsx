var React = require('react');

module.exports = React.createClass({
	render: function () {
		var error;
		if (this.props.field) {
			error = "Povinne pole!";
		}
		return (<div>
					<span>{error}</span>
		</div>)
	}

});