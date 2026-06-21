Available_cards=["Orange-100","Orange-500","Africell-1000","Qcell-500"]
Sold_cards=[]
Expired_cards=[]

user_name=input("enter user name:".title())
print(f"{user_name} welcome to the:\n===========================\ntop business management app\n===========================\n".title())
print("1.view available cards\n2.add new card\n3.sell card\n4.expire card\n5.sort cards\n6.reverse cards\n7.count cards\n8exit".title())

while True:
    option=input("enter the following option above".title())
    if option.isdigit():
        option=int(option)
    else:
        print("number only")

    if option==1:
        print(f"view cards {Available_cards}")

    if option ==2:
        Add=input("add new card:")
        Available_cards.append(Add)
        print(f"{Add} has been add to the available_cards list: \n{Available_cards} ")
    if option==3:
        sell=int(input("enter the number you want to sell:\n".title()))
        sell1=Available_cards.pop(sell)
        Sold_cards.append(sell1)
        print(f"the index {sell} ({sell1}) has been sold:\n and it is in the sold list {Sold_cards}".title())

    if option==4:
        Expired=int(input("enter expired index (number):"))
        Expired1=Available_cards.pop(Expired)
        #if Expired in Available_cards:
        Expired_cards.append(Expired1)
        print("expired card list",Expired_cards)

    if option==5:
        order=input("are you sure you want to arrange the list in alphabetal order:(y/n)".title())
        if order=="y":
            print(sorted(Available_cards))

    if option ==6:
        Available_cards.reverse()
        print("reverse",Available_cards)

    if option==7:
        count=f"Available card:\n{len(Available_cards)}\nsold card:\n{len(Sold_cards)}\nexpire card:\n{len(Expired_cards)}"
        print(f"total:\n{count}")

    if option==8:
        print("Exit")
        break


