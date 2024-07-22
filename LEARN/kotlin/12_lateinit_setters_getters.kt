

fun main() {

var myCar = Car()

myCar.myModel = "M3"	// Error returned cause "private set" But getter is not privase, so can get the vakue stored

}

class Car(){

// means initialise it later
lateinit var owner: String

val myBrand: String = "bmw"
// Custom getter
get() {
return field.toLowerCase()
}

// setter. create custom setter
var maxSpeed: Int = 250
 get() = field
 set(value){
  field = if(value > 0) value else throw IllegalArgumentException("Max speed must be > 0")
 }


// private setter. means it would be available only in that particular class
var myModel: String = "M5"
 private set


init {
this.owner = "Frank"
}

}


