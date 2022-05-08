import random
numbers = [1, 2, 3]
#  new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
range_list = [n*2 for n in range(1, 5)]

# new_list = [new_item for item in list if test]
names = ["basem", "alex", "mark", "ahmed", "salma"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) >= 5]

# Code challenge
List_1 = open('file1.txt').read().splitlines()
List_2 = open('file2.txt').read().splitlines()
result = [int(n) for n in List_1 if n in List_2]
# Write your code above 👆
print(result)

#  dictionary comprehension

# new_dictionary = {new_key:new_value for item in list}
# new_dictionary = {new_key:new_value for (key, value) in dict.items()}
# new_dictionary = {new_key:new_value for (key, value) in dict.items() if test}

#  Dictionary challenge 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
result = {word:len(word) for word in sentence.split()}
print(result)
#  Dictionary challenge 2
names = ["alex", "ahmed", "caroline", "dave", "basem"]
student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

#  how to iterate over a pandas dataframe
# for (index, row) in Pandas.Dataframe.iterrows():
#   print(row.score)

