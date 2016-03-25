'''
USING http://www.tvmaze.com/ API
Script to iterate through all TV Series in TVmaze DB. 
Using a python implementation of the TV Maze REST API. #https://github.com/srob650/pytvmaze
The TVmaze DB holds information about 14803 Tv Series. 
'''

import pytvmaze as PTM
import sys


lowerLimit = 1
upperLimit = 14803

if __name__ == "__main__":
	for id in range(lowerLimit,upperLimit):
		try:
			show = PTM.get_show(maze_id = id,embed = 'episodes')
			numberOfSeasons = len(show.seasons)
			nameOfTheShow = show.name
			try:
				f = open('series.txt','a')
				s = nameOfTheShow+" has "+str(numberOfSeasons)+" seasons."
				f.write(s+'\n')
				f.close()
			except Exception as e:
				print e
				pass
		except Exception as e:
			f = open('series.txt','a')
			f.write(str(e) + '\n')
			f.close()