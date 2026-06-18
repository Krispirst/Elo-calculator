#elo calculator on python3 by krispirst

import sys

print('Welcome to the Elo calculator in Python 3')

try: 
    p1_elo = int(input("Enter the first opponent's Elo rating: "))

    p2_elo = int(input("Enter the second opponent's Elo rating: "))

except:
    print("Error. Invalid input ")
    sys.exit()


#The first step is to use the formula to calculate each player's percentage chance of winning. 

expected_for_p1 = 1/(1+10**((p2_elo - p1_elo)/400))

expected_for_p2 = 1/(1+10**((p1_elo - p2_elo)/400))


print("""
Who won?

If the first player won, enter 1
If the second player won, enter 2
If the game ended in a draw, enter 3 """)
result = input("Enter the match result: ")

if result == "1":
    result_p1 = 1
    result_p2 = 0
    
elif result == "2":
    result_p1 = 0
    result_p2 = 1
    
elif result == "3":
    result_p1 = 0.5
    result_p2 = 0.5
    
else:
    print("Error. Invalid input ")
    sys.exit()



#And now, using the following formula, we need to calculate each player’s Elo rating based on the result

#The rating change depends on the K-factor which is calculated based on whether the player is new, how many games they’ve played, and so on
#For this calculator, I’ll use a k-factor of 20. If you’re interested in learning more about this topic, I recommend reading this article:
#https://www.researchgate.net/publication/397318383_Optimizing_K-factor_in_Elo_Rating_Systems

k_factor = 20

new_elo_p1 = p1_elo + k_factor * (result_p1 - expected_for_p1)

new_elo_p2 = p2_elo + k_factor * (result_p2 - expected_for_p2)

print("""
-------------------------------""")
print(f'New rating for the first player:{new_elo_p1}')
print(f'New rating for the second player: {new_elo_p2}')
print("-------------------------------")






