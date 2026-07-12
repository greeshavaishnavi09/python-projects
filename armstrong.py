num = int(input("enter a num:"))
total = sum(int(digit)** num for digit in str(num))
print(total)

if total == num:
    print("Armstrong number")
else:
    print("Not a armstrong number")
