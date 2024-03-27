#another way to organize code
#pakage is a container for multiple modules(functions)
#packages are mede from dirrectories by putting "__init.py" file in that dirrectory.
import zz_etc.point_18_ecommerce.shipping as ecommerce_shipping
# from etc.ecommerce18 import shipping

#to access any functions or classes in this module
ecommerce_shipping.calc_shipping()#prints message "calc_shipping"

#another way:
# from ecommerce18.shipping import calc_shipping
from zz_etc.point_18_ecommerce.shipping import calc_shipping
print("")
calc_shipping()
calc_shipping()
calc_shipping()
