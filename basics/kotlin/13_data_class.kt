
// must have at least one parameter
data class User(val id: Long, var name: String)


fun main(){
 // create object of a data class
 val user1 = User(1, "Denis")

 // access property
 val name = user1.name	// name = "Denis"

 // assign a new value
 user1.name = "Michael"

 // compare properties
 var user2 = User(1, "Michael")
 println(user1.equals(user2))	// prints "true"

 // copy objects
 var updatedUser = user1.copy(id=2)	// copy object while changing some properties


 // access by component
 println(user1.component1())	// prints id value
 println(user1.component2())	// prints name value


 // deconstruction. takes values from Dclass and stores them into separate vars
 val (id, name) = updatedUser
 // like so
 //val id = updatedUser.id
 //val name = updatedUser.name

 
