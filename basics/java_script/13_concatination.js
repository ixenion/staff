const os = require('os')

var totalMemory = os.totalmem()
var freeMemory = os.freemem()

// simple
console.log('Total MEmory: ' + totalMemory)

// better
console.log(`Total Memory: ${totalMemory}`)
console.log(`Free Memory: ${freeMemory}`)
