# ----------------------------------SESSION 1---------------------------------------------------------

'''
Problem 1: Hundred Acre Wood
Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
'''

def welcome():
    print("Welcome to The Hundred Acre Wood")

welcome()

'''
Problem 2: Greeting
Write a function greeting() that accepts a single parameter, a string name, 
and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
'''

def greetings(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")

'''
Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character	            Catchphrase
"Pooh"	                "Oh bother!"
"Tigger"	            "TTFN: Ta-ta for now!"
"Eeyore"	            "Thanks for noticing me."
"Christopher Robin"	    "Silly old bear."

If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"
'''

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("Oh bother!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

'''
Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.
'''
def get_item(items, x):
    length = len(items)

    if x >= length:
        return print(None)
    else:
        return print(items[x])

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

'''
Problem 5: Total Honey
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

'''

def sum_honey(hunny_jars):
    sum = 0
    length = len(hunny_jars)
    for i in range(0, length, 1):
        sum = sum + hunny_jars[i]
    print(sum)


hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

'''
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
'''
def doubled(hunny_jars):
    mult = 0
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    return print(hunny_jars)


hunny_jars = [1, 2, 3]
doubled(hunny_jars)

# ----------------------------------SESSION 2---------------------------------------------------------
'''
Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.
'''

def reverse_sentence(sentence):
    split = sentence.split()
    new = []
    for i in range(len(split) -1, -1, -1):
        new.append(split[i])
    return print(' '.join(new))

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)