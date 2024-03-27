/*
os.freemem()	// returns free memory on the machine
os.totalmem()	// returns tot mem on the machine
os.userInfo([options])
os.uptime()	//
*/
const os = require('os')

var totalMemory = (os.totalmem() / 8)
console.log(totalMemory)
