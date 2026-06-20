Living_Rabbit=["RabbitV",
"RabbitA",
"RabbitB",""
"RabbitF"]

sold_Rabbit=[]

Dead_Rabbit=[]



while True:
    # Ask the user for there name
    famer_name=input("what is your name?")
    #welocme them to the rabbit app
    print(f"{famer_name.title()} Welcome To:\n==============================\nJOY BOY  RABBIT FARM MANAGER\n==============================\n")
    # show the manue option that they enter
    user=input("enter the following manue below:\n1.viwe living rabbit\n2.add rabbit\n3.sell rabbit\n4.record dead rabbit\n5."
    "rename rabbit\n6.sort rabbits\n7.reverse rabbits\n8.count rabbits\n9.view sold rabbits\n10.view dead rabbits\n11.Exit:\n".title())
        
    if user.isdigit():# this allow only the user to enter digit(number)
        option=int (user)# convert the user input to integer(number),and store it in option variable
        if option==1:# if the user option is 1 show the original list
            print(Living_Rabbit)

    else:
        print("system only allow number")
         
        #Add Rabbit
    if option==2:# if the user option is 2 ,
            Ask=input("enter rabbit name you want to add:".strip().title())# Ask for the name of rabbit they want to put
            if Ask.isalpha():#this allow only the user to enter digit(number)
                Living_Rabbit.append(Ask)# add user input to the Living_Rabbit
                #print(Living_Rabbit)
                print(f"{Ask} have just been added successfully in Living_Rabbit:\n {Living_Rabbit}")# show it ha been add successrully
            else:
                print("the system only allow number")
     # Sell Rabbit
    if option==3:
          sell=input("enter the rabbit you want to sell:".title())
          
          if sell in Living_Rabbit:# if the user rabbit is in Living rabbit list
             #print(Living_Rabbit)
             Living_Rabbit.remove(sell)# Remove it from the Living rabbit list
             print("Living:\n",Living_Rabbit)# show that the rabbit has been remove
             sold_Rabbit.append(sell)# Add to the sold_Rabbit list
             print("sold:\n",sold_Rabbit)# show the sold list
          else:
              print(f"{sell} is not in rabbit list")

    # Dead Rabbit
    if option==4:
        Dead=input("enter the rabbit that died:".title())# ask the user to enter the rabbit that dead
        if Dead in Living_Rabbit:# check if the dead rabbit is in Living_Rabbit list:
            Living_Rabbit.remove(Dead)#Remove the dead rabbit from the Living_Rabbit:
            print("living",Living_Rabbit)# show the living rabbit for conformation
            Dead_Rabbit.append(Dead)# add the dead rabbit to Dead_Rabbit list
            print(f"Dead:{Dead_Rabbit} marked as dead.")# show evidence that the rabbit is the Deadlist
        else:
            print(f"{Dead}: this rabbit is not in the list")# if rabbit is not in Dead list show the rabbit is not there
    #Rename Rabbit
    if option==5:  
        # show output that allow user to enter the rabbit thay want to change
        name=input("enter the  name of the rabbit you want to change:".title())
        
        if name in Living_Rabbit:#check if rabbit is in Living_Rbbit
            new_name1=input("enter new name:".title())
            Living_Rabbit.remove(name)#remove the  name from the Living rabbit list
                #print(f"{new_name1}: has been added")
            Living_Rabbit.append(new_name1)# add the new name to the rabbit
            print(f"rabbit {name} has been change to {new_name1}\n")
            print(f"{new_name1} has been added to this list:{Living_Rabbit}")# show that new rabbit 
    # sort (arrange Alphabetical order)
    if option==6:
        Arange=input("are you sure you want to  arange the list is an alphabetcal order:(y/n)".title())# ask to user to choose (y/n) for comformation
        if Arange=="y":# if user choose y
         print(sorted(Living_Rabbit)) # show the arrange list
    #Reverse Rabbit
    if option==7:
        Living_Rabbit.reverse()
        print(f"reverse_list {Living_Rabbit}")
        
     #count Rabbit   
    if option==8:
        count=f"Living Rabbit:{len(Living_Rabbit)}\nSold Rabbit:{len(sold_Rabbit)}\nDead Rabbit:{len(Dead_Rabbit)}"

        print(f"total amount of rabbit is:\n{count}".title())

    # View Sold Rabbits
    if option==9:
        print(f"list of sold rabbits {sold_Rabbit}".title())

    # View Dead Rabbits:
    if option==10:
        print(f"list of dead rabbits:{Dead_Rabbit}".title())

    # Exit:
    if option==11:
        print("system close")
        break

            
