print'Lab04: Data Structures'

print
groceries = ['bananas','strawberries','apples','bread']

print'------------------------Lab04_1a-------------------------'
print
#adding champagne to the end of the list

groceries.append('champagne')
print'The new list of groceries are: '
for items in groceries:
    print '\t',items

print
print'------------------------Lab04_1b-------------------------'
print

#removing bread from the groceris list
print'The new list of groceries are: '
groceries.remove('bread')
for items in groceries:
    print '\t',items

print
print'------------------------Lab04_1c-------------------------'
print

print'Messi can create a dictionary where',
print'the keys are the items and the aisles are the values'
item = raw_input('Please enter your item here: ')
print''

aisles = {'bananas':'b','strawberries':'s','apples':'a','bread':'b'}
print item, 'is in', aisles[item],'aisle'
