// create a list of strings
val stringList: List<String> = listof("Denis", "Frank", "Michael")

// list of any type
val mixedTypeList: List<Any> = listof("Denis",30, 5, "BDay")


for(value in mixedTypeList) {
	if (value is Int){
		println("Integer: '$value'")
	} else if (value is Double) {
		println("Double: '$value' with Floor value ${floor(value)}")
	} else if (value is String) {
		println("String: '$value' of length ${value.length}")
	} else {
		println("Unknown Type")
	}

}


// Alternatively
for(value in mixedTypeList) {
	when(value) {
		is Int -> println("Integer: '$value'")
		is Double -> println("Double: '$value' with Floor value ${floor(value)}")
		is String -> println("String: '$value' of length ${value.length}")
		else -> println("Unknown Type")
	}
}



// Explicit (safe) casting using the "as?" keyword
val obj3: Any = 1337
val str3: String? = obj3 as? String // Works
println(str3)
