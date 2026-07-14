lists = ["sumit","Sumit","sumit123","suMIT","Sumit@123","1234"]

for char in lists:
    if char.isalpha():
       print("Alpha")
    elif char.isdigit(): 
        print("Digit")
    elif char.isalnum():
        print("Alphanum")
    elif char.islower():
        print("Lower")
    else:
        print("Special values")
