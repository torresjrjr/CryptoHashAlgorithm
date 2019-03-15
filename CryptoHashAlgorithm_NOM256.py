#1#
###---------- Declaring meal and digest ----------###
meal = None
digest = None

#2#
def convert_msg2num(messageToSend, basicCipherKey = None):
	'''
	Turns a string of text into a list of numbers, 
	then applies a basic cipher with a cipher key.
	INPUTS:
		messageToSend        str; message as text.
		basicCipherKey       int; basic cipher key.
	OUTPUTS:
		messageAsNumList     list; of integers.
	'''
	if basicCipherKey == None: basicCipherKey = 0
	
	messageAsNumList = []
	for character in messageToSend:
		append_num = [int(ord(character)) + int(basicCipherKey)]
		messageAsNumList = messageAsNumList + append_num
	return messageAsNumList

#3#
def createHashcodeList(digest):
	'''
	Creates a list of single character string elements,
	written as hexadecimal digits, from a list of
	integers from 0 to 15.
	INPUTS:
		digest     list; of ints from 0 to 15
	OUTPUTS:
		hashcodelist     list; of strings from '0' to 'F' (Hexadecimal).
	'''
	map_num2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	hashcodelist = [None] * len(digest)
	
	for i1 in range(0, len(digest)):
		digest_i = digest[i1]
		hashcodelist[i1] = map_num2hex[digest_i]
	return hashcodelist

#4#
def createHashcodeString(digest):
	'''
	Creates a string of hexadecimal digits,
	from a list of integers from 0 to 15.
	INPUTS:
		digest     list; of ints from 0 to 15
	OUTPUTS:
		hashcodestring     str; of characters from '0' to 'F' (Hexadecimal).
	'''
	map_num2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	hashcodelist = [None] * len(digest)
	
	for i1 in range(0, len(digest)):
		digest_i = digest[i1]                       # Extracts the number from the digest.
		hashcodelist[i1] = map_num2hex[digest_i]    # Turns the number to a hex value and assigns it to the hashcodelist.
	
	hashcodestring = ""
	
	for i1 in range(0, len(hashcodelist)):
		hashcodestring = hashcodestring + hashcodelist[i1] # Appends the characters to form a string.
	
	return hashcodestring

#6#
def hashcodeGrid4x4x4(hashcodestring=None, lineNum=4, columnNum=4, blockNum=4, gridBorders=None):
	'''
	Prints an aesthetic 4 by 4 grid of hexadecimal digits, 
	in blocks of 4, between 2 box lines above and below
	given a hashcode string.
	INPUTS:
		hashcodestring     str; of characters from '0' to 'F' (Hexadecimal), ideally 64 characters.
		lineNum            int; number of lines in the grid. Default = 4 .
		columnNum          int; number of columbs in the grid. Default = 4 . Note: doesn't do anything rn.
		blockNum           int; number of digits in a block. Default = 4 .
	ACTIONS:
		prints a hashcode grid:
		
			+---- ---- ---- ----+     example.
			 0123 4567 89AB CDEF 
			 0123 4567 89AB CDEF 
			 0123 4567 89AB CDEF 
			 0123 4567 89AB CDEF 
			+---- ---- ---- ----+
		
	OUTPUTS:
		None
	'''
	if hashcodestring == None: hashcodestring = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
	if len(hashcodestring) != 64: 
		print("ERROR: function hashcodeGrid4x4x4(hashcodestring) - input hashcodestring is not 64 characters.\n",
			 "Hashcode grid will not be printed!")
		return
	
	hashcodegrid = [" "] * lineNum # preparing 4 lines/strings, with an initial SPACE as padding.
	
	#lineNum = 4
	#blocksNum = 4
	#blockNum = 4
	
	for i1 in range(0, 64): # every character.
		lineIndex = int( (i1)/( 64/lineNum ) ) # every character at the end of a line.
		if i1 % blockNum == blockNum - 1 : # every character at the end of a block.
			hashcodegrid[lineIndex] = hashcodegrid[lineIndex] + hashcodestring[i1] + " "
		else: # every other character.
			hashcodegrid[lineIndex] = hashcodegrid[lineIndex] + hashcodestring[i1]
	
	if gridBorders == None: gridBorders = 1
	
	
	if gridBorders == 3: print("- - - - - - - - - - -")
	if gridBorders == 2: print("+---- ---- ---- ----+")
	if gridBorders == 1: print("+---- hash-code ----+")
	
	for i2 in range(0, lineNum):
		print(hashcodegrid[i2])
	
	if gridBorders == 1: print("+-------------------+")
	if gridBorders == 2: print("+---- ---- ---- ----+")
	if gridBorders == 3: print("- - - - - - - - - - -")
	
	return

#7#
def mealMerger(mealIn1, mealIn2):
	'''
	Returns a list merged from two other lists.
	Corresponding elements are summed, then
	modulo-ed 16.
	INPUTS:
		mealIn1     list; of ints.
		mealIn2     list; of ints.
	OUTPUTS:
		mealOut     list; of ints.
	'''
	if len(mealIn1) == len(mealIn2):
		mealOut = list(mealIn1)    
	if len(mealIn1) != len(mealIn2): 
		print("ERROR: function mealMerger(mealIn1, mealIn2) - inputs are not equal in length.\n",
			  "Smallest merge returned; algorithm cannot not guarantee omni-sensitivity!")
	if len(mealIn1) <  len(mealIn2):
		mealOut = list(mealIn1)
		print("  DEBUG: len(mealIn1) < len(mealIn2)")
	if len(mealIn1) >  len(mealIn2):
		mealOut = list(mealIn2)
		print("  DEBUG: len(mealIn1) > len(mealIn2)")
		
	i1 = 0
	while i1 < len(mealOut):
		a = mealIn1[i1]
		b = mealIn2[i1]
		mealOutDividend = a + b # Simple addition. Guarantees omni-sensitivity.
		mealOut[i1] = mealOutDividend % 61 # 61, a prime. Also not a multiple of 16, so 'A' and 'a' won't give the same meal out.
		i1+=1
	return mealOut

#8#
def hashFunctionNom(mealIn, nomIndexes):
	'''
	"Nibbles" a meal once; takes three specific elements of 
	a list and calculates a new element to replace one.
	Returns the meal with the modified element.
	INPUTS:
		mealIn        list; of ints.
	OUTPUTS:
		list(nom)     list; of ints.
	'''
	nom = list(mealIn)
	
	numberOfNomIndexes = len(nomIndexes)
	i1, i2, i3 = nomIndexes
	a = nom[i1]
	b = nom[i2]
	c = nom[i3]
	
	# list; The first 64 lucas numbers with L(0) = 2 and L(1) = 1 :
	lunum = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 
		 64079, 103682, 167761, 271443, 439204, 710647, 1149851, 1860498, 3010349, 4870847, 7881196, 12752043, 20633239, 
		 33385282, 54018521, 87403803, 141422324, 228826127, 370248451, 599074578, 969323029, 1568397607, 2537720636, 
		 4106118243, 6643838879, 10749957122, 17393796001, 28143753123, 45537549124, 73681302247, 119218851371, 
		 192900153618, 312119004989, 505019158607, 817138163596, 1322157322203, 2139295485799, 3461452808002, 
		 5600748293801, 9062201101803, 14662949395604]
	
	## Hash function option 1:
	#a_new = ((a+b*c)*(a-b)) % 256
	
	## Hash function option 2:
	terms_onlyabc = (a + b + c) + (b**a + c**a) + (a**a * b**b * c**c)    # terms with only the meal elements.

	terms_dual = a*lunum[i1] + (a**a)*lunum[(i1+a)%64] + (b**a)*lunum[(i1+b)%64] + (c**a)*lunum[(i1+c)%64]

	terms_lucasterms = lunum[(lunum[(i1*i1) % 64] + (i2*i3) % 64) % 64]   # terms with the lunum list.
	
	dividend = terms_onlyabc + terms_dual + terms_lucasterms
	modulus = 16   # Does NOT have to be 16, 
	# although values greater than 17 could cause big work in future interations
	# for example, for terms like a**b (17**17 = 3.93e+22 )
	
	a_new = dividend % modulus
	
	nom[i1] = a_new
	return list(nom)

#9#
def hashFunctionMunch(mealIn):
	'''
	"Nibbles" a through a full meal once; Repeats hashFunctionNom() over the entire meal, 
	from the beginning element, one cycle over, to a near last element.
	INPUTS:
		mealIn     list; of ints.
	OUTPUTS:
		digest     list; of ints.
	'''
	digest = list(mealIn)    # Defining a digest of equal length to fill in.
	numberOfNomIndexes = 3   #!# DEPENDANT on the function hashFunctionNom() #!#
	
	for i in range(-len(mealIn), len(mealIn) -numberOfNomIndexes): # Note: num of runs is dependant on numberOfNomIndexes.
		nomIndexes = (i, i+1, i+2)
		digest[i] = hashFunctionNom(mealIn, nomIndexes)[i] # returns list(nom);
	# digest is the sum of all the list(nom)'s.
	
	return digest

#10#
def hashFunctionChew(mealIn, numOfChews = None):
	if numOfChews == None: numOfChews = 64
	i1 = 1
	#print("\n hashFunctionChew executed, with numOfRuns =",numOfChews,"\n")
	while i1 <= numOfChews:
		digest = hashFunctionMunch(mealIn)
		mealIn = list(digest)
		i1+=1
	
	i2 = 0
	while i2 < len(digest):
		digest[i2] = digest[i2] % 16
		i2+=1
	
	return digest

#11#
def mealPadder(mealIn):
	soup = list(mealIn)
	lengthSoup = len(soup)
	numOfChunks = int( (lengthSoup-1)/64 ) + 2
	
	lengthPadded = numOfChunks * 64
	
	paddedFillerNumber = 3
	mealPadded = [paddedFillerNumber]*lengthPadded
	
	for i1 in range(0, lengthSoup):
		mealPadded[i1] = soup[i1]
	
	return mealPadded, lengthSoup, numOfChunks

#12#
def mealSalter(mealPaddedIn, lengthSoup):
	broth = list(mealPaddedIn)
	
	saltyList = [5]*64
	saltyList[-64 + 0] = lengthSoup % 2
	saltyList[-64 + 1] = lengthSoup % 3
	saltyList[-62 + 2] = lengthSoup % 5
	saltyList[-62 + 4] = lengthSoup % 7
	saltyList[-62 + 5] = lengthSoup % 11
	
	for i1 in range(-len(saltyList) + 5, -0):
		#saltyList[i1] = 3 + ( (i1) + saltyList[i1-1]**4 + saltyList[i1-2]**3 + saltyList[i1-3]**2 ) % (61 + (i1)**2 )# 61, a prime number.
		saltyList[i1] = 1 + (( 3**(saltyList[i1-1]) + 5**(saltyList[i1-2]) + 7**(saltyList[i1-3]) + 11**(saltyList[i1-4]) + 13**(saltyList[i1-5]) ) % (17)) # 17, a prime number.
		
	for i2 in range(-len(saltyList), -0):
		broth[i2] = int(saltyList[i2])
	return broth

#13#
def HashFunction_NOM256(mealIn, numOfChews=None):
	thePhatMeal = list(mealIn)
	thePhatMeal, lengthSoup, numOfChunks = mealPadder(thePhatMeal)
	thePhatMeal = mealSalter(thePhatMeal, lengthSoup)
	
	print("thePhatMeal (first 128):\n",thePhatMeal[:128])
	print("thePhatMeal Length: \n", len(thePhatMeal))
	print("lengthSoup: \n", lengthSoup)
	print("numOfChunks: \n", numOfChunks)
	
	for i1 in range(0, numOfChunks):
		lilDish = [] # restarts lilDish for the next chunk.
		#print("- CHUNK SEP -")
		
		# Extracts a chunk onto lilDish.
		for i2 in range( i1*64, i1*64 + 64 ):
			#print("_",i2)
			#print(thePhatMeal[i2])
			lilDish.append(thePhatMeal[i2]) # lilDish is established when loop finishes.
			#print(lilDish[i2])
		
		if i1 == 0: # If its the first chunk:
			#lilDishMerged = mealMerger(lilDish, lilDish) # Merge itself, for now.
			lilDishMerged = list(lilDish)
			digestOfChunk = hashFunctionChew(lilDishMerged, numOfChews)
		if i1 > 0:  # If its any subsequent chunk:
			#print("len(lilDish):\n",len(lilDish))
			#print("len(previouslilDish):\n",len(previouslilDish))
			lilDishMerged = mealMerger(lilDish, previouslilDish)
			digestOfChunk = hashFunctionChew(lilDishMerged, numOfChews)
		previouslilDish = list(digestOfChunk)
		
		#digest.append(digestOfChunk1)
	
	digest = list(digestOfChunk)
	
	return digest

#14#
### Main Program Loop ###

print("::::: Welcome to the CryptoHashAlgorithm program :::::")
print("  - This program creates a cryptographic hash output (digest) for any string of text input (meal).")
print("  - This program uses a algorithm called NOM-256.")
while True:
	userinput_menu = input("\n <> Enter a command:\n < [i] input a meal , [help] help , [q] quit >\n>>> ")
	
	if userinput_menu == "q":
		break

	if userinput_menu == "help":
		print("- - - - - Help - - - - -")
		print("  - \"My text input has quotation marks and won't work.\"")
		print(' Use a text editor (Notepad is very useful), and use the "Replace" feature to replace all (\") with (\\").')
		
		print("\n  - \"My text input has paragraph and won't work.\"")
		print(" You can convert your text to html (a code for writing text on webpages and emails...), or copy a html version\n",
			   "from a webpage\'s source. In chrome, you can right click on a webpage and do this, and view and copy the \n",
			   "relevant piece of text. Your text has multiple strings since it has these paragraph separators, so when \n",
			   "encoded in html, it'll instead appear as (<p>My first paragaph</p><p>My second paragaph</p>), and count as \n",
			   "one string. Ideally, you want to copy and paste from the fist (<p>) to the last (</p>)")

	elif userinput_menu == "i":
		userinput_meal = input(" <> Input a meal (a string of text):\n>>> ")
		print("Running...")
		meal = convert_msg2num(userinput_meal)

		print("meal:\n",meal[:128])
		digest = None
		#print("digest:\n",digest)

		digest = HashFunction_NOM256(meal)

		#print("meal:\n",meal[:128]) 
		print("digest:\n",digest)

		hashcodelist = createHashcodeList(digest)
		#print("hashcodelist:\n",hashcodelist,"\n")
		
		hashcodestring = createHashcodeString(digest)
		print("Hashcode string:\n",hashcodestring,"\n")
		
		print("hashcode Grid 4x4x4:")
		hashcodeGrid4x4x4(hashcodestring)
		print("\n")
	
	else:
		print("Command not recognised")

print("::::: END program :::::")