# _______________________________⚠ Variables In Python ⚠______________________________________________

a = 7
myFloat = 55.44

print(a)
print(myFloat)

# _______________________________⚠ String ⚠______________________________________________


myName = "Rohit Soni"

print(myName)
print(myName[7])
print(myName[4])

# myName[0] = "T"   # Strings are UnMutable means cannot be changed

print(myName)


# _______________________________⚠ List ⚠______________________________________________
#  [Supports Different Data Types but Dont Use them to be confused ]

myFruitsList = ["Mango", "Banana", "Grapes"]

print(myFruitsList)
print(myFruitsList[2])
print(myFruitsList[0])

myCollectionList = [1, 2, "Rohit", "Captian"]

print(myCollectionList[3])
print(myCollectionList)

myFruitsList[0] = "Apple"  # Change or Mutable

print(myFruitsList)


# _______________________________⚠ Tuple ⚠______________________________________________
# Tuples are UnMutable means cannot be changed

myTuple = ["Mango", "Banana", "Grapes"]

print(myTuple)
print(myTuple[2])
print(myTuple[0])

# myTuple[0] = "Apple"   # Tuple are UnMutable means cannot be changed

# _______________________________⚠ Dictionary ⚠______________________________________________
# Mutable means we can change the values


myObject = {
    "MyName": "Rohit",
    "MyAge": "23",
    "HairColor": "Black"
}

print(myObject)
print(myObject["MyAge"])
print(myObject["HairColor"])

myObject["MyAge"] = 44

print(myObject)  # Mutable means we can change the values


# _______________________________⚠ Sets In Python ⚠______________________________________________

""" A set is a collection of unique data. """

""" __ Suppose we want to store information about student IDs. Since student IDs cannot be duplicate,
        we can use a set. __"""

# But a set cannot have mutable elements means we can not change the values

student_ids = {112, 114, 116, 118, 115}

print(student_ids)

vowel_letters = {'a', 'e', 'i', 'o', 'u'}

print('Vowel Letters:', vowel_letters)


