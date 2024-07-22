// similar to interfaces but stil different...

// An abstract class cannot be instantiated
// (you cannot create objects of an abstract class)
// However, you can inherit subclasses from an abstract class.
// The members (properties and methods) of an abstract class are non-abstract
// unless you explicitly use the abstract keyword to make them abstract.

abstract class Mammal(private val name: String, private val origin: String, private val weight: Double){

	// abstract properrty
	abstract var maxSpeed: Double
	
	// abstract methods
	abstract fun run()
	abstract fun breaath()
	
	// concrete (non-abstract) method
	fun displayDetails(){
		println("Name: $name, Origin: $origin, Weight: $weight, " + "Max Speed: $maxSpeed")
	}

}



class Human(name: String, origin: String, weight: Double, override var maxSpeed: Double): Mammal(name, origin, weight){

	override fun run(){
		println("Runs on two legs")
	}
	
	override fun breath(){
		println("Breath through mouth or nose")
	}
}

class Elephant(name: String, origin: String, weight: Double, override var maxSpeed: Double): Mammal(name, origin, weight){

	override fun run(){
		println("Runs on four legs")
	}
	
	override fun breath(){
		println("Breath through the trunk")
	}
}



fun main() {

	val human = Human(name:"Denis", origin:"Russia", weight: 70.0, maxSpeed:28.0)
	val elephant = Elephant(name:"Rosy", origin:"India", weight:5400.0, maxSpeed:25.0)

	human.run()
	elephant.run()

	human.breath()
	elephant.breath()

}
