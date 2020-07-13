from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from readCsv import read_csv
from recogQR import decode_qr_code

def todaySubmit():
    driver=webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()
    url2="http://ehall.hnuahe.edu.cn/new/index.html"
    #今日校园填报
    driver.get(url2)
    driver.find_element_by_xpath("/html[@class=' ieundefined']/body/div[@id='ampEhallBody']/article[@id='ampLoginInArticle']/article[@id='ampLoginArticle']/div[@id='ampLoginRoleNav']/div[@id='ampHasNoLogin']").click()
    time.sleep(1)
    driver.find_element('id','username').send_keys('81908')
    driver.find_element('id','password').send_keys('102014')
    driver.find_element_by_xpath("/html/body/div[@class='auth_page_wrapper']/div[@class='auth_login_content']/div[@class='auth_login_right']/div[@class='auth_tab']/div[@class='auth_tab_content']/div[@class='auth_tab_content_item']/form[@id='casLoginForm']/p[5]/button[@class='auth_login_btn primary full_width']").click()
    url3="http://ehall.hnuahe.edu.cn/qljfwapp/sys/lwReportEpidemic/index.do?amp_sec_version_=1&gid_=eVA5WE5VV3hWU3h3UUZOUXhnQkJTcEQ0ZjJvdUJoZU11SEVKMUxsWXdSMjZwd1FYdjNiQXRoNlhQdHplOUJKZnZqdHlnUCtSVzdYanZ3ZFhkVGw2YlE9PQ&EMAP_LANG=zh&THEME=indigo"
    driver.get(url3)
    time.sleep(3)
    # 新增
    driver.find_element_by_xpath("//div[@class='bh-btn bh-btn-primary']").click()
    time.sleep(3)
    #拖动滚动条到底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element('id','save').click()
    time.sleep(2)
    # driver.find_element_by_css_selector("bh-has-modal-body.bh-modal.bh-pop bh-card bh-card-lv4 bh-dialog-con.bh-dialog-btnContainerBox.bh-has-modal-bodybh-dialog-btn bh-bg-primary bh-color-primary-5").click()
    driver.find_element_by_class_name('bh-dialog-btn').click()
    driver.find_element_by_xpath("//div[@class='bh-btn bh-btn-primary']").click()
    text=driver.find_element_by_class_name('content').text
    isok='今日已填报'
    if isok in text:
        print('今日校园填报成功')
        driver.quit()

# todaySubmit()