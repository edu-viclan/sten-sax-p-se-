


















def inmat(txt):
    inmat_str =""
    while True:
        input(txt) == inmat_str
        if inmat_str.isalpha == True:
            return inmat_str
        else:
            print("ogiltigt inmatning")

print(inmat("välj sten, sax eller påse"))