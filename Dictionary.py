colors = ["red", "blue", "green", "orange", "yellow"]
names = ["name1", "name2", "name3", "name4", "name5"]
# creating a dictionary
sample1 = {
    "name1": "red",
    "name2": "blue",
    "name3": "green",
    "name4": "orange",
    "name5": "yellow"
}

# accessing values of a dictionary
print(sample1)
print(sample1['name1'])

# getting the list of keys
print(sample1.keys())

# values of the dictionary
print(sample1.values())


for key in sample1.keys():
    print(key,sample1[key])