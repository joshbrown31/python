def hello_world(): #use snake casing -> underscore between words. colon instead of {}
    print("Hello World") #print is equivalent to console.log in JS. you can use either types of quotations.

hello_world()

def list_of_things(int, str, bool):

    print(int)
    print(str)
    print(bool)

    total_string = f"Here's my list of strings: {int}, {str}, {bool}. F-strings are awesome!!"
    print(total_string)

    newStr = "This is the new string",
    print(newStr)

list_of_things(9, "woah", True)


#F-strings-> introduced in python 3.6, so coderunner won't run these. Use curly brackets to pull variables into strings.
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.") #f goes before the quotation marks in order to f-format the string


#It's important to know that Python uses [ ] characters to return a copy of the list, constrained to the specified indices. This can be thought of as behaving like the slice function in JavaScript. The starting index and ending index should be separated by the ":" character.
x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];


#Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequences, including tuples and strings. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly used sequence function:

#len(sequence): Returns the number of items in a sequence.

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

""" Some built-in functions for sequences:
enumerate(sequence) - used in a for loop context to return two-item-tuple for each item in the list #indicating the index followed by the value at that index.

map(function, sequence) - applies the function to every item in the sequence you pass in. Returns a list of the results.

min(sequence) - returns the lowest value in a sequence.

sorted(sequence) - returns a sorted sequence

list.extend(list2) - adds all values from a second sequence to the end of the original sequence.

list.pop(index) - remove a value at given position. if no parameter is passed, defaults to final value in the list.

list.index(value) - returns the index position in a list for the given parameter. """


""" Range with 3 arguments:
Start: Inclusive of 1st
Stop: Exclusive of 2nd
Step: Interates by 3rd """
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


""" For Loops through Strings
Since a loop can be used on any sequence, you can access each value of a string individual with loop. """

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'


""" For Loops through Lists
If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly! """

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

""" For Loops through Dictionaries
Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary. """

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

""" That means if we want the values of our dictionary, we might do something like this: """

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

""" Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding: """

capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

for item in capitals.values():
    print(item)
#prints out tuples for each key:value pair