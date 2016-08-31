import Image
import os
# define by myself
import snakes_category


# whether exist the folder, if not, generate it
def gene_folder(folder_path):
	if os.path.exists(folder_path)==False:
		os.makedirs(folder_path)


# the function of resizing images
# "source_path" and "target_path" including files' name
def resize_images(source_path, target_path):
	# open image
	# img = Image.open('./4.jpg')
	# img = Image.open(source_path).convert('RGB')
	img = Image.open(source_path)

	# get rid of the the images of not-'RGB'
	if img.mode != 'RGB':
		return

	# w(width)，h(high)，最后一个参数指定采用的算法
	w = 500
	h = 500
	new_img= img.resize((w,h),Image.ANTIALIAS)

	# saving a new image
	# new_img.save('./4-new3.jpg',quality=100)
	new_img.save(target_path, quality=100)



if __name__ == '__main__':

	FindPath = './bing/'
	# list of snake's categories
	FileNames = snakes_category.get_fileNames(FindPath)


	# traversing the categories of snake
	for category in FileNames:

		# current access path
		current_folder = './bing_resize/%s'%(category)
		# judging if existed
		gene_folder(current_folder)

		# source images' path
		image_source_path = FindPath + category
		# get the images'name of each category
		imageNames = snakes_category.get_fileNames(image_source_path)

		print "category: %s"%(category)
		print "num_image: %s"%(len(imageNames))


		counter = 0
		# traversing the image file under current path
		for num_image in imageNames:
			counter += 1

			# defining source_path and target_path
			source_path = image_source_path + '/' + num_image
			target_path = current_folder + '/' + num_image

			# calligng the function to resize images
			resize_images(source_path, target_path)

			if counter%100 == 0:
				print "the %s image"%(counter)






