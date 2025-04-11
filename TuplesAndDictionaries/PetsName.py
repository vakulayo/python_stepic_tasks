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
#                     })
