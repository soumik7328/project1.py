import random
lst1=["RAEHTF","KABRE","OUSMIK","RENEG","OAERELANP","NANBAA","LPEPA","RAKM","IRSGYM","ESOUH","UOYBEUT","KOOB","UBS"]
st1={"FATHER","BRAKE","SOUMIK","GREEN","AEROPLANE","BANANA","APPLE","MARK","MYSIRG","HOUSE","YOUTUBE","BOOK","BUS","SUB"}
while True:
    ucount=0
    uc=int(input('''
Game Start....
1 Yes
2 No | Exit    
        '''))
    if uc==1:
        print("Arrange the latter to form a valid word")
        for a in range(1,6):
            
            cchoice=random.choice(lst1)
            print(cchoice)
            uchoice=input().upper()
            if uchoice in st1:
                print("\ncorrect\n")
                ucount+=1
            else:
                print("\nWRONG\n")
                ucount-=1
    else:
        break            
    print("Net Score is ",ucount) 
