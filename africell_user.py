BALANCE=500
buldle=["25","75","250","500"]
sole=[]
SM=["whatsApp","Facebook","TikTok","Instagram"]
Night=[" 500mb","1gb","2gb","3.34mb"]
stop="y"

while True:
    print("welcome to africell internet".title())
    print("1.check balance\n2.buy for this line\n3.buy for another line\n4.sm bundle\n5.night bundle\n6.yamix plus" \
          "7.roaming bundle\n8.kidzonet\n9.exit".title())
    
    manue=input("enter the option above:\n".title())
    if manue.isdigit():
        option=int(manue)
    
    if option==1:
        print(f"your balance is:\n {BALANCE} mb\nle 100:".title())

    if option==2:
        print("select bundle form 0-3",buldle)
        buy=int(input("choose the amount you want to by:".title()))
        buy1=buldle.pop(buy)
        print(f"you have buy {buy1} mb successfully".title())
        sole.append(buy1)
    
    if option==3:
        Other=input("enter phone number:".title())
        print(buldle)
        Other1=int(input("selcet bundle from 0-3:".title()))
        Other2=buldle.pop(Other1)
        print(f"{Other2}mb sussessfully sent to {Other}".title())

    if option==4:
        print(SM)
        print("1.view balance\n2.add new bundle\n3.remove bundle\n4.sort bundle\n".title())


    if option==5:
        print("night:\n",Night)
        Night_add=input("enter the number you want to buy ".title())
        if Night_add.isdigit():
            Night_add=int(Night_add)
        Night_add1=Night.pop(Night_add)
        print(f"you have successfully buy {Night_add1} enjoy your night")

    if option==6:
        Exit=input("are you sure?y/n:")
        if Exit==stop.strip().title():
         print("thank you for using africell:".title())
         break


        
 
