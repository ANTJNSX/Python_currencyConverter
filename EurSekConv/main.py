from os import system
import time
from forex_python.converter import CurrencyRates
cr = CurrencyRates()

def convertToSEK(val):
	new_val = cr.convert('EUR', 'SEK', val)
	return(new_val)


def printData():
	print("[Rate] - [EUR] - [SEK]", end="\n")
	
	for i in range(len(euros)):
		print("[" + str(cr.get_rate('EUR', 'SEK')) + "] - "  + "[" + str(euros[i]) + "] - "  + "[" + str(kronor[i]) + "]")

		if i == len(euros)-1:
			# time.sleep(10)
			
			# loop over 10 times
			crTimer = 10
			for i in range(crTimer):
				# rewrite current output with current countdown
				print(str(crTimer-i) + " Seconds left before next update ", end="\r")
				time.sleep(1)
				# end loop

			system('clear')

euros = []
kronor = []

intervals = int(input("increase with intervals of?: "))
amount = int(input("enter amount of times: "))

money = 0
for i in range(amount):
	money += intervals
	euros.append(money)

for i in euros:
	crSEK = convertToSEK(i)	
	kronor.append(crSEK)

system('clear')
while 1:
	printData()