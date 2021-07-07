name="Rohan WaRange"
print(name.lower())

print(name.upper())

print(name.title())
print(name.capitalize())
print(name.casefold())
print(name.center(20,"$"))
print(name.encode())
print(name.endswith("e"))
# print(name.title())
# print(name.title())
# print(name.title())
# print(name.title())
print(name.zfill(13))

print(name.count("R"))

firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "Rohabcnghi"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))

