import random
ops = ["sten", "sax", "påse"]

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

for i in range(x_omgångar):
    print(f"Omgång {i+1}")
    val = random.randint(0,2)
    print(ops[val])
    drag = inmat("välj sten sax eller påse -->")
    if val == 0 and drag == "sten":
        print("ja")
