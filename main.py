
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

print("hello world")print(" haha du är dum ")
# tillervka sten saks eller påse 
# #sten sten>sax>påse>sten   
# #V = antal vinster du har vunnigt 
# #Datorgissning= inport ( mellen 1 -3)
import random as rand
rand = rand.randint(0, 99)
rand = rand.randint(0, 2)
gissning = input("vilken gissning tack \n 'sten' 'sax' 'påse'--->")
print(rand)

gissning = input("'sten' 'sax' 'påse'")


print (rand)