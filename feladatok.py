import random
def feladat1():
    szam:float =float(input("Adj meg egy páratlan számot:"))
    while szam%2==0:
        szam:float =float(input("Adj meg egy páratlan számot:"))
        
def feladat2():
    i:int = 0
    db:int=0
    while (i<7):
        szam:int =int(random.random()*96)+5
        print(szam)
        if(szam%5==0):
            db+=1
        
        i+=1
    print(f"A számok között  {db} db 5-tel osztható van!")

        
def feladat3(text, betu):
    '''hossz=len(text)
    i:int = 0
    while (hossz[i]):
        if
        i+=1
    print(f"A szövegben {betu} db 'a' betű van")'''

    betu = "a"
    for i in range(256):  
        if i == betu:
            betu = chr(i)
            break
    

    text = text.lower()
    betu = betu.lower()
    
    
    darab = 0
    for karakter in text:
        if karakter == betu:
            darab += 1
    print(f"A szövegben {darab} db '{betu}' betű van.")
    

    
    
def feladat4():
        print()


        
    

