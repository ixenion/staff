var url = 'http://mylogger.io/log'

function log(message) {
	// Send an HTTP request
	console.log(message)
}

// export module
module.exports.log = log
//module.exports.endPoint = url
