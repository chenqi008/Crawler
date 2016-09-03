
from PIL import Image, ImageStat
# define by myself
import snakes_category


if __name__ == '__main__':

    # extract the files' name under FindPath
    FindPath = './bing2_resize/'
    FileNames = snakes_category.get_fileNames(FindPath)

    # # calculate total value of pixel of all images ordering by 'RGB'
    # total_value_list = [0.0, 0.0, 0.0]
    # # calculate total number of pixel of all images ordering by 'RGB'
    # total_pixel_list = [0.0, 0.0, 0.0]

    # the total mean, Var and image counting
    total_mean = [0.0, 0.0 ,0.0]
    total_Var = [0.0, 0.0 ,0.0]
    image_counting = 0
    category_counting = 0

    # traversing the categories of snake
    for category in FileNames:
        # extract the num of images
        FindImagePath = FindPath + category + '/'
        ImageNums = snakes_category.get_fileNames(FindImagePath)

        category_counting += 1

        print "Id of Category: %s"%(category_counting)
        print "Current Category: %s"%(category)

        # travesing the num of each category
        for image_num in ImageNums:

            image_counting += 1
            
            # locating the current image's path
            current_image = FindImagePath + image_num
            
            # open image and get its station
            img = Image.open(current_image)
            stat = ImageStat.Stat(img)

            # # the sum of current image's value
            # temp_sum = stat.sum
            # # the number of pixel for current image
            # temp_count = stat.count

            # the ordering of 'RGB'
            for i in xrange(3):
                # total_value_list[i] += temp_sum[i]
                # total_pixel_list[i] += temp_count[i]
                total_mean[i] += stat.mean[i]
                total_Var[i] += stat.var[i]


    # the final value
    final_mean = [0.0, 0.0 ,0.0]
    final_Var = [0.0, 0.0 ,0.0]

    for f in xrange(3):
        final_mean[f] = total_mean[f]/image_counting
        final_Var[f] = total_Var[f]/image_counting


    print "The final mean is :", final_mean
    print "The final Var is :", final_Var




    # # calculate the total means
    # mean_RGB = [0.0, 0.0, 0.0]
    # for p in len(mean_RGB):
    #     mean_RGB[p] = total_value_list[p]/total_pixel_list[p]





# im01 = Image.open('./3.jpg')
# im02 = Image.open('./6.jpg')
# # r, g, b = im02.split()

# stat = ImageStat.Stat(im01)
# # print stat.sum
# # print stat.count
# print im02.mode
# print im02.size
# print stat.extrema
# print stat.mean[0]
# print stat.var


# # stat_r = ImageStat.Stat(im01, r)
# # print stat_r.sum
# # print stat_r.count


# # stat_g = ImageStat.Stat(im01, g)
# # print stat_g.sum
# # print stat_g.count


# # stat_b = ImageStat.Stat(im01, b)
# # print stat_b.sum
# # print stat_b.count






