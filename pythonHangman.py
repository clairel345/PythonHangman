import random

print("")
print("Category: Fruits!")

wordList = [
    "apple",
    "orange",
    "grape",
    "kiwi",
    "mango",
    "blueberry",
    "watermelon",
    "peach",
    "plum",
    "cherry",
    "pomegranate"
]


run = True

word = wordList[random.randint(0, len(wordList) - 1)]

wordFormat = ""; #the _ _ _ _ _ part

def guessLines (theWord):
	global wordFormat

	#print("The word: " + theWord);
	for letter in theWord:
		wordFormat += "_ "


guessLines(word)

#add in spaces between the words
spacedWord = ' '.join(word) + " "

#print("\n" + spacedWord + "\n")


theNope = ""
wordsUsed = []
amountWrong = 0


human = {
	1: "O", #head
	2: "|", #spine
	3: "/", #L arm
	4: "\\", #R arm
	5: "/", #L leg
	6: "\\", #R leg

}

headSpace = " "
bodySpace = " "
lArm = " "
rArm = " "
lLegSpace = " "
rLegSpace = " "

def updateHangman(w):
	global headSpace, bodySpace, lArm, rArm, lLegSpace, rLegSpace

	if w == 1:
		headSpace = "O"
	elif w == 2:
		bodySpace = "|"
	elif w == 3:
		lArm = "/"
	elif w == 4:
		rArm = "\\"
	elif w == 5:
		lLegSpace = "/"
	elif w == 6:
		rLegSpace = "\\"



while(run):

	print(theNope)
	print("        _________")
	print("        |       |")
	print("        |       |                             " + "Letters Used: ")
	print("       " + headSpace + "        |       Guess the word:       "  + ", ".join(wordsUsed))
	print("      " + lArm + bodySpace + rArm + "       |")
	print("      " + lLegSpace + " " + rLegSpace + "       |       " + wordFormat + "               " )
	print("                |")
	print("                |")
	print("     ________________")

	theNope = ""

	ter = input("Guess ONE letter: ")

	if ter == "":
		theNope = "Try Again. ONE letter"

	elif ter in spacedWord:
		ind = spacedWord.index(ter)

		#case of same letters in diff spots
		if(wordFormat[ind] != "_"):
			test = spacedWord[ind + 2:]
			if ter in test:
				ind = test.index(ter) + len(spacedWord[:ind]) + 2

		wordFormat = wordFormat[:ind] + ter + wordFormat[ind + 1:]
	
	else:
		if len(ter) == 1:
			wordsUsed.append(ter)
		amountWrong += 1
		updateHangman(amountWrong)

		theNope = "Nope, try again."


	if wordFormat == spacedWord:
		print("\n        _________            YOU")
		print("        |       |           WIN!!!!")
		print("        |       |                             " + "Letters Used: ")
		print("       " + headSpace + "        |       Guess the word:       "  + ", ".join(wordsUsed))
		print("      " + lArm + bodySpace + rArm + "       |")
		print("      " + lLegSpace + " " + rLegSpace + "       |       " + wordFormat + "               " )
		print("                |")
		print("                |")
		print("     ________________")
		print("You win! The word was: " + word)
		print("")
		run = False


	if amountWrong > 5:
		print("You Lose! The word was: " + word)
		print("        _________")
		print("        |       |")
		print("        |       |                             " + "Letters Used: ")
		print("       " + headSpace + "        |       Guess the word:       "  + ", ".join(wordsUsed))
		print("      " + lArm + bodySpace + rArm + "       |")
		print("      " + lLegSpace + " " + rLegSpace + "       |       " + wordFormat + "               " )
		print("                |")
		print("                |")
		print("     ________________")
		run = False

	if ter == 'done':
		#print(wordFormat + " - " + spacedWord)
		#print(wordFormat == spacedWord)

		print("Try again next time!")
		run = False


#python3 pythonHangman.py







