const fs = require('fs')

//syncdir = fs.readdirSync('./')	// returns curent dir files
//console.log(syncdir)


fs.readdir('./', function(err,files) {
	if (err) console.log('Error', err)
	else console.log('Result', files)
})

