
fun myF(a: Int){
 a = 5	// Error. cannot assign value to a parameter
}

// a is a parameter
fun myF(a: Int){
 // a is a variable
 var a = 5
 // also can do
 var a = a
}

