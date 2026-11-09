mig = 0
dator = 0
print ("välkommen, mit namn är vecktorbot2000 (jag kommer att vinna)")

mit_namn = input("vad är dit episka namn -o-o-> ")

import random
#vad vill jag ha för sak 
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
    except ValueError:   # om du spränger dig sjäv kör om. 
        print("ogiltig inmatning, skriv ett heltal")



for i in range(x_omgångar):
    dsvar = random.randint(0,2)
    if dsvar == 0:
        dsvar = "sten"
    elif dsvar ==1:
        dsvar = "sax"
    elif dsvar == 2:
        dsvar = "påse"
    print (f"spelomgång nr {i+1}\n {"-"*30} ")
    mitsvar = inmat("välj gärna mällan sten sax eller påse ->")
    
    print (f"vecktorbot2000 väljer ! {dsvar}")
    print (f"{mit_namn} spelade {mitsvar}")
    
    if mitsvar  == dsvar:
        print("oavgjort")
    elif mitsvar == "sten" and dsvar== "sax":
        print ("du har vunnit")
        mig = mig + 1 
    elif mitsvar == "sax" and dsvar == "påse":
        print ("du vannn")
        mig = mig +1
    elif mitsvar == "påse" and dsvar== "sten":
        print ("har vunnit")
        mig = mig+1
    else:
        dator = dator + 1
        print ("vecktorbot2000 har vunnit")
        
print("du har vinnit ",f"{mig}","gånger", f"och vecktorbot2000 har vunigt {dator}")

print(f"SLUTGILTIGARESULTATET!!!\n {"="*20}\n vecktorbot2000:{dator}p \n {mit_namn}: {mig}p ")

if mig > dator:
    print (f"{mit_namn} är vinnaren !!! tjoho!    och ")
elif mig < dator:
    print (f"vecktorbot är vinnaren !! yippi!!")
else :
    print ("ingen vinnare oavgjort")


















