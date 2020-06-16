from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from readCsv import read_csv
from recogQR import decode_qr_code
from todaySchool import todaySubmit

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
time.sleep(1)

driver.maximize_window()
time.sleep(1)







print('123')
driver.get(url)

ul = driver.find_element_by_xpath('/html/body/ul/li[2]/span').click()
time.sleep(1)

ul1=driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div/button').click()
time.sleep(1)





#输入你的手机和身份证号后4位
# userMobile='13598036457'
# idCard='2014'
driver.find_element('name','mobile').send_keys(userMobile)
driver.find_element('name','idCard').send_keys(idCard)
#driver.find_element("name","password").send_keys("yourpassword")
time.sleep(2)
# 确认进入第二次的填报
# ul4=driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div/div/div/button').click()
ul4=driver.find_element_by_xpath("/html[@class='pixel-ratio-2 retina']/body/div[@class='container my-content']/form[@id='my-form']/div[@class='form-group'][5]/div[@class='col-sm-offset-2 col-sm-10']/div[@class='row']/div[@class='col-lg-12 col-md-12 col-sm-12 col-xs-12']/button[@class='btn btn-primary']").click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/ul/li[1]/span').click()
time.sleep(2)
# 填写上报地点
select1=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]').click()
time.sleep(1)
# 省
for i in range(1,22):
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/ul/li['+str(i)+']').click()
    time.sleep(1)

#市 1郑州市
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/ul/li['+city+']').click()
time.sleep(1)

#区 1中原区 2 二七区
loc='1'
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[3]/ul/li['+area+']').click()
time.sleep(1)

# 确定区域
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/button[2]').click()
time.sleep(1)
#最后提交
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[16]/button').click()
time.sleep(3)

# url2="http://ehall.hnuahe.edu.cn/new/index.html?browser=no"

#今日校园填报
todaySubmit()

# driver.get(url2)
#
# driver.find_element_by_xpath("/html[@class=' ieundefined']/body/div[@id='ampEhallBody']/article[@id='ampLoginInArticle']/article[@id='ampLoginArticle']/div[@id='ampLoginRoleNav']/div[@id='ampHasNoLogin']").click()
#
# time.sleep(1)
# driver.find_element('id','username').send_keys('81908')
# driver.find_element('id','password').send_keys('102014')
#
# driver.find_element_by_xpath("/html/body/div[@class='auth_page_wrapper']/div[@class='auth_login_content']/div[@class='auth_login_right']/div[@class='auth_tab']/div[@class='auth_tab_content']/div[@class='auth_tab_content_item']/form[@id='casLoginForm']/p[5]/button[@class='auth_login_btn primary full_width']").click()
# url3="http://ehall.hnuahe.edu.cn/qljfwapp/sys/lwReportEpidemic/index.do?amp_sec_version_=1&gid_=eVA5WE5VV3hWU3h3UUZOUXhnQkJTcEQ0ZjJvdUJoZU11SEVKMUxsWXdSMjZwd1FYdjNiQXRoNlhQdHplOUJKZnZqdHlnUCtSVzdYanZ3ZFhkVGw2YlE9PQ&EMAP_LANG=zh&THEME=indigo"
#
# driver.get(url3)