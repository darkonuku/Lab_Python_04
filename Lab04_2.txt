print'Lab04_32'
print
print'----------------------------Lab04_2a--------------------------'
print

print'To create the catalog,  i will use the dictionary data structure.',
print'This is because the dictionary data structure affords us a faster way',
print'to search for values based on key indeces.'



print
print'----------------------------Lab04_2b--------------------------'
print

catalog = {'Apples':'SPIC_APPLES','Bananas':'SPIC_BANANAS',\
           'Bread':'SPIC_BREAD','Carrots':'SPIC_CARROTS',\
           'Champagne':'SPIC_CHAMPAIGNE','Strawberries':'SPIC_STRAWBERRIES'}

print catalog,



print
print'----------------------------Lab04_2c--------------------------'
print


#modifying the price of strawberries

catalog['Strawberries'] = 'WPIC_STRAWBERRIES'
print catalog,



print
print'----------------------------Lab04_2d--------------------------'
print


catalog['Chicken'] = 'SPIC_CHICKEN'
print catalog,
