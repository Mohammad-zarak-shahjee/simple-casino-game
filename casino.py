import random
cash=100
def play(bet):
	global cash
	cards=['K','Q','J']

	print('.....*****SHUFFLING*****.....')
	random.shuffle(cards)
	y=0
	while(y==0):
		playerguess=int(input('Guess the position of QUEEN >>\n\n  1\n\n  2\n\n  3\n\n'))
		if(playerguess==1 or playerguess==2 or playerguess==3):


			if(cards[playerguess-1]=='Q'):
				cash += 3*bet
				print('WOHOOOOO!!!\nYOU WIN!!!\nSEQUENCE IS {} {} {}\nTOTAL CASH={}'.format(cards[0],cards[1],cards[2],cash))
			else:
				cash -= bet
				print('BOOOOOO!!!\nYOU LOSE!!!\nSEQUENCE IS >> {} {} {}\nTOTAL CASH={}'.format(cards[0],cards[1],cards[2],cash))
			y=1
		else:
			print("card {} doesn't exist".format(playerguess))


print("$$$*****WELCOME TO CASINO ROYALE*****$$$")
print("Total cash available is $100")


while(cash>0):
	x = 'y'
	bet=int(input("What's yor bet:"))
	if(bet==0):
		print("Sorry! you can't bet nothing.")
		continue
	elif(bet>cash):
		print("Sorry you don't have that much cash.")
		continue
	elif(bet==cash):
		x=input("Are you sure you want to bet all your money?\npress y/Y to continue else press any key to change your bet:")

	if(x=='y' or x=='Y'):
		play(bet)
	else:
		continue

print('Sorry! you lost all your money.')



