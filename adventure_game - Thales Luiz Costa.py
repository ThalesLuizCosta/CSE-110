first_choice = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? Type 'MATCH' or 'FLASHLIGHT': ")

if first_choice.upper() == 'MATCH':
    second_choice = input("The forest began to burn, Then you see a way to run up a river and in the river you find two things to choose from, a 'BOAT' or a 'STONE DANGEROUS PATH', what do you want to do? : ")

    if second_choice.upper() == 'BOAT':
        print("You selected 'BOAT'. With this boat, would you like to 'ROW' or to 'REST'? : ")

        third_choice = input("You selected 'ROW'. so you come up the river, you chose to row and you see a waterfall, then you choose 'JUMP AND SWIM' to the river's edge or 'COVER' and hope the fall is not fatal, wht do you want to do? ")

        if third_choice.upper() == 'ROW':
            print("You selected to row, but when you went to start the row fell into the water, so in a moment of desperation you hold on a branch by the river that keeps your boat still and when screaming for help no one hears, only the alligators and they answer the call and devour you, you died... Game over!")
        
        fourth_choice = input("You selected 'REST', then when you wake up you are in some cannibal village, but they are not in the village, so you have two choices 'HIDE' or 'RUN', what do you want to do? ")
        
        if fourth_choice.upper() == 'HIDE':
            print("You selected 'HIDE', but his smell is too strong to disguise himself in the middle of the bush, so the cannibals find you and take you to the village, where you will be made along with your friends...you and your friends died, the game is over!")

        elif fourth_choice.upper() == 'RUN':
            print("You selected 'RUN', but when you ran, you found a group of hunters who were after you and your group, for knowing the area and knowing the dangers that are there, CONGRATULATIONS you and your friends are safe!")

        if third_choice.upper() == 'JUMP AND SWIM':
            print("You selected 'JuMP AND SWIM, but in the river there were alligators and they ate you, game over!")

        elif third_choice.upper() == 'COVER':
            print("You selected 'COVER', your boat crashed into the waterfall and you found your friends' camp again, CONGRATULATION!!!")

        elif second_choice.upper() == 'STONE DANGEROUS PATH':
            print("You selected 'STONE DANGEROUS PATH'. This path leads to a dead end. You are stuck!")

    else:
        print("Invalid choice. Please enter 'BOAT' or 'STONE DANGEROUS PATH'.")

elif first_choice.upper() == 'FLASHLIGHT':
    second_choice = input("You selected 'FLASHLIGHT'. With your flashlight in hand, you notice two paths you can take: 'LEFT' or 'RIGHT'. Which way would you like to go? : ")
    
    if second_choice.upper() == 'LEFT':
        third_choice = input("You selected 'LEFT'. With this path, would you like to enter the 'MYSTERIOUS HOUSE' or 'CONTINUE WALKING'? : ")

        if third_choice.upper() == 'MYSTERIOUS HOUSE':
            fourth_choice = input("You have entered the MYSTERIOUS HOUSE. Inside, you find hidden treasures, but next to it has a photo with an unsigned note written, 'For whoever finds this treasure, throw it away, because there is a curse on it', so you think of some alternatives, 'TAKE THE TREASURE FOR YOU', 'FIND OUT WHO WROTE THE NOTE' OR 'CALL YOUR FRIENDS TO SHARE THIS TREASURE', what would you do? ")

            if fourth_choice.upper() == 'TAKE THE TREASURE FOR YOU':
                print("You selected 'TAKE THE TREASURE FOR YOU', then you've been taken to another dimension, where there's a bank carrying your doomed soul of greed to wander eternally through the underworld...game over!")

            elif fourth_choice.upper() == 'FIND OUT WHO WROTE THE NOTE':
                print("You selected 'FIND OUT WHO WROTE THE NOTE', but you just found something written with something like blood and when looking to the side discovers an undead walking near you, and it ends up exploding and you end up dying together, game over!")

            elif fourth_choice.upper() == 'CALL YOUR FRIENDS TO SHARE THIS TREASURE':
                print("You selected 'CALL YOUR FRIENDS TO SHARE THIS TREASURE', But to your surprise, the house opens the floor and in it there is a passage that leads to a paradisiacal place, where there are millions of people living very well and in endless happiness, because this treasure is of eternal life, but it can only be found if you shared it with your friends, CONGRATULATIONS YOU WON!!!")

        elif third_choice.upper() == 'CONTINUE WALKING':
            print("You continue walking and find a beautiful clearing in the forest, do you want TO 'STAY HERE' or 'KEEP WALKING'? ")

            fourth_choice = input("You selected 'STAY HERE', but suddenly a huge tiger appears and he can't climb the tree, so think about your decision to 'CLIMB THE TREE AND FIRE THE SIGNALER' or 'FIGHT' with the tiger with a sharp spear and a shield, what do you want to do? ")
            
            if fourth_choice.upper() == 'CLIMB THE TREE AND FIRE THE SIGNALER':
                print("You do not have a signaler and now you are stuck on top of a tree with a hungry tiger waiting for you, you will die, the game is over!")

            elif fourth_choice.upper() == 'FIGHT':
                print("Despite its size, the tiger is blind and also does not have a good light, so when skewering the tiger below the jaw it falls dead and hearing the cry of the tiger a rescue team called by his friends arrives at the site, CONGRATULATIONS... YOU ARE SAFE!")
        else:
            print("Invalid choice. Please enter 'MYSTERIOUS HOUSE' or 'CONTINUE WALKING'.")

    elif second_choice.upper() == 'RIGHT':
        print("You selected 'RIGHT'. You find a path leading to a peaceful garden nearby your friend's camp.")

    else:
        print("Invalid choice. Please enter 'LEFT' or 'RIGHT'.")

else:
    print("Invalid choice. Please enter 'MATCH' or 'FLASHLIGHT'.")