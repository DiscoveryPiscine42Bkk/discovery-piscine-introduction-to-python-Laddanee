def pinprawa (family):
    return list(filter(lambda name: family[name] == "pin", family.keys ()))

dupont_family = {
    "pin": "pin",
    "geno": "geno",
    "mairu": "prawa",
    "chutinun": "pin",
    "yungmak": "pin"
}

print(pinprawa(dupont_family))