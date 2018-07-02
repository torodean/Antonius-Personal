###################################
## gscraper.py
## Created By: Antonius Torode
## Date: June 2018
###################################

from __future__ import division

file_orig = open('webscrape.txt', 'r')
file_modified = open('webscrape_modified.txt','w')

#information about guild
guildName = ''
guildRealm = ''
battlegroup = ''
achievementPoints = ''
guildLevel = ''
side = ''

#information about guild members
memberNames = []
memberClasses = []
memberRace = []
memberLevel = []
memberAchievementPoints = []

def returnVar(input):
	'''Takes a string of the form "var: val" and returns var.'''
	return input.split(':')[0])
	
def returnVal(input)
	'''Takes a string of the form "var: val" and returns val.'''
	return input.split(':')[1].lstrip()

def find_between( s, first, last ):
	'''Finds the string between two strings that appear first in another string.'''
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""
		
def find_between( s, first, last ):
	'''Finds the string between two strings that appear first in another string.'''
	try:
		start = s.index( first ) + len( first )
		end = s.rindex( last, start )
		return s[start:end]
	except ValueError:
		return ""

names = []
clean_lines = []

with file_orig as f:
	lines = f.readlines()
	clean_lines = [l.strip() for l in lines if l.strip()]
	clean_lines = [l.replace("}","") for l in clean_lines if l.replace("}","")]
	clean_lines = [l.replace("{","") for l in clean_lines if l.replace("{","")]
	clean_lines = [l.replace(",","") for l in clean_lines if l.replace(",","")]
	clean_lines = [l.replace("\"","") for l in clean_lines if l.replace("\"","")]
	clean_lines = [l.replace(" \"","\"") for l in clean_lines if l.replace(" \"","\"")]
	
with file_modified as f:
	f.writelines('\n'.join(clean_lines))
	
print(names)