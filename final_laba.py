print("Variant №11 , student Karpilov V.I КМ-82")
print("________________________________________")

def toFixed(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

flag = True;
while(flag):
    print("Enter number of program (1,2,3),")
    print("or 0 for exit")
    number = input()
    if(number=="1"):
        print("*     *")
        print(" * * * ")
        print("  * *  ")
    elif(number=="2"):
        while True:
            try:
                minutes_limit = float(input("Enter number if minutes(A)"))
                break
            except:
                print("A must be a number")
        while True:
            try:
                tarif_price = float(input("Enter a price(В)"))
                break
            except:
                print("B must be a number")
        while True:
            try:
                used_minutes = float(input("Number of used minutes(c)"))
                break
            except:
                print("С Must be a number")
                    
        pay=0
            
        if(used_minutes > minutes_limit):
            pay = minutes_limit*tarif_price
            used_minutes -= minutes_limit
                
        pay += used_minutes*3
        print("Pric:",pay)
        print("____________")
            
    elif(number=="3"):
        try:
            value = int(input("Enter number:"))
        except:
            print("Error")
        if(value>=(-3.5)):
            print("Result:",4*(value**2)+2*value-19)
        else:
            print("Rsult:",toFixed(-((2*value)/((-4)*value + 1)),3))
    elif(number=="0"):
        flag = False
    else:
        print("You have entered an invalid number")
