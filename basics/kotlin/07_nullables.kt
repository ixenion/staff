

fun main()
{

 var name: String = "John"
 // name = null -> Compilation Error
 var nullableName: String? = "John"
 nullableName = null

 var len = name.length
 // var len2 = nullableName.length -> Error
 // old fashion
 if(nullableName != null)
 {
  var len2 = nullableName.length
 }
 else
 {
  null
 }

 // new fashion
 var len2 nullableName?.length

 var var1 = "Name"
 println("Name: $var1.toLowerCase())


 // do code if var isnot null
 nullableName?.Let { println(it.length) }
 

}



