// The class tht inherits the features of another
// class is called the Sub class or child class or Derived class
// and tha class whose features are
// inherited is called the Super class or parent class or Base class


// by default all classes are not inheritable, need to add "open"
open class Vehicle{
	// properties
	// methods
}

// inherit from it:
open class Car(val name: String, var brand: String) : Vehicle(){
	// properties also may be "open"
	open var range: Double = 0.0

	fun extendedRange(amount: Double){
		if(amount > 0)
			range += amount
	}

	open fun drive(distance: Double){
		println("Drove for $distance KM")
	}
}

class ElectricCar(name: String, brand: String, batteryLife: Double) : Car(name, brand){
	// overriding Parent function
	override var range = batteryLife * 6
	override fun drive(distance: Double){
		println("Drove for $distance KM on electricity")
	}
	
}





fun main(){
	var myCar = Car(name:"A3", brand:"Audi")
	var myECar = ElectricCar(name:"S-Model", brand:"Tesla", batteryLife:85.0
	
	myECar.extendedRange(amount:200.0) // now Tesla be "Drove for 400 KM"
	myCar.drive(distance:200.0)
	myECar.drive(distance:200.0)	// and there is no complaining

}












