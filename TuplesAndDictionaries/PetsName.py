def dog_owners(pets_list):
    res = dict()
    for i in pets_list:
        res[(i[1], i[2], i[3])] = res.get((i[1], i[2], i[3]), []) + list((i[0],))
    return res

pets = [("Fido", "John", "Malkovic", 22),
        ("Butch", "Jake", "Smirnoff", 18),
        ("Zooma", "Simon", "Ng", 32),
        ("Chase", "Martha", "Black", 73),
        ("Rocky", "Simon", "Ng", 32)]

print(dog_owners(pets))

#should be:
# == {("John", "Malkovic", 22): ["Fido"],
#                     ("Jake", "Smirnoff", 18): ["Butch"],
#                     ("Simon", "Ng", 32): ["Zooma", "Rocky"],
#                     ("Martha", "Black", 73): ["Chase"]
#                     })
