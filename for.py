# Simple for loop on number list
iNumbers = [1,2,3,4,5]

for i in iNumbers:
    print(i)

# Loop using range
rangeNum = range(10)
for k in rangeNum:
    print(k)

# Simple for loop on  String List
iString = ('Srinivas', 'Anil', 'Peter', 'Alex', 'Lakshmi')

for j in iString:
    print(j)

# Simple for loop on Dictionary
number_of_legs = {
    'Birds': 2,
    'Cats': 4,
    'Ant': 6,
    'Spider': 8
}

for animal, legs in number_of_legs.items():
    print("{} have {} legs".format(animal,legs))
