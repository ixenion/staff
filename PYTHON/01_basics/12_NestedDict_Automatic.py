# a clean way to add nested data to a dictionary
from collections import defaultdict

# recursive version of defaultdict
# which itself will create a new default dict value
# when a non existing key is accessed
def recursive_defaultdict():
    return defaultdict(recursive_defaultdict)


nested_dict = recursive_defaultdict()

# 'recursive_defaultdict' will automatically create nested
# dictionaries as we need them
nested_dict["planet"]["earth"]["mass (kg)"] = 6*10**24
nested_dict["planet"]["mars"]["mass (kg)"] = 6.4*10*23

# code above is much cleaner than the verbose alternative:
nested_dict = {}
nested_dict["planet"] = {}
nested_dict["planet"]["earth"] = {}
nested_dict["planet"]["mars"] = {}
nested_dict["planet"]["earth"]["mass (kg)"] = 6*10**24
nested_dict["planet"]["mars"]["mass (kg)"] = 6.4*10**23
