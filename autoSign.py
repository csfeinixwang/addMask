from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from readCsv import read_csv
from recogQR import decode_qr_code
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

#学校编码
url=decode_qr_code()
if url is None:
    url="http://jktb.haedu.gov.cn/?ext=fHp3MD8zNygxeXx9OS41&rn=1564346163"
print(url)
# 读取手机号和身份证后四位
userMobile=read_csv()[0][1]
idCard=read_csv()[1][1]
city=read_csv()[2][1]
area= read_csv()[3][1]
print(userMobile)
print(idCard)
print(city)
print(area)



driver=webdriver.Chrome(executable_path='chromedriver.exe')
# time.sleep(1)

driver.maximize_window()
# time.sleep(1)







# print('123')
driver.get(url)

# ul = driver.find_element_by_xpath('/html/body/ul/li[2]/span').click()
#教师
WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/ul/li[2]/span')).click()

# ul1=driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div/button').click()
# time.sleep(1)
# 不能反复测试太快，服务器不允许
isappera=WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('schoolName').is_displayed())
if(isappera):
    # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('btn-warning')).click()
    print(isappera)
    time.sleep(1)
    # driver.find_element_by_class_name('btn-warning').click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('btn-warning')).click()

# driver.find_element_by_class_name('btn-warning').click()

#输入你的手机和身份证号后4位
# userMobile='13598036457'
# idCard='2014'
# driver.find_element('name','mobile').send_keys(userMobile)
# driver.find_element('name','idCard').send_keys(idCard)
# isdispear=WebDriverWait(driver,10).until_not(lambda x: x.find_element_by_class_name('btn-warning').is_displayed())
isappera1=WebDriverWait(driver,15).until(lambda x:x.find_element_by_class_name('form-control').is_displayed())
if(isappera1):
    print(isappera1)
    time.sleep(1)
    WebDriverWait(driver, 15,5).until(lambda x: x.find_element_by_xpath("/html[@class='pixel-ratio-2 retina']/body/div[@class='container my-content']/form[@id='my-form']/div[@class='form-group'][1]/div[@class='col-sm-10']/input[@class='form-control']")).send_keys(userMobile)
    WebDriverWait(driver, 15,5).until(lambda x: x.find_element_by_xpath("/html[@class='pixel-ratio-2 retina']/body/div[@class='container my-content']/form[@id='my-form']/div[@class='form-group'][2]/div[@class='col-sm-10']/input[@class='form-control']")).send_keys(idCard)
    # driver.find_element('name','mobile').send_keys(userMobile)
    # driver.find_element('name','idCard').send_keys(idCard)
    driver.find_element_by_class_name('btn-primary').click()
    print('进入2次')




#driver.find_element("name","password").send_keys("yourpassword")
# time.sleep(2)
# 确认进入第二次的填报
# ul4=driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div/div/div/button').click()
# ul4=driver.find_element_by_xpath("/html[@class='pixel-ratio-2 retina']/body/div[@class='container my-content']/form[@id='my-form']/div[@class='form-group'][5]/div[@class='col-sm-offset-2 col-sm-10']/div[@class='row']/div[@class='col-lg-12 col-md-12 col-sm-12 col-xs-12']/button[@class='btn btn-primary']").click()

# WebDriverWait(driver,10).until(lambda x: x.find_element_by_class_name('btn-primary')).click()
# driver.find_element_by_class_name('btn-primary').click()

# time.sleep(4)
# driver.find_element_by_xpath('/html/body/ul/li[1]/span').click()
WebDriverWait(driver,10,3).until(lambda x: x.find_element_by_xpath("/html/body/ul[@class='fill-tab-new']/li[1]")).click()

# time.sleep(2)
# 填写上报地点
# select1=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]').click()
# WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]')).click()
# time.sleep(1)



# 省
# for i in range(1,22):
#     driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/ul/li['+str(i)+']').click()
#     time.sleep(1)

#市 1郑州市
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/ul/li['+city+']').click()
# time.sleep(1)

#区 1中原区 2 二七区
# loc='1'
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[3]/ul/li['+area+']').click()
# time.sleep(1)

# 确定区域
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/button[2]').click()
# time.sleep(1)

#最后提交
for i in range(2):
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[16]/button').click()

isok=WebDriverWait(driver,5).until(lambda x:x.find_element_by_class_name("fill-tab-new").text)
str1="提交成功"
result1= str1 in isok
if(result1):
    driver.quit()
print(result1)



# driver.quit()

# url2="http://ehall.hnuahe.edu.cn/new/index.html?browser=no"

#今日校园填报
from todaySchool import todaySubmit
todaySubmit()

