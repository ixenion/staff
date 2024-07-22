// interfaces allow to extend functionality of classes

interface Drivable{
	val maxSpeed: Double
	fun drive(): String
	fun brake(){
		println("The drivable is braking")
	}

}


open class Car(override val maxSpeed: Double, val name: String, var brand: String) : Drivable{
	// properties also may be "open"
	open var range: Double = 0.0

	fun extendedRange(amount: Double){
		if(amount > 0)
			range += amount
	}
	
	override fun drive(): String {
		return "driving the interface drive"
	}
	// shorter way:
	override fun drive(): String = "driving the interface drive"

	open fun drive(distance: Double){
		println("Drove for $distance KM")
	}
}

class ElectricCar(maxSpeed: Double, name: String, brand: String, batteryLife: Double) : Car(maxSpeed, name, brand){
	// overriding Parent function
	override var range = batteryLife * 6
	override fun drive(distance: Double){
		println("Drove for $distance KM on electricity")
	}

	override fun drive(): String{
		return "Drove for $range KM on electricity"
	}
	
}

// interface can inherit from another interface
