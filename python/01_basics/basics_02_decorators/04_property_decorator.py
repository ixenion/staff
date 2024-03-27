# EXAMPLE 1

# Python program to illustrate the use of
# @property decorator
 
# Defining class
class Portal:
 
    # Defining __init__ method
    def __init__(self):
        self.__name =''
     
    # Using @property decorator
    @property
     
    # Getter method
    def name(self):
        return self.__name
     
    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val
 
    # Deleter method
    @name.deleter
    def name(self):
       del self.__name
 
# Creating object
p = Portal();
 
# Setting name
p.name = 'GeeksforGeeks'
 
# Prints name
print (p.name)
 
# Deletes name
del p.name
 
# As name is deleted above this
# will throw an error
# print (p.name)



# EXAMPLE 2

# Python program to illustrate the use of
# @property decorator
 
# Creating class
class Celsius:
     
    # Defining init method with its parameter
    def __init__(self, temp = 0):
        self._temperature = temp
 
    # @property decorator
    @property
     
    # Getter method
    def temp(self):
         
        # Prints the assigned temperature value
        print("The value of the temperature is: ")
        return self._temperature
 
    # Setter method
    @temp.setter
    def temp(self, val):
         
        # If temperature is less than -273 than a value
        # error is thrown
        if val < -273:
            raise ValueError("Temperature must be abowe -273 celsius.\nExit.")
         
        # Prints this if the value of the temperature is set
        print("The value of the temperature is set.")
        self._temperature = val
 
 
# Creating object for the stated class
cel = Celsius();
 
# Setting the temperature value
cel.temp = -270
 
# Prints the temperature that is set
print(cel.temp)
 
# Setting the temperature value to -300
# which is not possible so, an error is
# thrown
cel.temp = -300
print(cel.temp)
