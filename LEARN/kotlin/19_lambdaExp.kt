// lambda (Expression) is a function which has no name
// -> is lambda operator

// define usual function of adding 2 numbers
fun addNum(a:Int, b:Int) {
	val add = a + b
	println(add)
}

// same but shorter
val sum: (Int, Int) -> Int = {a: Int, b: Int -> a + b}
println(sum(5,10))

// even shorter
val sum = {a:Int, b:Int -> println(a + b)}
sum(5,10)





































