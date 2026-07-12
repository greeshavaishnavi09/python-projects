#Password Validaton

#Minimum 8 characters
#One uppercase
#One lowercase
#One digit

#Return Valid or Invalid.

password= input("Enter a password:")
password_length = len(password)
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)
num = any(char.isdigit() for char in password)

if password_length >= 8 and uppercase and lowercase and num:
    print("valid password")
else:
    print("Invalid password")    