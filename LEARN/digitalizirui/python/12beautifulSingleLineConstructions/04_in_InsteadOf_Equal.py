name = "Vasya"
if name == "Vasya" or name == "Petya":
    print(name)

# simplier
if name in ("Vasya", "Petya"):
    print(name)


# example 2
a = b = c = d = e = True

if a and b and c and d and e:
    print("All True")

# simplier
if all((a, b, c, d, e)): print("All True")
# instead of "OR"
if any((a, b, c, d, e)): print("At least one True")
