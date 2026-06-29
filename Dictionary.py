# Dictionary comp
names = ['Greesha','Vaishnavi','Tejaswi','Gunnu']
heros = ['Superman','Spiderman','Batman','Captainamerica']

# I want dict{'name':'heros'} for each name, heros in zip(name , heros)
my_dict = {}
for names , heros in zip(names , heros):
    if names != 'Vaishnavi':
        my_dict[names] = heros
print(my_dict)    
