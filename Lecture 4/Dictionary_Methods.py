dict = {
    "Name" : "Atharva Bari",
    "Roll no." : 5,
    "Course" : "TYCO",
    "Subjects" : ["DCN", "JPR", "MIC", "OOP"],
    "Marks" : {
        "DCN" : 45,
        "JPR" : 46,
        "MIC" : 47,
        "OOP" : 48
    }
}

print(len(list(dict.keys()))) # List gives the list of all keys in the dictionary. 
# len gives the no. of keys in the Dictionary. 
print(len(dict), "\n") # len can also be printed this way.

print(dict.values(), "\n")

print(list(dict.items()), "\n")

print(dict.get("Name"))

# dict.update({"City" : "Dahanu"}) # one way to write this method 
# print(dict)

new_update = {"Gender" : "Male"} # another way
dict.update(new_update) 
print(dict)