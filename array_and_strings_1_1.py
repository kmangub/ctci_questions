# 1.1 Implement an algorithm to determine if a string has all unique characters. what if you cannot use aditional data structures

#Input takes in a string
#output is True or False

#Algorithm. First we want to iterate through each character of the string.

def unique_characters(string):
  each_char = []
  unique = True

# We want to iterate through the string
  for char in string:
    # The if statement checks to see if the character exists in our list and will change the status of unique 
    if char in each_char:
      unique = False
    # appends the char to the array
    else:
      each_char.append(char)

  return unique
      
# tests
print(unique_characters('abcde'))


#Solution
#Clarify if the string is ASCII or Unicode string

#  American Standard Code for Information Interchange (ASCII) is code used to represent characters