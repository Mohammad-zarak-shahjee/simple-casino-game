import random
cash=100
def play(bet):
	global cash
	cards=['K','Q','J']

	print('.....*****SHUFFLING*****.....')
	random.shuffle(cards)
	playerguess=int(input('Guess the position of QUEEN >>\n\n  1\n\n  2\n\n  3\n\n'))
	if(cards[playerguess-1]=='Q'):
		cash += 3*bet
		print('WOHOOOOO!!!\nYOU WIN!!!\nSEQUENCE IS {} {} {}\nTOTAL CASH={}'.format(cards[0],cards[1],cards[2],cash))
	else:
		cash -= bet
		print('BOOOOOO!!!\nYOU LOSE!!!\nSEQUENCE IS >> {} {} {}\nTOTAL CASH={}'.format(cards[0],cards[1],cards[2],cash))

print("*****WELCOME TO CASINO CARRO*****")
print("Total cash available is $100")

while(cash>0):
	bet=int(input('Whats yor bet:'))
	if(bet==0 or bet>cash):
		break
	play(bet)
	print('**************************************************')

