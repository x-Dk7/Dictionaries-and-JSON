import json

# dictionaries
p1 = { "name":"Dk", "age":16, "hair":"black hair", "gender":"male"}
p2 = { "name":"Ellie", "age":45, "hair":"dirty blonde hair", "gender":"female"}
p3 = { "name":"Mahmoud", "age":47, "hair":"black hair", "gender":"male"}
p4 = { "name":"Javad", "age":92, "hair":"gray hair", "gender":"male"}

# list of my family members
family = [p1, p2, p3, p4]
print("Family:")
print(type(family))
# prints a member of my family and their information
for member in family:
    print(member['name'] + ", " + str(member['age']) + ", " + member['hair'] + ", " + member["gender"])
print()

# list of family members becomes a dictionary
dict_family = {'members': family}
print("Dictionary of family:")
print(type(dict_family))
family = dict_family['members']
# prints a member of my family and their info
for member in family:
    print(member['name'] + ", " + str(member['age']) + ", " + member['hair']+ ", " + member["gender"])
print()

# converts dictionary into a JSON file
json_family = json.dumps(dict_family)
print("JSON family: ")
print(type(json_family))
print(json_family + "(੭ತ◡ತ)੭̸*✩⁺˚")
print()


# converts JSON file into a dictionary
dict_family = json.loads(json_family)
print("Dictionary of people:")
print(type(dict_family))
family = dict_family['members']
# prints a member of my family and their info using dictionary
for member in family:
    print(member['name'] + ", " + str(member['age']) + ", " + member['hair']+ ", " + member["gender"] + "   (੭ತ◡ತ)੭̸*✩⁺˚")
print()

# creates a new list with the family dictionary
new = dict_family["members"]
# selecting parents by using indexes in the list
parents = [new[2], new[3]]
# selecting grandparents by using indexes in the list
grandparents = [new[4]]
# creates a new dictionary with only parents and grandparents
new_dict = {'parents': parents, 'grandparents': grandparents}
print("New dictionary:")
print(type(new_dict))
print(new_dict)
print()

# parents
print("My parents:")
# creates a variable from dictionary only using the parents
parents = new_dict["parents"]
# prints parents and their info using the dictionary
for member in parents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['hair']+ ", " + member["gender"] + "   (੭ತ◡ತ)੭̸*✩⁺˚")
print()

# grandparents
print("My grandparents:")
# creates a variable from dictionary only using the grandparents
grandparents = new_dict["grandparents"]
# prints grandparents and their info using the dictionary
for member in grandparents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['hair']+ ", " + member["gender"] + "   (੭ತ◡ತ)੭̸*✩⁺˚")
print()