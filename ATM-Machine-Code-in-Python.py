print("\n----------------------------Welcome to the Anonymous Bank-------------------------------")
print("\nPlease Insert your ATM Card")
import time
#card = input("Insert Card")
#print(card)

        
pin = 1234 
balance = 200
option1 = 0
option2=0
option3 = 0
restart = "yes"
time.sleep(6)
i=1
pin=int(input("\nEnter your 4 DIGIT Pin: ")) 
if pin == 1234:
     while i<5:
             i = i +1
             print("\nYou Have 4 Attempts")     
             print('''
                   Chose options From These:
                   1. Add Money
                   2. Withdraw Money
                   3. Current Balance
                   4. Exit''')
             options = int(input("Chose Options: "))
             
             if options==1:
                 print("Add Money.")
                 money  = int(input("Enter Money: "))
                 balance = balance + money
                 print(f"Now your Money is {balance}$")
                 print("Thanks For Visisting our Bank")
                 
                 print("If you want to Exit press the option 4")
             #elif restart != ("N","No")
             elif options == 2:
                
                    
                  print("Withdraw Money")  
                  money=int(input("Enter Amount: "))
                  if money<balance:
                      
                   balance = balance-money
                   print(f"You withdraw the ${balance} ")
                   print(f"Your Money is Now {balance}$")
                   
                   print("Thanks For Visisting our Bank")
                   print("If you want to Exit press the option 4")
                  else:
                      print("You Have Sufficent Balance")
                      print("Thanks For Visisting our Bank")
                      print("If you want to Exit press the option 4")
                                  # print("Do you want to chose any option again: ")
            
                
             elif options ==3:
              print(f"This is your Current Balance: {balance}$")
              print("\nThanks For Visisting our Bank")
              print("If you want to Exit press the option 4")
              #print("Do you want to chose any option again: ")
            #  opt=print("Write the option YES: ")
             #elif restart == "yes":
              #restart
              
                
         
             elif options == 4:
              print("You Exit from the ATM Machine")
              print("\nThanks For Visisting our Bank")
              print("Do you want to chose any option again: ")
              break
else:
    
    print("You Have Enter Invalid Synatx")
    print("Thank You.\nHave a Nice Day.")
    #int(input("Enter Correct Pin: "))
    #def Bank()    
