# problem: get all names starting on "A"
names = ["Hristo", "Ademar", "Teya", "Stefania", "Arhip"]
names_starts_a = []
for name in names:
    if name.startswith("A"):
        names_starts_a.append(name)
print(names_starts_a)

# simplier
names = ["Hristo", "Ademar", "Teya", "Stefania", "Arhip"]
names_starts_a = [name for name in names if name.startswith("A")]

# another simple way
names = ["Hristo", "Ademar", "Teya", "Stefania", "Arhip"]
names_starts_a = list(filter(lambda name: name.startswith("A"), names))

# but better use "kortej" - tupl
# because it faster and uses less RAM then "list"
names = ["Hristo", "Ademar", "Teya", "Stefania", "Arhip"]
names_starts_a = tuple(filter(lambda name: name.startswith("A"), names))

