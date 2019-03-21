import random
name = input("Enter your name:")
rounds = int(input("Enter number of rounds: "))
r_p_won = r_c_won = 0
for i in range(rounds):
	print("Round ",i+1)
	choice=input("Enter choice - r for Rock, s for Scissor, p for Paper: ")
	choice=choice.lower()
	all={'r':'rock','p':'paper','s':'scissor'}
	print(name," choosed ",all[str(choice)])
	comp_choice=random.choice(list(all))
	print("Computer choosed ", all[str(comp_choice)])
	comb=choice+comp_choice
	if (comb == 'rs' or comb=='pr' or comb=='sp'):
		print(name," wins.")
		r_p_won += 1
	elif(comb=='sr' or comb=='rp' or comb=='ps'):
		print("Computer wins.")
		r_c_won += 1
	else:
		print("Draw !")
if( r_c_won > r_p_won ):
	print("Computer won by ", r_c_won-r_p_won, "rounds")
elif(r_c_won < r_p_won):
	print(name," won by ", r_p_won-r_c_won, "rounds")
else:
	print("Draw !")