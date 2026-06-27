name = input("what's your name? ")

match name:
    case "Greesha" | "Vaishu" | "Mittu":
        print("Hyderabad")
    case "Gunnu":
        print("Vizag")
    case _:
        print("who?")