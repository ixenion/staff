// ?: Elvis operator


var nullableName : String? = "Denis"
var name = nullableName ?: "Guest"
println("$name")	// Denis

var nullableName : String? = "Denis"
nullableName = null
var name = nullableName ?: "Guest"
println("$name")	// Guest

nullableName!!.toLowerCase()


// chain safe call
val wifesAge: String? = user?.wife?.age ?: 0



