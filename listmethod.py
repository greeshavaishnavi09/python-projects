nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

#  I want 'n' for each 'n' in nums if 'n' is divisible by 3
my_list = []
for n in nums:
    if n%3 == 0:
        my_list.append(n)
print(my_list)        

# I want a (letter , num) pair for each other where letter as 'abcd' and num as 0123
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)        


