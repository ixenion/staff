// used to create dynamic arrays

ArrayList<E>(): Is used to create an empty ArrayList
ArrayList(capacity: Int): Is used to create an ArrayList of cpecified capacity
ArrayList(elements: Collection<E>): Is used to create an ArrayList filled eith the elements of a collection


// functions of ArrayList
open fun add(element: E): Boolean -> used to add the specific element into the collection
open fun clear() -> used to remove all elementst from the collection
open fun get(index:Int):E -> used to return the element at specified index in the list
open fun remove(element:E):Boolean -> used to remove a single instance of the specific element from current collection, if it is available
// thare are many more functions in the ArrayList Class



// Empty ArrayList
fun main(){
	val arrayList = ArrayList<String>()		// Creating an empty arraylist
	arrayList.add("One")					// Adding an object in arraylist
	arrayList.add("Two")
	println("....print ArrayLIst....")
	for (i in arrayList) {
		println(i)
	}
}
// Output
....print ArrayList
One
Two


// ArrayList using collections
fun main() {
	val arrayList: ArrayList<String> = ArrayList<String>(5)
	var list: MutableList<String> = mutableListOf<String>()

	list.add("One")
	list.add("Two")

	arrayList.addAll(list)

	println("....print ArrayList....")
	val itr = arrayList.iterator()

	while(itr.hasNext) {
		println(itr.next())
	}
	println("size of arrayList = "+arrayList.size)
}
// Output
....print ArrayList....
One
Two
size of arrayList 2



// ArrayList get()
fun main(args:Array<String>) {
	val arrayList:ArrayList<String> = ArrayList<String>()
	arrayList.add("One")
	arrayList.add("Two")
	for (i in arrayList) {
		println(i)
	}
	println("....print ArrayList....")
	println( arrayList.get(1))
}
// Output
One
Two
Two







