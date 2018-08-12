import os


for file in os.listdir('E:/My Music/audio_cache/'):
	if "youtube" in file:
		splitFileName = file.split('-')
		cleanedSplitFileName = splitFileName[2:]
		newFileName = "".join(cleanedSplitFileName)
		print('Renaming {0} to {1}.'.format(file,newFileName))
		os.rename(file,newFileName)
		print('...done!')