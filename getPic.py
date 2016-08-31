from selenium import webdriver
import time
import urllib
import os
# define by myself
import snakes_category


# whether exist the folder, if not, generate it
def gene_folder(folder_path):
    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)


if __name__ == '__main__':
    
    # 启动Firefox浏览器
    driver = webdriver.Firefox()

    # 最大化窗口，因为每一次爬取只能看到视窗内的图片
    driver.maximize_window()

    # open web
    url = "http://cn.bing.com/images/trending?FORM=ILPTRD"
    driver.get(url)

    # list of snake's categories
    FindPath = './bing/'
    FileNames = snakes_category.get_fileNames(FindPath)

    # traversing each category
    for category in FileNames:
        # current access path
        current_folder = './draft/%s/'%(category)
        # judging if existed
        gene_folder(current_folder)

        # clear text-box
        driver.find_element_by_id("sb_form_q").clear()
        time.sleep(1)
        
        # input text into text-box
        driver.find_element_by_id("sb_form_q").send_keys(category.replace('_',' '))
        time.sleep(1)

        # search
        driver.find_element_by_id("sb_form_go").click()
        time.sleep(1)

        # # get the current url
        # curr_url = driver.current_url

        # 模拟滚动窗口以浏览下载更多图片
        pos = 0
        # 图片编号
        m = 0 
        for i in range(10):
            # 每次下滚500
            pos += i*500
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            time.sleep(1)   
            
            # for element in driver.find_elements_by_xpath(xpath):
            for element in driver.find_elements_by_tag_name("img"):
                img_url = element.get_attribute('src')
                # 保存图片到指定路径
                urllib.urlretrieve(img_url, '%s%s.jpg' % (current_folder, m))
                m += 1
        
    driver.close()

