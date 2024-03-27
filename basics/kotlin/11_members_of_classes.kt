class Pr(fn: String = "John"){

// member variables - properties
var age: Int? = null
var hobby: String = "watch Netflix"
var firstName: String? = null

init {
this.firstName = firstName
}

// member functions - methods
fun stateHobby(){
println("$firstName\'s hobby is $hobby")
}

// member secondary constructor
constructor(fn: String, age: Int): this(fn){
this.age = age
}


}


fun main(){
var denis = Pr("Denis", age: 31)
println("Denis is ${denis.age} years old")
denis.hobby = "skateboard"
denis.stateHobby()	// access method of th Pr class


