my_dict = {
    
    "name": "haneesh",
    "age":11,
    "grade":8,
    "weight":35.4,
    "student": True
}
print(my_dict)
print(len(my_dict))
print(my_dict["name"])

my_dict["grade"] = 6
print(my_dict)

my_dict["gender"] = "male"
print(my_dict)

my_dict.pop("weight")
print(my_dict)

name = my_dict.get("name")
print("name")
my_dict.clear()
print(my_dict)

new_dict = my_dict.values()
print(new_dict)