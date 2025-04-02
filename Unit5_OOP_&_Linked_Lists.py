'''
python

class Dog:
    def __init__(self, name, breed, language='English'):
        self.name = name
        self.breed = breed
        self.language = language

    def bark(self):
        if self.language == 'English':
            return "Woof"
        elif self.language == 'Korean':
            return "Mong Mong"
        elif self.language == 'Hindi':
            return "Bhaw Bhaw"
        else:
            return "..."

fido = Dog('fido', 'lab', 'English')
mandoo = Dog('mandoo', 'jindo', 'Korean')
ladoo = Dog('ladoo', 'Himalayan', 'Hindi')


# print(f"{fido.name} is a {fido.breed} and says {fido.bark()}")
# print(f"{mandoo.name} is a {mandoo.breed} and says {mandoo.bark()}")
# print(f"{ladoo.name} is a {ladoo.breed} and says {ladoo.bark()}")


# # Node class for Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List Class
        
class LinkedList:
    def __init__(self):
        self.head = None # first node
        self.tail = None # last node

    def add(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def print(self):
        result = ''

        current = self.head

        while current:
            result += str(current.value)
            if current.next:
                result += ' -> '

            current = current.next
        
        print(result)

# dog_node1 = Node(f"{fido.name}")

# print(f"{dog_node1.value}")
        
pet_list = LinkedList()
pet_list.add(f"{fido.name} says {fido.bark()}")
pet_list.add(f"{ladoo.name} says {ladoo.bark()}")
pet_list.add(f"{mandoo.name} says {mandoo.bark()}")

pet_list.print()
             
print(pet_list.tail.next)
'''

# from collections import defaultdict

# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items=[]
#     def get_player(self):
#         return f"{self.character} driving the {self.kart}"
#     def set_character(self, name):
#         names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
#         if name in names:
#             print("Character Updated")
#         else:
#             print("Invalid Character")
#     def add_item(self, item_name):
#         item=["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
#         if item_name in item:
#             self.items.append(item_name)
#     def print_inventory(self):

#         #expected output: 
#         # Inventory: banana: 2, bob-omb: 1, super star: 1
#         if len(self.items)==0:
#             print ("Inventory empty")
#         else:
            
#             freq_map = defaultdict(int)
#             for item in self.items:
#                 freq_map[item] += 1
            
# player_one = Player("Yoshi", "Dolphin Dasher")

# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)

#-----------------------------------------------------------------------------------------------

print("-----------------Problem 1.1 Session #1----------------------------------------------------------")
'''
Standard Problem Set Version 1
Problem 1: New Horizons
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# Instantiate your villager here

apollo = Villager("Apollo", "Eagle", "pah")
#Example Usage:
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
# Example Output:
# Apollo
# Eagle
# pah
# []

print("-----------------Problem 1.2 Session #1----------------------------------------------------------")
'''
Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip")

#Example Usage:
print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
print(bones.greet_player("Karla"))

# Example Output:
# Bones
# Dog
# yip yip
# []

print("-----------------Problem 1.3 Session #1----------------------------------------------------------")
'''
Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"

#Example Usage:
print(bones.greet_player("Samia"))
# Example Output:
# Bones: Hey there, Samia! How's it going, ruff it up!

print("-----------------Problem 1.4 Session #1----------------------------------------------------------")
'''
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def set_catchphrase(self, new_catchphrase):

        catchphrase_length = len(new_catchphrase)
        
        if not new_catchphrase:
            return print("Invalid catchphrase")
        elif catchphrase_length < 20 and isinstance(new_catchphrase, str) and  new_catchphrase.replace(" ", '').isalpha():
            print("Catchphrase updated!")
            self.catchphrase = new_catchphrase
        else:
            return print("Invalid catchphrase")

#Example Usage:
alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
# Example Output:
# Example 1:
# Catchphrase Updated!
# sweet dreams
# Invalid catchphrase
# sweet dreams

print("-----------------Problem 1.5 Session #1----------------------------------------------------------")
'''
Problem 5: Add Furniture
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".
'''
class Villager:
    # ... methods from previous problems
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    # New method
    def add_item(self, item_name):
        valid_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in valid_furniture:
            self.furniture.append(item_name)
        else:
            return None

#Example Usage:
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
# Example Output:
# []
# ["acoustic guitar"]
# ["acoustic guitar", "cacao tree"]
# ["acoustic guitar", "cacao tree"]

print("-----------------Problem 1.6 Session #1----------------------------------------------------------")
'''
Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
'''

class Villager():
    # ... methods from previous problems
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    # New method
    def add_item(self, item_name):
        valid_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in valid_furniture:
            self.furniture.append(item_name)
        else:
            return None
    
    def print_inventory(self):
        # Implement the method here
        dict =  {}
        quantity = 1
        if not self.furniture:
            return print("Inventory empty")

        for item in self.furniture:
            if item not in dict:
                dict[item] = quantity
            else:
                dict[item] = quantity + 1
        return print(dict)

#Example Usage:
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory() 

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

# Example Output:
# Inventory empty
# acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2

print("-----------------Problem 1.7 Session #1----------------------------------------------------------")
'''
Problem 7: Group by Personality
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.
'''
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):

    matching_villagers = []
    
    for villager in townies:
        if villager.personality == personality_type:
            matching_villagers.append(villager.name)
    return matching_villagers

    
#Example Usage:
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
# Example Output:
# ["Bob", "Stitches"]
# []

print("-----------------Problem 1 Session #2----------------------------------------------------------")
'''
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list with the name of all friends the current villager and new_contact have in common.
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        myList = []

        for i in new_contact.friends:
            if i in self.friends:
                myList.append(i.name)
        return myList

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")


bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

# Example Output:
# ['Raymond', 'Fauna']
# []

'''
Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("Kk_slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

#Example Usage:
print("-----------------------------------Problem 2 Session #2-----------------------------------------------")
print_linked_list(kk_slider)
#Example Output:
#K.K. Slider -> Harriet -> Saharah -> Isabelle

'''
Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task. Write a function add_task() that takes in the head of a linked list and adds a new node to the front of the task list.

The function should insert a new Node object with the value task as the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_first(head, task):
    t = Node(task, head)
    head = t   
    return head
    

#Example Usage:
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

print("-----------------------------------Problem 3 Session #2------------------------------------------------------------")
# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))
#Example Output:
#check turnip prices -> shake tree -> dig fossils -> catch bugs

'''
Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two. Return the head of the modified list.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def halve_list(head):
    pass
#Example Usage:
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

print("-----------------------------------Problem 4 Session #2------------------------------------------------------------")
# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))
# Example Output:
# 2.5  -> 3 -> 3.5




