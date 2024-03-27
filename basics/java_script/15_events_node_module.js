// indicates that something is happening



const EventEmiter = require('events')	// class
const emitter = new EventEmiter()	// object

// Register a listener
emitter.on('messageLogged', function(arg){
	console.log('Listener called', arg)
})


// Raise an event
emitter.emit('messageLogged', {id: 1, url: 'http://'})



