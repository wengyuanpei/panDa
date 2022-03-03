from  time import  sleep
from selenium import webdriver
from redis import StrictRedis


#获取redis键方法,redis的键是通过，图片地址最后的数字组合固定的键查出的

def logIn(id,pwd):
    url = "https://dev-scrm.964yx.com/#/login"
    dv=webdriver.Firefox()
    dv.implicitly_wait(10)
    dv.maximize_window()
    dv.get(url)
    sleep(5)
    # path1=dv.find_element_by_css_selector('[style="float: left;"]')
    path1=dv.find_element_by_xpath('//img[@style="float: left;"]').get_attribute("src")
    print("img地址是："+path1)
    code=path1[-13:]
    print("redis值："+code)
    # dv.quit()
    #********************************************************************************
    #获取验证码
    host = '192.168.84.39'
    port = 6379
    db = 0
    password = '123456'

    redispool = StrictRedis(
        host=host,
        port=port,
        db=db,
        password=password)
    redis_key='DEFAULT_CODE_KEY:CAPTCHA:'+code
    key_list=redispool.get(redis_key)
    key_code=key_list.decode()
    # print(key_list)
    # print(type(key_list))

    code_end=key_code[-6:-1]
    print("验证码："+code)
    #**************************************************************************************
    dv.find_elements_by_class_name('ant-input')[0].clear()
    dv.find_elements_by_class_name('ant-input')[0].send_keys(id)
    sleep(2)
    dv.find_elements_by_class_name('ant-input')[1].send_keys(pwd)
    sleep(2)
    dv.find_elements_by_class_name('ant-input')[2].send_keys(code_end)
    sleep(2)
    dv.find_element_by_class_name('ant-btn-primary').click()
    sleep(2)
    # url_now=dv.current_url
    sleep(2)
    # print('当前请求的页面：'+url_now)

id='17345043365'
pwd='123456'
logIn(id,pwd)





# logIn('17345043365','123456')




#
# def getRides_Code(code_redis):
#     host = '192.168.84.39'
#     port = 6379
#     db = 0
#     password = '123456'
#
#
#     redispool = StrictRedis(
#         host=host,
#         port=port,
#         db=db,
#         password=password)
#
#     redis_key='DEFAULT_CODE_KEY:CAPTCHA:'+code_redis
#     key_list=redispool.get(redis_key)
#     key_code=key_list.decode()
#     code=key_code[-6:-1]
#     print("验证码："+code)
#     return code


# 这是一个登录系统获取令牌的方法
# url = "https://dev-scrm.964yx.com/#/login"
# code_redis=getRides_key()
# code=getRides_Code(code_redis)
# id='17345043365'
# pwd='123456'
# code =code
# driver=webdriver.Firefox()
# # driver.get(url)
# # driver.implicitly_wait(10)
# sleep(2)
#
# driver.find_elements_by_class_name('ant-input')[0].clear()
# driver.find_elements_by_class_name('ant-input')[0].send_keys(id)
# driver.find_elements_by_class_name('ant-input')[1].send_keys(pwd)
# driver.find_elements_by_class_name('ant-input')[2].send_keys(code)
# driver.find_element_by_class_name('ant-btn-primary').click()
