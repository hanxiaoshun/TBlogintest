from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import uuid
import time
import json
import time
import requests
import re
import random
import os
from io import BytesIO
import re
from PIL import Image
import requests
from requests.cookies import RequestsCookieJar

s = requests.session()
# from PIL import Image
# import math
# from bs4 import BeautifulSoup

# 注意：以下设置将体现在 谷歌浏览器： 版本 74.0.3729.169（正式版本） （32 位），
# 以及selenium 谷歌客户端已经设置好，版本需要同步
# 用户参数设置区域，如果改变了账户名和密码，那么以下内容中如果是基于requests请求那么请求头和cookie设置需要重新设置
# 另外如果更换了爬虫服务的机器，那么也请重新设置请求头和cookie设置

# 以下单位皆为 秒
login_retry = 10  # 后台尝试登陆间隔次数
left = 594 - 110
top = 445 - 110

width = 1200
height = 700
delay = 1

#  基于起始位置参数设置所要截取的图片尺寸 （为了防止偏差，最好实际测试）
right = left + 115
bottom = top + 40

# 请求头和cookie设置
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

chrome_options = Options()
# 不弹出浏览器模式，不弹出浏览器模式默认网页size
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--user-agent=' + user_agent)
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--log-level=3')  # 添加屏蔽
# chrome_options.add_argument('--proxy-server={}'.format(proxy))
# # 配置忽略ssl错误
# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['acceptSslCerts'] = True
# capabilities['acceptInsecureCerts'] = True
# browser = webdriver.Chrome(desired_capabilities=capabilities)
# chrome_driver = '../Application/chromedriver.exe'  # 手动指定使用的浏览器位置
# chrome_driver = '../Application/chromedriver.exe'  # 手动指定使用的浏览器位置
chrome_driver = r"D:\PycharmProjects\taobaolive\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,
                          chrome_options=chrome_options)


class TaoBaoLive(object):
    def __init__(self):
        # self.session = requests.session()
        # self.cookies = requests.cookies.RequestsCookieJar()
        self.init_width = 1200
        self.init_height = 700
        self.root_url = 'https://login.taobao.com/member/login.jhtml?sub=true&redirectURL=https%3A%2F%2Fliveplatform.taobao.com%2Flive%2FaddLive.htm'
        self.login_username = "李凤杰0923"
        self.login_password = "li13503300183"
        self.driver = None

    # def cookie_fetch_126(self):
    #     main_header = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #         'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #         'Connection': 'keep-alive'
    #     }

    # def login_126(self):
    #
    #     main_header = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #         'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #         'Connection': 'keep-alive'
    #     }
    #     post_data = {'username': self.login_username, 'url2': self.login_url2, 'password': self.login_password}
    #     response = self.session.request('post',
    #                                     'https://mail.126.com/',
    #                                     data=post_data,
    #                                     headers=main_header,
    #                                     cookies=self.cookies,
    #                                     verify=False)  # 传递cookie
    #     # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
    #     self.session.cookies.update(response.cookies)
    #     # {"gid": "2498864890707537149", "type": 2, "sitekey": "6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya"}
    #     text = response.text
    def get_open_QRCode(self, xcode_url):
        print(xcode_url)
        response = requests.get(xcode_url)
        xcode_path = 'D:/PycharmProjects/taobaolive/static/img/xcode.png'
        if os.path.exists(xcode_path):
            os.remove(xcode_path)
        else:
            pass

        with open(xcode_path, 'wb') as f_xcode:
            f_xcode.write(response.content)

        # time.sleep(3)
        # img = Image.open(xcode_path)
        # img.show()

    def test_show_QRCode(self):
        xcode_path = 'D:/PycharmProjects/taobaolive/static/img/xcode.png'
        img = Image.open(xcode_path)
        img.show()

    def get_xcode(self):
        try:
            driver.set_window_size(self.init_width, self.init_height)
            driver.get(self.root_url)
            all_windows = driver.window_handles
            print('登录之前所有窗口', all_windows)
            cookies = driver.get_cookies()
            print("登录之前的cookie：%s " % str(cookies))
            print("登录之前的url：%s " % driver.current_url)
            match_group = re.match(
                r'.*?<img src="//img.alicdn.com/imgextra/(.*?)-xcode.png">.*?">',
                str(driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
            page_xcode = ''
            if match_group:
                if match_group.group(1):
                    print(match_group.group(1))
                    page_xcode = match_group.group(1)
                else:
                    xpath_click_QC = '//*[@id="J_LoginBox"]/div[1]/div[1]'
                    element_class_click = self.driver.find_element_by_xpath(
                        xpath_click_QC)
                    if element_class_click:
                        element_class_click.click()
                        time.sleep(2)
                        match_group = re.match(
                            r'.*?<img src="//img.alicdn.com/imgextra/(.*?)-xcode.png">.*?">',
                            str(driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
                        if match_group.group(1):
                            print(match_group.group(1))
                            page_xcode = match_group.group(1)
            else:
                time.sleep(2)
                js = 'setTimeout(function(){document.getElementById("J_Quick2Static").click()},100)'
                driver.execute_script(js)
                # xpath_click_QC = '//*[@id="J_LoginBox"]/div[1]/div[1]'
                # element_class_click = driver.find_element_by_xpath(xpath_click_QC)
                time.sleep(2)
                match_group = re.match(
                    r'.*?<img src="//img.alicdn.com/imgextra/(.*?)-xcode.png">.*?">',
                    str(driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
                if match_group:
                    if match_group.group(1):
                        print(match_group.group(1))
                        page_xcode = match_group.group(1)
                else:
                    return {'status': 'fail'}
            xcode_url = 'https://img.alicdn.com/imgextra/' + page_xcode + '-xcode.png'
            print(xcode_url)
            self.get_open_QRCode(xcode_url)
            self.driver = driver
            return {'status': 'ok'}
        except Exception as first_img_code_localutils_e:
            print("异常信息：%s " % str(first_img_code_localutils_e))
            raise first_img_code_localutils_e
        
    def finish_xcode(self):
        time.sleep(1)
        self.driver.refresh()
        all_windows = self.driver.window_handles
        print('登录之前所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之前的cookie：%s " % str(cookies))
        print("登录之前的url：%s " % self.driver.current_url)
        print(self.driver.page_source)
        print('------------==========---------------')
        # https://aq.taobao.com/durex/validate?param=7nmIF0VTf6m%2Bbx8wuCmPLTEdh1Ftef8%2BJfH%2FyeLO7VdDJzdZH6EtvEW5AK01mqsL1NFidBNPt6rI%2FdGZIliXlYc0WeTpx%2BCCWdcE%2BE6PElzqWjTNUbvwPAvrkXrCxVMWaKeARrd6nBLSzcnGbj%2B56MawxmNmMHpeA4EHqxSLO3xzcwybOEcX2Ha%2Frea%2BRg2RJ%2BjVa%2BHqcxSJ6QVjdsIVLRvwO0L8EwDMEjcHj0TId8iJ0zL1HttyoNS3Q%2FQhE0qTWqwPZWqaomVCK72xt0pnHsoeSXT8Nw6rvAmdnH6GQzBtDtrZxzwPxk8haunoT%2FLmyLS21k2UV91cVOLPWjJvG4zYK06O%2FwKfwaYoVLyW8YSS6DC%2F2bZHjNBRcWj%2FZrX0x%2FbdPToc2Q28PQpb5ZBoOhJaKTlujV5FXoRxB0N%2FbycNtzeU0XysoRmz3JoiQ5bPi500EHwNFKI%3D&redirecturl=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin_mid.htm
        match_group = re.match(
            r'.*?durex/validate(.*?)&redirecturl=https.*?',
            str(self.driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
        param = ''
        print(match_group)
        if match_group:
            if match_group.group(1):
                print(match_group.group(1))
                param = match_group.group(1)
        validate_url = 'https://aq.taobao.com/durex/validate'+param + \
            '&redirecturl=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin_mid.htm'
        self.driver.get(validate_url)
        print("---------------????????----------------")
        all_windows = self.driver.window_handles
        print('登录之前所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之前的cookie：%s " % str(cookies))
        print("登录之前的url：%s " % self.driver.current_url)
        print(self.driver.page_source)
        xpath_click_free = '//*[@id="J_Phone"]/ul/li[3]/input[1]'
        element_class_free = self.driver.find_element_by_xpath(xpath_click_free)
        if element_class_free:
            element_class_free.click()
            time.sleep(2)
            return {'status': 'ok', 'need': 'yes'}
        else:
            return {'status': 'ok', 'need': 'no'}

    def finish_xcode_x(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        all_windows = self.driver.window_handles
        print('登录之前所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之前的cookie：%s " % str(cookies))
        print("登录之前的url：%s " % self.driver.current_url)
        # 鼠标左键点击， 200为x坐标， 100为y坐标
        # self.driver.save_screenshot('foo.png')
        # ActionChains(self.driver).move_by_offset(860, 340).click().perform()
        ActionChains(self.driver).move_by_offset(885, 450).click().perform()
        time.sleep(1)
        return {'status': 'ok', 'need': 'yes'}

    def finish_xcode_bak(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        # 'D814197904344C8C773630C86B148B75E156C90E4FE1E7CA419FA7CF4F28EF9BE68DC942B6F2A08DCAF6C3F8BE425EDA434668EC30B62E088BF8F2182DFCBFF150'
        # 'D8178EFC218547DF0DEC8970482CB4C97BE9C8D47C49AF32E4CFE2C9F9305BAC637E95BF3D6F1986E3C62C08ACDD61EF4198515EB8A6186A129097158E079E5601'
        all_windows = self.driver.window_handles
        print('登录之前所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之前的cookie：%s " % str(cookies))
        print("登录之前的url：%s " % self.driver.current_url)
        # 鼠标左键点击， 200为x坐标， 100为y坐标
        # ActionChains(self.driver).move_by_offset(860, 340).click().perform()
        time.sleep(1)
        # self.driver.switch_to_frame('_oid_ifr_')
        # 'https://aq.taobao.com/durex/validate?'
        # 'param=7nmIF0VTf6m%2Bbx8wuCmPLTEdh1Ftef8%2BuaFsaUbuW%2FoN0BufRyldvdJ3AefdjXNzMui1QxLLsG%2FVKQ6Wv3GZp1qBG5U6dL%2BqxPfAIQOCjjoafPbyh7HxVZCJ8jwQAhFazVyu%2FgwQDkqMRQr0Nr4cBZodXnSFTbXwK5104TThP8ztxIPROp4oStX0Bth8bxtP5Zbo6aSqaPtp%2BysBu5zhDNMYBINut9H7z5zWdQC7w97%2F9V4WonNf9IxxCmiX%2BNwnqs4Hnn7xNfW3%2Fu4PZvaDEfeW9GnifQI19fOMXfhgdVmIUizYteb4ipqFyr5p8WRBV4igpg1ydbLso2GpSx2Y2oa0UerfYzfJd2syiuRR8NqztVqcgz8jl%2BpsIO3UMKEu4oMNa2BB3daxWHryAWVacRJkyMwDS%2FrUOV3Gv7V3GBKpFRPnkj910Yo9BfI56%2BhRHbvyGMiEhyRJajqc2PiBNOThuqD2CEtc%2Bn8%2FyPTox8kBaJsi%2BuTAaw%3D%3D&redirecturl=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin_mid.htm'
        # ActionChains(self.driver).move_by_offset(200, 100)
        # .context_click().perform() # 鼠标右键点击
        print(self.driver.page_source)
        print('------------==========---------------')
        # https://aq.taobao.com/durex/validate?param=7nmIF0VTf6m%2Bbx8wuCmPLTEdh1Ftef8%2BJfH%2FyeLO7VdDJzdZH6EtvEW5AK01mqsL1NFidBNPt6rI%2FdGZIliXlYc0WeTpx%2BCCWdcE%2BE6PElzqWjTNUbvwPAvrkXrCxVMWaKeARrd6nBLSzcnGbj%2B56MawxmNmMHpeA4EHqxSLO3xzcwybOEcX2Ha%2Frea%2BRg2RJ%2BjVa%2BHqcxSJ6QVjdsIVLRvwO0L8EwDMEjcHj0TId8iJ0zL1HttyoNS3Q%2FQhE0qTWqwPZWqaomVCK72xt0pnHsoeSXT8Nw6rvAmdnH6GQzBtDtrZxzwPxk8haunoT%2FLmyLS21k2UV91cVOLPWjJvG4zYK06O%2FwKfwaYoVLyW8YSS6DC%2F2bZHjNBRcWj%2FZrX0x%2FbdPToc2Q28PQpb5ZBoOhJaKTlujV5FXoRxB0N%2FbycNtzeU0XysoRmz3JoiQ5bPi500EHwNFKI%3D&redirecturl=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin_mid.htm
        match_group = re.match(
            r'.*?durex/validate(.*?)&redirecturl=https">.*?">',
            str(self.driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
        param = ''
        print(match_group)
        if match_group:
            if match_group.group(1):
                print(match_group.group(1))
                param = match_group.group(1)
        validate_url = 'https://aq.taobao.com/durex/validate'+param + \
            '&redirecturl=https%3A%2F%2Flogin.taobao.com%2Fmember%2Flogin_mid.htm'
        self.driver.get(validate_url)

        all_windows = self.driver.window_handles
        print(' validate_url 窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("validate_url 的cookie：%s " % str(cookies))
        print("validate_url 的url：%s " % self.driver.current_url)

        print(self.driver.page_source)
        match_group = re.match(
            r'.*?"code":"D8(.*?)"},{"type":"securityPhone".*?">',
            str(self.driver.page_source), re.M | re.I | re.S | re.IGNORECASE)
        code = ''
        if match_group:
            if match_group.group(1):
                print(match_group.group(1))
                code = match_group.group(1)
        code = 'D8' + code

        print(code)

        cookies = self.driver.get_cookies()
        with open('cookies.txt', 'w', encoding='utf-8') as sele_cookie_foo:
            json.dump(cookies, sele_cookie_foo)
        # 这里我们使用cookie对象进行处理
        jar = RequestsCookieJar()
        with open("cookies.txt", "r") as fp:
            cookies = json.load(fp)
            for cookie in cookies:
                jar.set(cookie['name'], cookie['value'])
        print('jar ::', jar)
        s.headers = {"User-Agent": user_agent}
        # 'checkType: phone
        # target: D84541D6B371E6D9837781D1D7576912EA940C47AF74EF4A63614ECB96F9DBA71C3BDCCAC73310AC0A668D5D61AC612854B7BDCF4731397B72BC0D98D1A25ABBCE
        # safePhoneNum: 
        # checkCode: '
        data = {'checkType': 'phone', 'target': code, 'safePhoneNum': '', 'checkCode': ''}
        sendcode_url = 'https://aq.taobao.com/durex/sendcode' + param + '&checkType=phone'
        r = s.post(sendcode_url, data=data, cookies=jar)

        print(r.status_code)
        print(r.url)
        print(r.text)
        return {'status': 'ok', 'need': 'yes'}
        # print('J_SendCodeBtn' in self.driver.page_source)
        # if 'J_SendCodeBtn' in self.driver.page_source:
        #     print("J_SendCodeBtn")
        #     print('J_SendCodeBtn' in self.driver.page_source)
        #     js_J_SendCodeBtn = "setTimeout(function(){document.getElementsByClassName('J_SendCodeBtn').click()},100)"
        #     driver.execute_script(js_J_SendCodeBtn)
        #     return {'status': 'ok', 'need': 'yes'}
        # else:
        #     xpath_click_free = '//*[@id="J_LoginBox"]/div[1]/div[1]'
        #     element_class_free = self.driver.find_element_by_xpath(
        #         xpath_click_free)
        #     if element_class_free:
        #         element_class_free.click()
        #         time.sleep(2)
        #         return {'status': 'ok', 'need': 'yes'}
        #     else:
        #         return {'status': 'ok', 'need': 'no'}

    def phone_captcha_Code(self, captcha_Code):
        all_windows = self.driver.window_handles
        print('登录之前所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之前的cookie：%s " % str(cookies))
        print("登录之前的url：%s " % self.driver.current_url)
        input_captcha_Code = '//*[@id="J_Phone"]/ul/li[5]/input'
        enter_xpath = '//*[@id="J_FooterSubmitBtn"]'
        element_input = self.driver.find_element_by_xpath(input_captcha_Code)
        element_input.clear()
        element_input.send_keys(captcha_Code)
        element_input = self.driver.find_element_by_xpath(enter_xpath)
        element_input.click()
        time.sleep(5)
        self.driver.get('https://login.taobao.com/member/login_by_safe.htm?allp=&sub=false&guf=&c_is_scure=&from=tb&type=1&style=&minipara=&css_style=&tpl_redirect_url=https%3A%2F%2Fliveplatform.taobao.com%2Flive%2FaddLive.htm&popid=&callback=&is_ignore=&trust_alipay=&full_redirect=&user_num_id=833462752&need_sign=&from_encoding=&not_duplite_str=&sign=&login_type=11&loginsite=0&appkey=00000000&qrlogin=&keyLogin=&newMini2=')
        
        all_windows = self.driver.window_handles
        print('登录之后所有窗口', all_windows)
        cookies = self.driver.get_cookies()
        print("登录之后cookie：%s " % str(cookies))
        print("登录之后的url：%s " % self.driver.current_url)
        
        return {'status': 'ok', 'need': 'yes'}
        # print('J_SafeCode')
        # print('J_SafeCode' in self.driver.page_source)
        # if 'J_SafeCode' in self.driver.page_source:
        #     js_J_SafeCode = "setTimeout(function(){document.getElementsByClassName('J_SafeCode').value='" + \
        #                                 captcha_Code + "'},100)"
        #     driver.execute_script(js_J_SafeCode)
        #     print('J_FooterSubmitBtn')
        #     print('J_FooterSubmitBtn' in self.driver.page_source)
        #     if 'J_FooterSubmitBtn' in self.driver.page_source:
        #         js_J_FooterSubmitBtn = "setTimeout(function(){document.getElementById('J_FooterSubmitBtn').click()'},100)"
        #         driver.execute_script(js_J_FooterSubmitBtn)
        #         return {'status': 'ok', 'need': 'yes'}
        #     else:
        #         return {'status': 'fail', 'need': '提交验证码失败'}
        # else:
        #     return {'status': 'fail', 'need': 'no'}

    # def mymovefile(self, srcfile, dstfile):
    #     if not os.path.isfile(srcfile):
    #         print(srcfile)
    #     else:
    #         fpath, fname = os.path.split(dstfile)    #分离文件名和路径
    #         if not os.path.exists(fpath):
    #             os.makedirs(fpath)                #创建路径
    #         which.remove(srcfile, dstfile)          #移动文件
    #         print("move %s -> %s" % (srcfile, dstfile))


if __name__ == '__main__':
    taoBaoLive = TaoBaoLive()
    # taoBaoLive.test_show_QRCode()
    taoBaoLive.get_xcode()
    taoBaoLive.test_show_QRCode()
    taoBaoLive.finish_xcode()
