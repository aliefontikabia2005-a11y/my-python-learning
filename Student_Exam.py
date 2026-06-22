customers=["jariatu","esther","dija","abu","ishamel","alpha","ij","shaggi","staven","abibatu","alima","bakarr"]
completed_sales=[]
cancelled_sales=[]

user_name=input("What is your name?:")
print(f"{user_name} Welcome to the:")

while True:
    print("=========================\ntop_up business manager\n=========================".title())
    print("\n1.view waiting customer\n2.add new customer\n3.complete top-up sale\n4.cancle customer order\n5.correct customer name" \
    "\n6.sort customers A-Z\n7.reverse customer list\n8.show business statistics\n9.view complete sales\n10.view cancelled sales\n11.exit".title())

    manue=input("enter the following manue:\n".title())
    if manue.isdigit():
        option=int(manue)

    if option==1:
        print(f"view waiting customer:\n{customers}")

    if option==2:
        Add=input("enter new costomer:")
        if Add in customers:
            print("name alrady the the list")
        else:
            customers.append(Add)
            print(f"{Add} has been added to waiting costomer list:\n{customers}")

    if option==3:
        print(f"costomer {customers}")
        Sell=int(input("enter customer index:".title()))
        Sell1=customers.pop(Sell)
        print(customers)
        completed_sales.append(Sell1)
        print(f"you have complete sale with {Sell1}\ncompleted_sale list:\n{completed_sales} ".title())

    if option==4:
        cancle=input("enter cancle customer:".title())
        if cancle in customers:
            customers.remove(cancle)
            #print(customers)
            cancelled_sales.append(cancle)
            print(f"{cancle} has been remove from the customer list and add to cancle_sale list:\n{cancelled_sales}".title())
        else:
            print(f"{cancle} is not in the list ")

    if option==5:
        change=int(input("enter the index of the customer you want to change:".title()))
        change1=input("now enter the new name you want to give that customer:".title())
        customers[change]=change1
        print(customers)

    if option==6:
        customers.sort()
        print(f"organise list from A-Z:\n{customers}".title())

    if option==7:
        customers.reverse()
        print(f"reversr from Z-A:\n{customers}")

    if option==8:
        count=f"total waiting customer:\n{len(customers)}\ntotal completed sales:\n{len(completed_sales)}\ntotal cancelled sales:\n{len(cancelled_sales)}"
        print(count.title())

    if option==9:
        print(completed_sales)

    if option==10:
        print(cancelled_sales)

    if option==11:
        Exit=input("are you want to exit? y/n:".title())
        if Exit=="y":
            break
        


   
       