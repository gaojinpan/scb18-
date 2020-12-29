

from selenium import webdriver   #导入包

driver = webdriver.Chrome()    # 启动浏览器 初始化
driver.get('http://erp.lemfix.com/login.html')   # 打开一个网址

driver.maximize_window()  # 浏览器窗口最大化

# 输入用户名、密码点击登录
driver.find_element_by_id('username').send_keys('13916686542')  #找到元素；输入用户名
driver.find_element_by_id('password').send_keys('lemon123')   #找到元素；输入密码
driver.find_element_by_id('btnSubmit').click()    #找到元素；点击登录

