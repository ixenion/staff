

fun main(){

 var denis = Person("Denis", "Panjuta")

}


class Person constructor(firstName: String, lastName: String){

init {
println("Person created")	// immideatly executed when class is created. used to initialise objects

}


}


// class with default values
class Person constructor(fn: String = "John"){

}

