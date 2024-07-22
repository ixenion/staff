// are the keywords whith are used to restrict the use of classes, interfaces, methods, and properties in kotlin

1. public
A public modifier element is accessable from everywhere in the project
It's a default modifier in kotlin. If any class, interface, etc. are not specified with any
access/visibility modifier then that class, interface etc. is used in a public scope.
All public declarations can be placed at the top of the file.
If a member of a class is not specified then it is by default public.

2. private
A private modifier allows the element to be accessable only within th block in
which properties, fields, etc. are declared.
The private modifier declaration does not allow access outside the scope.
A private package can be accessable within that specific file.

3. internal modifier
Intern modifier is feature in kotlin, which is not available in Java.
The internal modifier makes the field visible only inside the module in which it is implemented.
All fields are declared as internal which are accessable only inside the module in which they are implemented.

Open keyword
In Kotlin all classes are final by default, so they can't be inherited by default.
Side note: in Java it's the opposite, there you have to make your class final explicitly
So to make a class inheritable to other classes you must mark it with the "open" keyword,
else you get an error "type is final so can't be inherited"

4. protected modifier
A pr modf with a class or an interface allows visibility to its class or
subclass only.
A protected declaration (when overriden) in its subClass is also protected unless
it is explicitly changed.
The protected modifier cannot be declared at top level. (for Packages)


