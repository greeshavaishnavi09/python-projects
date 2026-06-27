def main():
    x = int(input("what's x?"))
    if is_odd(x):
        print("odd")
    else:
        print("even")

def is_odd(n):
    return n % 3 == 0
        
    
main()     