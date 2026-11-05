
def inmat(txt):
    while True:
        svar = input(txt).lower()
        if svar in ["sten", "sax", "påse"]:
            return svar 
        else:
            print("Ogiltig inmatning")

while True:
    try: 
        x_omgångar = int(input("Hur många omgångar vill du spela? -->"))
        if x_omgångar > 0:
            break
        else: 
            print("Ange minst 1 omgång!")
    except ValueError:
        print("ogiltig inmatning, skriv ett heltal")
