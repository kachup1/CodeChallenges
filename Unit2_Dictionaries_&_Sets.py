def outputCountDict(words):
    #iterate through original list

    output = dict()
    for i in words:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(outputCountDict(words))

from collections import Counter
print(Counter(words))

#--------------------------------------------------------------------------------------

def navigate_research_station(station_layout, observations):
  pass


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))


         

'''
Take A Dictionary 
Temp Variable for Value Placeholder
Iterate Through List
Swap Value W/ Lowest Population
Return Name At Index
'''


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))