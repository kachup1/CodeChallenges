#Notes 

# def recursive_sum(num):
#     if num <= 1:
#         return num
#     return num + recursive_sum(num - 1)

# result = recursive_sum(5)
# print(result) #Output: 15
'''
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
'''
def count_suits_iterative(suits):
    count = 0
    for s in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    
    if suits == []:
        return 0
    else:
        return 1 + count_suits_iterative(suits[1:])
#Example Usage:
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))# 3
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))# 4

'''
Problem 2: Collecting Infinity Stones
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
'''
def sum_stones(stones):
    if stones == []:
        return 0
    else:
        return stones[0] + sum_stones(stones[1:]) 
#Example Usage:
print(sum_stones([5, 10, 15, 20, 25, 30]))#105
print(sum_stones([12, 8, 22, 16, 10]))#68

'''
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
'''

def count_suits_iterative(suits):
    unique_suit = []
    for i in suits:
        if i not in unique_suit:
            unique_suit.append(i)
    return len(unique_suit)

def count_suits_recursive(suits):
    unique_suits = []
    if suits == []:
        return 0
    else:
        unique_suits.append(suits[0])
        count_suits_recursive(suits[1:])
    return len(unique_suits)

#Example Usage:
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))#3
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))#2


print("____________________________________________")
'''
Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.

'''
'''understand
we have an target cruise_length and a list of cruise lenghts
use binary search to find the cruise_length in the list or return false if it's not there
'''
'''Plan
    find the midpoint
    check if the midpoint less than the target
    set the left pointer by mid+1
    if it's less than the target
    set the right to mid-1
    if midpoint == target:
    return True
    
    if left > right:
        return False
    
'''

def find_cruise_length(cruise_lengths, vacation_length):
    mid = len(cruise_lengths)//2
    print(cruise_lengths)
    if mid == 0 and cruise_lengths[mid] != vacation_length:
        return False
    if cruise_lengths[mid] == vacation_length:
        return True
    elif cruise_lengths[mid] > vacation_length:
        return find_cruise_length(cruise_lengths[:mid], vacation_length)
    elif cruise_lengths[mid] < vacation_length:
        return find_cruise_length(cruise_lengths[mid+1:], vacation_length)
    else:
        return False




print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

'''
find the mid = (left+right)//2
add if statement if the mid is found we return mid 
elif statement if the mid < preffered deck we push left closer to the right 
else: right closer to the left 
'''

def find_cabin_index(cabins, preferred_deck,left=0,right=None):
    
    if right == None:
        right=len(cabins)-1
    
    if left > right:
        return left  
    mid = (left+right)//2

    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] < preferred_deck:
        return find_cabin_index(cabins,preferred_deck,mid+1,right)
    else:
        return find_cabin_index(cabins,preferred_deck,left,mid-1)
    



print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

# 2
# 1
# 4


'''
As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.

Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.
'''


# def count_checked_in_passengers(rooms, count=0, left=0, right=None):
#     mid = (left+right) // 2
    
#     if right == None:
#         right=len(rooms)-1
#     if left > right:
#         return count
    
#     if rooms[mid] == 1:
#         count += 1
#         return 
#     else:
#         return find_cabin_index(rooms,count,left,mid-1)
    
    
# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))