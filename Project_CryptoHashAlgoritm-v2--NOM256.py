print(" ::: NOM256 ::: ")
print(" A Cryptographic Hash Algorithm")
print(" - version: 2")
print(" - Source: https://github.com/torresjrjr/CryptoHashAlgorithm")
print(" ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ")

import time
from datetime import timedelta
from matplotlib import pyplot as plt
import numpy as np

### Functions for presentation and outputs ###

RATE = 4.2535969274764765e-05 # seconds per character.

def createHashcodeString(digest):
    """
    Returns a hexadecimal hash string of alphanumeric characters, 
    given a digest list of integers ranging from 0 to 15.
    """
    map_num2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hashcodelist = [None] * len(digest)
    
    for i1 in range(0, len(digest)):
        digest_i = digest[i1]                       # Extracts the number from the digest.
        hashcodelist[i1] = map_num2hex[digest_i]    # Turns the number to a hex value and assigns it to the hashcodelist.
    
    hashcodestring = ""
    
    for i1 in range(0, len(hashcodelist)):
        hashcodestring = hashcodestring + hashcodelist[i1] # Appends the characters to form a string.
    
    return hashcodestring

def hashcodeGrid4x4x4(hashcodestring):
    """
    Prints a 4 x 4 x 4 grid of alphanumeric hexadecimal characters, 
    representing a hash string.
    """
    hashcodegrid = [" "," "," "," "]
    
    i1 = 0
    while i1 < 64: # every character.
        linenum = int(i1/16) # every 16th character.
        if i1 % 4 == 3: # every 4th character.
            hashcodegrid[linenum] = hashcodegrid[linenum] + hashcodestring[i1] + " "
        else: # every other character.
            hashcodegrid[linenum] = hashcodegrid[linenum] + hashcodestring[i1]
        i1=i1+1
    
    #print("- - - - - - - - - - -")
    print("+---- ---- ---- ----+")
    for line in hashcodegrid:
        print(line)
    print("+---- ---- ---- ----+")
    #print("- - - - - - - - - - -")
    
def approximateTime(meal):
    """
    Returns an estimated time to compute a hash of a given meal string.
    The relationship is known to be linear.
    """
    RATE = 4.2535969274764765e-05 # seconds per character.
    time = len(meal)**1 * RATE
    return time
    
### Functions for preparing the data ###

def prepareMealFromFile(filepath="meal.txt"):
    """
    Prepares a meal as a string, from any file.
    """
    print(f'Reading file: {filepath}')
    with open(filepath, 'rb') as f:
        rawmeal = str(f.read())
        
    binstring = ""
    for char in rawmeal:
        binstring += bin(ord(char))
    
    binstring = binstring.replace("b","10")
    
    stringSuffix = "10"*128 # filler string of length 256.
    # Adds enough filler string to be multiple of 256:
    binstring += stringSuffix[:((len(stringSuffix)-len(binstring))%len(stringSuffix))]
    
    return binstring

def prepareMealFromString(string=""):
    """
    Prepares a meal as a string, from a string.
    """
    binstring = ""
    for char in string:
        binstring += bin(ord(char))
        
    binstring = binstring.replace("b","10")
    
    stringSuffix = "10"*128 # filler string of length 256.
    # Adds enough filler string to be multiple of 256:
    binstring += stringSuffix[:((len(stringSuffix)-len(binstring))%len(stringSuffix))]
    
    return binstring

def splitUpMeal(bigmeal, max_multiple=16):
    """
    Divides a meal into more manageble and less intensive meal sizes
    """
    batch_size = 256 * max_multiple # 4096
        
    stringSuffix = "10" * int(batch_size/2) # filler string of length 256.
    # Adds enough filler string to be multiple of 256:
    bigmeal += stringSuffix[:((len(stringSuffix)-len(bigmeal))%len(stringSuffix))]
        
    batch_list = [bigmeal[i:i+batch_size] for i in range(0, len(bigmeal), batch_size)]
    return batch_list
    

### Preparation of the data ###

print("Preparing data to hash...")
TIME_1 = time.time()
T1 = time.time()

meal = prepareMealFromFile()
#meal = prepareMealFromString('The quick brown fox jumps over the lazy dog.')

MEAL_LENGTH = len(meal)

batch_list = splitUpMeal(meal)

T2 = time.time()
TIMETAKEN = T2-T1
print("time taken:", TIMETAKEN)

print("--- --- --- \n meal preview:\n" + str(meal[:254]) + "\n...\n")
print("length of meal:", len(meal))
#print("quotient of 256:",len(meal)/256)
#print("remainder of 256:",len(meal)%256)

#print("##################################")
#print("--- --- --- \n batch_list preview:\n", batch_list[0], "\n...\n")
print("Total batches:",len(batch_list))
#print("##################################")

### Functions for creating a hash ###

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def createIts(meal):
    its = [prime%(len(meal)) for prime in primes]
    return its

its = [prime%(len(meal)) for prime in primes]

def nom(meal, i1):
    # Iterators
    #numOfIts = len(meal)
    #its = [i1 for i1 in range(0,numOfIts)]
    #its = [0,2,1,6, len(meal)]
    #its = createIts(meal)
    numOfIts = len(its)
    
    newnom = 0
    for i2 in range(0,numOfIts):
        newnom += int(meal[its[i2]+i1]) + primes[i2]
        #print(primes[i2])
        #print("newnom =", newnom)
    
    newnom = str(newnom % 10)
    return newnom
    
def nibble(meal):
    broth = ""
    for i1 in range(-len(meal), 0):
        broth += nom(meal, i1)
    return broth

def munch(broth, numOfMunches):
    for i1 in range(numOfMunches):
        broth = nibble(broth)
    return broth

def chew(broth):
    broth = munch(broth, 4)
    
    #thing = broth
    #print(type(thing), len(thing), len(thing)%256)
    
    broth_list_int = []
    for char in broth:
        broth_list_int.append(int(char))
        
    #thing = broth_list_int
    #print(type(thing), len(thing), len(thing)%256)
    
        
    digest_list_four = []
    tempInt = 0
    i1 = 0
    for inte in broth_list_int:
        if i1 % 4 != 0:
            tempInt += inte
            tempInt = tempInt % 16
        else:
            digest_list_four.append(tempInt)
            tempInt = 0
        i1 += 1
        
    thing = digest_list_four
    #print(type(thing), len(thing), len(thing)%64)
    
    return digest_list_four
    
def gulp(meal):
    #print("Proccessing...")
    broth = meal
    chunks = [broth[i:i+256] for i in range(0, len(broth), 256)]
    #print("Number of chunks:", len(chunks))
    #print(" - Chunkified...")
    digest = [0]*64
    i1 = 1
    global Ti
    Ti = 0
    for chunk in chunks:
        t1 = time.time()
        
        if i1 == 1:
            chewed = chew(chunk)
            digest = chewed
        else:
            chewed = chew(chunk)
            digest = [(int(x) + int(y))%16 for x, y in zip(digest, chewed)]
        
        t2 = time.time()
        #print("time taken:", t2-t1)
        Ti += t2-t1
        #print("time TOTAL:", Ti)
        #print(" - Chewed!")
        
        i1 += 1
    #print("Hash finished.")
    return digest

### Creating a hash ###

#print(meal)
print("##########################################################################")
print("Hashing...")
T1 = time.time()

#broth = gulp(meal)

i2 = 0
broth_batch_list = []
for meal in batch_list:
    broth_batch_list += [gulp(meal)]
    #print("broth_batch_list:\n", broth_batch_list)
    
    i2 += 1
    
    Total_batches_left = len(batch_list) - i2
    batch_size = len(batch_list[0])
    seconds_left = Total_batches_left * RATE * batch_size
    
    print("Total batches left: "+str(Total_batches_left)+
          "    Estimated Time: "+str(timedelta(seconds=seconds_left)))
    
print("broth_batch_list length:", len(broth_batch_list))

broth = [((sum(x) + max(x)) % 16) for x in zip(*broth_batch_list)]

T2 = time.time()
TIME_2 = time.time()
print("##########################################################################")
#print("DIGEST:\n", broth)
TIMETAKEN = T2 - T1
TIMETAKEN = TIME_2 - TIME_1
print("time taken:", TIMETAKEN)

### Finalising a hash ###

broth_list_int = []
for char in broth:
    broth_list_int.append(int(char))

tempInt = 0
for inte in broth_list_int:
    tempInt = (tempInt + inte) % 16
broth_list_int[0] = tempInt

#print("broth_list_int: \n", broth_list_int)
thing = broth_list_int
#print(type(thing), len(thing), len(thing)%64)

### Calculating stats for presenting a hash ###

broth_list_int_sorted = sorted(broth_list_int)
#print(broth_list_int_sorted)
thing = broth_list_int_sorted
#print(type(thing), len(thing), len(thing)%64)

average_value = sum(broth_list_int)/len(broth_list_int)
#average_value = 7.5
#print("average_value =", average_value)

def sigmoid01(x, xmid, L, k):
    euler = 2.71828182845904523536028747135266249775724709369995
    sigma = L/(1 + euler**(-k*(x-xmid)))
    return sigma

# temp.
average_value_adj = (average_value+0.5)
#print("average_value_adj =", average_value_adj)

sigmoid_value = sigmoid01(average_value_adj, 8, 16, 4)
#print("sigmoid_value =", sigmoid_value)

### Presenting a hash ###

HashcodeString = createHashcodeString(broth_list_int)

x = broth_list_int

fig = plt.figure(num=None, figsize=(10, 5), dpi=128, facecolor='w', edgecolor='b')
ax = fig.add_subplot(1, 1, 1) # nrows, ncols, index

hint_max = 0.3
hint = sigmoid01(average_value_adj, 8, hint_max*2, 4) - hint_max
#print(hint)
#faceColor = (max(0, hint), 0, max(0, -hint))
faceColor = (max(0, hint), max(0, (hint_max-abs(hint))   ), max(0, -hint))
#faceColor = (max(0, hint), max(0, (hint_max-abs(hint))**2), max(0, -hint))
#print(faceColor)
#ax.set_facecolor('#FFFFFF')
#ax.set_facecolor('#0c1111')
ax.set_facecolor(faceColor)

plt.xticks(np.arange(0, 256+1, 4.0))
plt.yticks(np.arange(0, 15+1, 2.0))

plt.grid(b=True, which='major', axis='both', linestyle=':', color='#555555')
plt.grid(b=True, which='minor', axis='both', linestyle='-', color='g')

plt.plot(broth_list_int, 'wo:')
#plt.plot(broth_list_int, 'ko:')
plt.plot(broth_list_int_sorted, 'r.-')

plt.title(HashcodeString, {'fontsize': 16}, fontfamily='consolas')

print("'outhash.png' will be saved once figure is closed")
plt.show()

print("Saving hash output graph 'hash.png'...")
fig.savefig('outhash.png', dpi=fig.dpi);
print("'hash.png' saved")

### Printing the hash ###

print("\nOutput hash:")
HashcodeString = createHashcodeString(broth_list_int)
print(HashcodeString)
print("\n4x4x4 hash grid.:")
hashcodeGrid4x4x4(HashcodeString)

### Verifying hash output validity ###

def verifyHashcode(digest):
    list_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    list_num = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 , 11 , 12 , 13 , 14 , 15 ]
    
    total = 0
    for i2 in range(len(digest)):
        digest_i = digest[i2]
        #print("digest_i =", digest_i)
        
        for i1 in range(16):
            if digest_i == list_str[i1] and i2 != 0:
                total += list_num[i1]
                #print("total =", total)
                #print("list_num[i1] =", list_num[i1])
                continue
        
        #print("--- --- ---")
    
    #print("total =", total)
    
    checknum = total % 16
    #print("checknum =", checknum)
    
    checkstr = list_str[checknum]
    #print("checkstr =", checkstr)
    
    checkorg = digest[0]
    #print("checkorg =", checkorg)
    
    if checkorg == checkstr:
        isValid = True
    else:
        isValid = False
    
    return isValid

print("\nVerifying hash validity...")
print("Validity is", str(verifyHashcode(HashcodeString)))
print("\n")

### Writing the hash output ###

with open('outhash.txt', 'w') as f: 
    f.write(HashcodeString)
    print('\'outhash.txt\' saved and ready.')

with open('outhash-history.txt', 'a') as f: 
    f.write(HashcodeString + "\n")
    print('\'outhash-history.txt\' saved and ready.')
    
with open('outhash-testing.txt', 'a') as f: 
    f.write(HashcodeString + " {'meal_length':"+str(MEAL_LENGTH)+", 'time_taken':"+str(TIMETAKEN)+"}\n")
    print('\'outhash-testing.txt\' saved and ready.')


### END ###
DONE_TIMER = 5
print(f'Done. Quitting in {DONE_TIMER} seconds')
time.sleep(DONE_TIMER)
print("END")
