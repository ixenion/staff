// used instead of "else if"

var season = 3
when(season)
{
 1 -> println("Spring")
 2 -> println("Summer")
 3 -> 
 {
  println("Fall")
  println("Autumn")
 }
 4 -> println("winter")
}

var month = 3
when(month)
{
 in 3..5 -> println("Spring")
 in 6..8 -> println("Summer")
 in 9..11 -> println("Fall")
 12, 1, 2 -> println("Winter")

 else -> println("Invalid month")
}



// check "x" for it's type

var x : Any = 13.111
when(x)
{
 is Int -> println("$x is an Int")
 is Double -> println("$x is a Double")
 is String -> println("$s is a String")

 else -> println("$x is none of the above")
}




