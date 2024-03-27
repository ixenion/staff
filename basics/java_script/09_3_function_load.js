// for single function load need to export that function only
module.exports = log


// loading function at another .js
const logger = require('./module/to/load')
logger('message')
