def dog_owners(pets):
    res = dict()
    for pet, name, surname, age in pets:
        res[(name, surname, age)] = res.get((name, surname, age), []) + [pet]
    return res

petss = [("Fido", "John", "Malkovic", 22),
        ("Butch", "Jake", "Smirnoff", 18),
        ("Zooma", "Simon", "Ng", 32),
        ("Chase", "Martha", "Black", 73),
        ("Rocky", "Simon", "Ng", 32)]

print(dog_owners(petss))

#should be:
# == {("John", "Malkovic", 22): ["Fido"],
#                     ("Jake", "Smirnoff", 18): ["Butch"],
#                     ("Simon", "Ng", 32): ["Zooma", "Rocky"],
#                     ("Martha", "Black", 73): ["Chase"]
#                     }


def update_age(owners, owner, new_age):
    if owners.get(owner) and new_age != owner[2]:
        owners[(owner[0], owner[1], new_age)] = owners.pop(owner)

dog_owners = {("John", "Malkovic", 22): ["Fido"],
              ("Jake", "Smirnoff", 18): ["Butch"],
              ("Simon", "Ng", 32): ["Zooma", "Rocky"],
              ("Martha", "Black", 73): ["Chase"]
              }


update_age(dog_owners, ("Jake", "Smirnoff", 18), 22)
update_age(dog_owners, ("Jake", "Smirnoff", 22), 23)
update_age(dog_owners, ("Jake", "Smirnoff", 30), 24)
print(dog_owners.get(("Jake", "Smirnoff", 22))) #==None
print(dog_owners.get(("Jake", "Smirnoff", 18))) #==None
print(dog_owners.get(("Jake", "Smirnoff", 23))) #==['Butch']
print(dog_owners.get(("Jake", "Smirnoff", 24))) #==None