##################################################
# File: wordlistGenerator.py
# Author: Antonius Torode
# Purpose: This file generates a wordlist from a character set.
##################################################

from itertools import permutations
from itertools import product

letSet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capLetSet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numSet = ['0','1','2','3','4','5','6','7','8','9']

letSetSize = len(letSet)
capLetSetSize = len(capLetSet)
numSetSize = len(numSet)

def allNumberPermutations(minLength, maxLength):
	"""
	This function will make a text file and store all number permutations of length A to length B.
	Input Paramters: Integers (minLength, maxLength).
	"""
	file = open("allNumberPermutations{0}{1}.txt".format( str(minLength),str(maxLength) ), "w+")

	numPerm = ""
	maxLength += 1
	for num in product(numSet, repeat = maxLength):
		numPerm = ""
		
		for i in range(0,maxLength):
			numPerm += str(num[i])
			if i >= minLength and numPerm not in file:
				file.write(numPerm + '\n')

	
def allPermutations(minLength, maxLength, set, setName):
	"""
	This function will make a text file and store all permutations of a set of length minLength to length maxLength.
	
	Input Paramters: 
		integers: minLength, maxLength 
		array: set
		str: setName 
	"""
	file = open("allPermutations_{0}-{1}_{2}.txt".format( str(minLength),str(maxLength), setName ), "w+")

	perm = list("")
	string = ''
	maxLength += 1
	setSize = len(set)
	counter = 0
	
	while minLength <= maxLength:
		
		
		minlength += 1
	
	
	for l in range(minLength, maxLength):
		perm = list("")
		for x in range(0,l):
			perm.append(set[0])
		for j in range(0,l):
			for i in range(0,setSize):
				perm[l-j-1] = set[i]
				for c in set:
					perm[l-1] = c
					string = "".join(perm)
					file.write("{0}, {1}, {2}, {3}: {4}\n".format(str(l), str(j), str(i), c, string))	
	
	
allPermutations(2,3, numSet, "numbers")