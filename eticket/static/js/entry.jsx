'use strict'

/*
 * Entry point for MSL dashboard client, it just starts the app.
 */

var Switcher = require('./components/Switcher');

ReactDOM.render(<Switcher/>, document.getElementById('content'));
