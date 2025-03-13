
#-------------------------SESSION 1-----------------------------------------------------------------------

'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

1. Every opening tag has a corresponding closing tag of the same type.
2. Tags are closed in the correct order.
'''
def is_valid_post_format(posts):

    # Initialize a stack to keep track of the opening tags as you encounter them.
    stack = []
    # Iterate through the posts
    for i in range(len(posts)):
    # If it's an opening tag, push it onto the stack
        if (posts[i] == "(") or (posts[i] == "[") or (posts[i] == "{"):
            stack.append(posts[i])
    # If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag
        elif (posts[i] == ")"): 
            if stack[-1] == "(":
    # If yes, pop the opening tag from the stack (we've found its match!)
                stack.pop()
        elif (posts[i] == "]"):
            if stack[-1] == "[":
                stack.pop()
        elif (posts[i] == "}"):
            if stack[-1] == "{":
                stack.pop()

    # If no, the tags are not properly nested and we should return False
            
    # After processing all characters, if the stack is empty, all tags were properly nested and we should return True. If the stack is not empty, some opening tags were not closed, so return False
    if not stack:
        return True
    else:
        return False
print("---------Problem 1.1----------")
print(is_valid_post_format("()")) #True
print(is_valid_post_format("()[]{}")) #True
print(is_valid_post_format("(]")) #False

'''
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.
'''

def reverse_comments_queue(comments):
    stack = []
    stack2 = []

    for i in range(len(comments)):
        stack.append(comments[i])

    for i in range(len(stack), 0, -1):
        popped = stack.pop()
        stack2.append(popped)
    return stack2

print("---------Problem 1.2----------")
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))# ['Thanks for sharing.', 'Love it!', 'Great post!']
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))# ['Well written.', 'Interesting read.', 'First!']

'''
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
'''

def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ", "")

    right_pointer = len(title) - 1
    left_pointer = 0

    while left_pointer < right_pointer:
        if title[left_pointer] != title[right_pointer]:
            return False
        elif title[left_pointer] == title[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
    return True

print("---------Problem 1.3----------")
print(is_symmetrical_title("A Santa at NASA"))# True
print(is_symmetrical_title("Social Media")) # False

'''
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
'''
# def engagement_boost(engagements):
#     squared_engagements = []
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     squared_engagements.sort(reverse=True)
    
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1

    result_2 = []

    left_pointer = 0
    right_pointer = len(engagements) - 1

    while left_pointer < right_pointer:
        if squared_engagements[left_pointer] > squared_engagements[right_pointer]:
            temp = squared_engagements[left_pointer]
            squared_engagements[left_pointer] = squared_engagements[right_pointer]
            squared_engagements[right_pointer] = temp

            left_pointer += 1
            right_pointer -= 1

    for squared, _ in squared_engagements:
        result_2.append(squared)
    return result_2

print("---------Problem 1.4----------")
print(engagement_boost([-4, -1, 0, 3, 10])) # [0, 1, 9, 16, 100]
print(engagement_boost([-7, -3, 2, 3, 11])) # [4, 9, 9, 49, 121]

#-------------------------SESSION 2-----------------------------------------------------------------------
'''
Problem 1: Manage Performance Stage Changes
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.
'''

def manage_stage_changes(changes):
    #stack
    canceled_stack = []
    scheduled_stack = []

    #iterate over changes
    for change in changes:
        if change == "Cancel" and len(scheduled_stack) > 0:
            canceled_stack.append(scheduled_stack.pop())
        elif change == "Reschedule":
            scheduled_stack.append(canceled_stack.pop())
        else:
            scheduled_stack.append(change)
    return [letter[-1] for letter in scheduled_stack]

print("---------Problem 2.1----------")
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

