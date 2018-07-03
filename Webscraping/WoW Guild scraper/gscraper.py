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
	return input.split(':')[0]
	
def returnVal(input):
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
realm = []
classes = ['guild']
race = ['guild']
gender = ['guild']
level = []
achievementPoints = []
spec = ['guild']
description = ['guild']
rank = ['guild']
memberCounter = 0
clean_lines = []

with file_orig as f:
	lines = f.readlines()
	clean_lines = [l.strip() for l in lines if l.strip()]
	clean_lines = [l.replace("}","") for l in clean_lines if l.replace("}","")]
	clean_lines = [l.replace("{","") for l in clean_lines if l.replace("{","")]
	clean_lines = [l.replace(",","") for l in clean_lines if l.replace(",","")]
	clean_lines = [l.replace("\"","") for l in clean_lines if l.replace("\"","")]
	clean_lines = [l.replace(" \"","\"") for l in clean_lines if l.replace(" \"","\"")]
	clean_lines = ["---" if "character" in x else x for x in clean_lines]
	clean_lines = ["" if "lastModified" in x else x for x in clean_lines]
	clean_lines = ["" if "backgroundImage" in x else x for x in clean_lines]	
	clean_lines = ["" if "thumbnail" in x else x for x in clean_lines]
	clean_lines = ["" if "icon" in x else x for x in clean_lines]
	clean_lines = ["" if "battlegroup" in x else x for x in clean_lines]
	clean_lines = ["" if "role" in x else x for x in clean_lines]
	clean_lines = ["" if "order" in x else x for x in clean_lines]
	clean_lines = ["" if "guild" in x else x for x in clean_lines]
	clean_lines = ["spec2" if "spec" in x else x for x in clean_lines]
	clean_lines = [l.replace("","") for l in clean_lines if l.replace("","")]
	
for i, line in enumerate(clean_lines):
	if "spec" in line:
		clean_lines[i+1] = clean_lines[i+1].replace("name","spec")

clean_lines = [l.replace("spec2","") for l in clean_lines if l.replace("spec2","")]

for line in clean_lines:
	if "name" in line:
		memberCounter += 1 
		names.append(line.split(':')[1].lstrip())
	if "realm" in line:
		realm.append(line.split(':')[1].lstrip())
	if "class" in line:
		classes.append(line.split(':')[1].lstrip())
	if "race" in line:
		race.append(line.split(':')[1].lstrip())
	if "gender" in line:
		gender.append(line.split(':')[1].lstrip())
	if "level" in line:
		level.append(line.split(':')[1].lstrip())
	if "achievementPoints" in line:
		achievementPoints.append(line.split(':')[1].lstrip())
	if "spec" in line:
		spec.append(line.split(':')[1].lstrip())
	if "description" in line:
		description.append(line.split(':')[1].lstrip())
	if "rank" in line: 
		rank.append(line.split(':')[1].lstrip())
		
with file_modified as f:
	f.writelines('\n'.join(clean_lines))
	

print(len(names))
print(len(level))
print(len(rank))
	
print('Name\t\tlevel\tspec\trank\t')
for i, val in enumerate(names):
	print('{0}\t\t{1}\t{2}'.format(names[i],level[i],rank[i]))
	
print('\nTotal members : {0}'.format(memberCounter))







