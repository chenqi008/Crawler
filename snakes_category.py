import os



# get the names of file or folder under the current folder
def get_fileNames(FindPath):

	FileNames = os.listdir(FindPath)
	
	FileNames.sort()

	# print FileNames
	# print len(FileNames)

	return FileNames


if __name__ == '__main__':

	FindPath = './bing/'

	FileNames = get_fileNames(FindPath)





