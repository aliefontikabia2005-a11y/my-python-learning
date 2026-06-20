SECRET_NUMBER='7'#the game secreat number
attempt=3# how many attempt did you have

# welcome message to the player
print("welcome to the guessing game!!!!\n".upper())
#Ask the player for there name
user_name=input("what is your name player:".title())
 
# the loop that run the program
while attempt:
  attempt-=1
  # Ask the player to guess of any number :
  guessing_number=input(f'{user_name},guess of any number you think the computer is hidden from you:===>'.title())
  if guessing_number.isdigit():
    guessing_number=str(guessing_number)
  else:
       print("the game allow number only ")
 # if the number the user enter is the same, respon to the user with a congulations message
  if guessing_number==SECRET_NUMBER:
    print("congulations".title())
    break
  else:
     # else if player_number is grater than the hidden number, 
    if SECRET_NUMBER>guessing_number:
            
        # tell the player that the number is to high, and they should try again
         print(f"{guessing_number} is too high")
         print(f"{attempt } attempt left\ntry again {user_name}\n\t".title())
        

   # else if player_number is less than the secreat number,
    elif SECRET_NUMBER<guessing_number:
           # tell the player that there number is to low,they should try again
           print(f"{guessing_number} is too low:")
           print(f"{attempt} attempt left\ntry again {user_name}\n\t ".title())

     