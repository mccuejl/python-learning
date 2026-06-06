# Day 3 of 100 Days of Code Project File - Choose Your Own Adventure Game

print('''           .-._   _ _ _ _ _ _ _ _
.-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
                             (((-'\ .' /
                           _____..'  .'
                          '-._____.-'
''')

print("Welcome to Choose Your Own Adventure!\n Your mission, should you choose to accept it, is to cross the lake without geeting eaten by the crocodile.")

mission_accepted = input("Do you accept the mission? Enter Y for Yes and N for No. ").upper()
if mission_accepted == "Y":
    print("Let's play!")
  
    left_or_right = (input("Would you like to go left or right? Enter L for left or R for Right. ")).upper()
    
    if left_or_right == "L":
        print("Good choice! You avoided the alligator pit.")
    
        swim_or_boat = input("Do you want to swim across the lake or wait for a boat? Enter S for swim or B to wait for a boat. ").upper()
        if swim_or_boat == "B":
            print("The boat captain will get you safely across the river! ")

            which_gate = input("Do you want to go through the (B)lue, (R)ed, or (Y)ellow gate? ").upper()

            if which_gate == "Y":
                print("Congratulations! You successfully completed the mission!")
            
            elif which_gate == "B" or which_gate == "R":
                print("Game over! You walked right through the gate and fell into an alligator pit! 🐊")

        else:
            print("Game over! That wasn't a log you saw in the river. It was an alligator and it ate you!")

    else:
        print("Game over! You stepped in the alligator pit. Please play again.")
    

elif mission_accepted == "N":
    print("You're no fun!") 

else:
    print("That's not a valid selection. Please press play to try again.")
