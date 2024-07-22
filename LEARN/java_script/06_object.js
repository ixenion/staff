let name = "ab"
let age = 30
let person = {
 name: 'Mosh',
 age: '30'
}

console.log(person)	// {name: "Mosh", age: 30}

// dot notation
person.name = 'John'
console.log(person.name)

// bracket notation
person['name'] = 'Mery'


// interaction
let selection = 'name'
person[selection] = 'Mary'


