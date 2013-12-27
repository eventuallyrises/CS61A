# List comprehensions allow putting a for loop, if statements, and assignment all on one line
# allows to map and filter a list in a single expression

# List comprehensions consist of:
#  1.  Input Sequence
#  2.  Variable representing the members of the Input Sequence
#  3.  An Predicate expression (optional)
#  4.  An Output Expression producing elements of the output list from members of the Input 
#      sequence that satisfy the predicate


# Problem: Which months are safe to eat shellfish, based on 
#          old wive's tale of only eat in months containing "R"

# Original Code
months = ['January', 'February', 'March', 'April', 'May', 
          'June', 'July', 'August', 'September',
          'October', 'November', 'December']
selected_months = []

for month in months:
    if 'r' in month:
        selected_months.append(month)

print('Original List:', months)

print('Shellfish months')
print('----------------')
print('--> Using FOR Loop + IF <-- \n', selected_months)


# Version 2, Using list comprehensions
# Structure of List Comprehension statement
# [ output exp for element in sequence (optional predicate expression)]
#   ---------- -----------------------  -----------------------------
#       ^              ^                    ^
#       |              |                    |
# [  month      for month in months      if 'r' in month  ]

shellfish_months = [month for month in months if 'r' in month]
print('\n --> Using List Comprehension <-- \n', shellfish_months)

# Downside to using List Comprehensions
# ---> Entire list must be stored in memory at once.
# Solution: use generator
# --> A generator has the same general syntax, but put in parenthesis
#     rather than brackets

# turn shellfish_months into a generator object instead
shellfish_months = (month for month in months if 'r' in month)
print('\n --> now with more generator <-- \n', list(shellfish_months))



    




