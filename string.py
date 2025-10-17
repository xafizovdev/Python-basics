ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # We add a space between two variables.

ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")


""".upper()-->The upper() method converts all the letters in the text to uppercase."""
""".lower()-->The lower() method converts all the letters in the text to lowercase."""
""".capitalize()--> The capitalize() method writes the first letter of the text in uppercase and makes the rest of the letters lowercase."""
""".title()-->The title() method writes each word in the text with a capitalized first letter."""

ism = input("What's your name?")
print("Assalom alaykum, " + ism)

street = "Bog'bon"
neighborhood = "Sog'bon"
district = "Bodomzor"
region = "Samarqand"


print(street + " street, " + neighborhood + " neighborhood, " + \
      district + " district, " + region + " region")


print("Please enter the following information:")
street = input("Your street: ")
neighborhood = input("Your neighborhood: ")
district = input("Your district: ")
region = input("Your region: ")
print(street + " street, " + neighborhood + " neighborhood, " + \
      district + " district, " + region + " region")


print(street + " street,\n" + neighborhood + " neighborhood,\n" + \
      district + " district,\n" + region + " region")

address = f"{street} street, {neighborhood} neighborhood, {district} district, {region} region"
print(address)


print(address.upper())
print(address.lower())
print(address.title())
print(address.capitalize())


