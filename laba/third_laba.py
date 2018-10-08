import time
delay = 2

End = False
while(not End):
    words = input("Enter words, splited by space : ")
    if(len(words)==0):
        print("You have entered void")
        continue
    words = words.split(" ")
    Entered = False
    
    while(not Entered):
        try:
            indicator = int(input("Enter len : "))
            Entered = True
        except:
            print("You hane entered wron simbol")
    
    for i in range(len(words)):
        if(len(words[i]) == indicator - 1):
            words[i] = words[i][:2] + "  " + words[i][2:]
        else:
            pass

    print(words)
    
    Answered = False
    while(not Answered):
        answer = input("You want to exit ?(yes/no) : ")
        if(answer=="yes" or answer=="Yes" or answer=="YES"):
            Answered = True
            End = True
        elif(answer=="no" or answer=="No" or answer=="NO"):
            Answered = True
        else:
            print("This was something strange")
            pass
print("Good luck")
time.sleep(delay)
            
