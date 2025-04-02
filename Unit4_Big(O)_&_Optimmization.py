'''
Problem 1: Planning Your Daily Work Schedule
Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
def find_task_pair(task_times, available_time):
  sums = {}
  for time in range(0,len(task_times)):
    complement = abs(available_time - task_times[time])
    if complement in sums.values():
      return True
    sums[complement] = task_times[time]

  return False

print("----------------Problem 1---------------------------")
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time)) # True

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time)) # True

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time)) # False

'''
Problem 2: Minimizing Workload Gaps
You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def find_smallest_gap(work_sessions):
  ans = float('inf')
  aux = work_sessions[0]
  for x in range(1, len(work_sessions)):
    if ans > abs(aux[1] - work_sessions[x][0]):
      ans = abs(aux[1] - work_sessions[x][0])
      if ans > 60:
        ans -= 40
    aux = work_sessions[x]
  return ans

print("----------------Problem 2---------------------------")
work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions)) # 60

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2)) # 30

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3)) # 15

'''
Problem 3: Expense Tacking and Categorization
You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def calculate_expenses(expenses):
    categories = {}

    for i in range(len(expenses)):
      category = expenses[i][0]
      if category in categories:
          categories[category] += expenses[i][1]
      else:
        categories[category] = expenses[i][1]
        
    return (categories, max(categories, key=categories.get))

print("----------------Problem 3---------------------------")
expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses)) 
# ({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

'''
Problem 4: Analyzing Word Frequency
As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. Additionally, return a list of the word(s) that appear most frequently.

Assumptions:

The text is case-insensitive, so "Word" and "word" should be treated as the same word.

Punctuation should be ignored.

In case of a tie, return all words that have the highest frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def word_frequency_analysis(text):
  word_dict = {}
  text_list = text.split()
  for word in text_list:
    if word.lower().replace(".", "") in word_dict:
      word_dict[word.lower().replace(".","")] += 1
    else:
      word_dict[word.lower().replace(".","")] = 1
  max_freq = max(word_dict.values())
  max_words = [word for word, frequency in word_dict.items() if frequency == max_freq]
  return word_dict, max_words


print("----------------Problem 4---------------------------")
text = "The quick brown fox jumps over the lazy dog-. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))

#OUTPUTS
# ({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])
#({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1, 'their': 1, 'passion': 1}, ['travel'])
#({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])

'''
Problem 5: Validating HTML Tags
As a digital nomad who frequently writes and edits HTML for your blog, you want to ensure that your HTML code is properly structured. One important aspect of HTML structure is ensuring that all opening tags have corresponding closing tags and that they are properly nested.

Given a string of HTML-like tags (simplified for this problem), write a function to determine if the tags are properly nested and closed. The tags will be in the form of <tag> for opening tags and </tag> for closing tags.

The function should return True if the tags are properly nested and closed, and False otherwise.

Assumptions:

You can assume that tags are well-formed (e.g., <div>, </div>, <a>, </a>, etc.).

Tags can be nested but cannot overlap improperly (e.g., <div><p></div></p> is invalid).

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def validate_html_tags(html):
  stack = []
  html_list = html.split(">")
  html_dict = {"</div>" : "<div>", "</a>" : "<a>", "</p>" : "<p>"}
  for x in html_list:
    curr = x + ">"
    if curr in html_dict.values():
      stack.append(curr)
    if curr in html_dict.keys():
      if not stack or stack[-1] != html_dict[curr]:
        return False
      stack.pop()
  return not stack

print("----------------Problem 5---------------------------")
html = "<div><p></p></div>"
print(validate_html_tags(html)) #True

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2)) #False

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3)) #True

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4)) #False


'''
Problem 6: Task Prioritization with Limited Time
You often have a long list of tasks to complete, but limited time to do so. Each task has a specific duration, and you only have a certain amount of time available in your schedule. You need to prioritize and complete as many tasks as possible within the given time limit.

Given a list of task durations and a time limit, determine the maximum number of tasks you can complete within that time.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def max_tasks_within_time(tasks, time_limit):
  pass

tasks = [5, 10, 7, 8]
time_limit = 20
print(max_tasks_within_time(tasks, time_limit))

tasks_2 = [2, 4, 6, 3, 1]
time_limit = 10
print(max_tasks_within_time(tasks_2, time_limit))

tasks_3 = [8, 5, 3, 2, 7]
time_limit = 15
print(max_tasks_within_time(tasks_3, time_limit))

# Problem 6 solution is in O(nlogn) I was gonna use sort() sapce would be O(1)