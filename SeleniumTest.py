"""
自动化打开chrome
"""
import sys
from selenium import webdriver

class Selenium_Test(object):
    def Baidu_Select_Element_By_ID(self):
        """
        创建webdriver类型的对象 wd ,运行浏览器驱动，并运行Chrome浏览器
        等号右边 返回的是 WebDriver 类型的对象，我们可以通过这个对象来操控浏览器
        比如 打开网址、选择界面元素等。
        """
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        # r表示后面字符串中的 \ 不是转义
        """
        使用 WebDriver实例对象的 get方法 可以让浏览器打开指定网址
        执行下面这行代码时，自动化程序就发起了 打开百度网址的 请求消息 ，
        通过浏览器驱动， 给 Chrome浏览器。
        Chrome浏览器接收到该请求后，就会打开百度网址，通过浏览器驱动， 
        告诉自动化程序 打开成功。
        """
        wd.get('https://www.baidu.com')
        # wd.get('http://www.python3.vip')

        """
        操控界面元素 之前 先选择元素（告诉浏览器，要操作的这个web元素的特征）
        """
        # 根据id选择元素，返回该元素对应的WebElement对象
        element = wd.find_element_by_id('kw')

        # 通过该对象，可以对页面元素进行操作
        # 比如 输入字符串 到 这个输入框里
        element.send_keys('白月黑羽\n')
        # \n 表示回车，进入搜索，也可以用点击 百度一下 进入搜索
        # element.send_keys('白月黑羽')
        # element = wd.find_element_by_id('su')
        # element.click()

        # from time import sleep
        # sleep(2)

        # 设置 最大等待时长 为10s
        wd.implicitly_wait(10)

        element = wd.find_element_by_id('kw')
        print(element.get_attribute('value'))

        element = wd.find_element_by_id('3')
        sys.stdout.write(str(element.text) + '\n')

        elem = element.find_elements_by_tag_name('h3')
        # elem = [str(elem.text) for elem in elem]
        print(elem[0].text)
        # 获取元素属性
        element = element.get_attribute('innerHTML')
        print(element)


        # 关闭浏览器窗口
        wd.quit()

    def Select_Element_By_Class(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

        elements = wd.find_elements_by_class_name('plant')
        # for element in elements:
        #     sys.stdout.write(str(element) + '\n')
        #     print(element.text)  # text属性 指的是该类型对应的文本内容

        ele = [str(element.text) for element in elements]
        sys.stdout.write(str(ele) + '\n')

    def Select_Element_By_Tag(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

        elements = wd.find_elements_by_tag_name('span')
        # for element in elements:
        #     sys.stdout.write(str(element) + '\n')
        #     print(element.text)  # text属性 指的是该类型对应的文本内容

        ele = [str(element.text) for element in elements]
        sys.stdout.write(str(ele) + '\n')

    def Select_Element_By_WebElement(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

        element = wd.find_element_by_id('container')

        # 限制 选择元素的范围是 id 为 container 元素的内部
        spans = element.find_elements_by_tag_name('span')

        span = [str(span.text) for span in spans]
        sys.stdout.write(str(span) + '\n')

    def Select_Element_By_CSS_Selector(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')

        wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

        element = wd.find_elements_by_css_selector('#container #inner11 > span')
        # elem = [str(element.text) for element in element]
        for elem in element:
            sys.stdout.write(elem.get_attribute('outerHTML') + '\n')

        ele = wd.find_elements_by_css_selector('div#bottom > div.footer1')
        for elem in ele:
            print(elem.get_attribute('outerHTML'))


        ele = wd.find_elements_by_css_selector('.plant, #bottom')
        for elem in ele:
            print(elem.get_attribute('outerHTML'))
        wd.quit()

    def Select_Element_By_CSS_Selector_nth(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')

        wd.get('http://cdn1.python3.vip/files/selenium/sample1b.html')
        wd.implicitly_wait(10)

        element = wd.find_elements_by_css_selector(':nth-child(2)')
        # elem = [str(element.text) for element in element]
        for elem in element:
            sys.stdout.write(elem.get_attribute('outerHTML') + '\n')

        wd.quit()

    def Select_Frame(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')

        wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')

        # 切换到frame里面
        wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))
        element = wd.find_elements_by_css_selector('.plant')
        elem = [str(elem.get_attribute('outerHTML')) for elem in element ]
        sys.stdout.write(str(elem) + '\n')

        # 切换回最外部的HTML中
        wd.switch_to.default_content()
        wd.find_element_by_css_selector('#outerbutton').click()

        from time import sleep
        sleep(5)
        wd.quit()

    def Select_Window(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.implicitly_wait(10)
        wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

        element = wd.find_element_by_css_selector('a')
        element.click()
        # wd.title属性是当前窗口的标题栏 文本
        print(wd.title)
        # 保存当前窗口句柄
        mainwindow = wd.current_window_handle

        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if 'Bing' in wd.title:
                break
        print(wd.title)
        new_window = wd.find_element_by_css_selector('#sb_form_q')
        new_window.send_keys('白月黑羽')
        new_window = wd.find_element_by_id('sb_form_go')
        new_window.click()

        from time import sleep
        sleep(2)

        # 切换为原来的窗口
        wd.switch_to.window(mainwindow)
        print(wd.title)
        elem = wd.find_element_by_css_selector('button#outerbutton')
        elem.click()

        sleep(5)
        wd.quit()

    def Select_Radio_Checkbox_Select(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.implicitly_wait(10)
        wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

        # radio 单选框
        element = wd.find_element_by_css_selector('#s_radio input[checked="checked"]')
        print(element.get_attribute('value'))

        element = wd.find_element_by_css_selector('#s_radio input[value="小江老师"]')
        element.click()

        # checkbox 复选框
        checkbox = wd.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')
        for box in checkbox:
            box.click()

        wd.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()

        # select选择框
        # 导入select类
        from selenium.webdriver.support.ui import Select
        # 创建Select对象,单选框
        select = Select(wd.find_element_by_css_selector('#ss_single'))
        # 通过select对象选中小雷老师
        select.select_by_value('小雷老师')

        # 多选框
        select = Select(wd.find_element_by_css_selector('#ss_multi'))
        # 清除所有已经选中的选项
        select.deselect_all()
        # 选择小雷老师和小凯老师
        select.select_by_value("小雷老师")
        select.select_by_visible_text("小凯老师")

        from time import sleep
        sleep(5)

        wd.quit()

    def Other(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.implicitly_wait(10)
        wd.get('https://www.baidu.com/')

        from selenium.webdriver.common.action_chains import ActionChains
        ac = ActionChains(wd)  # webdriver对象作为参数传入

        # 鼠标移动到元素上
        ac.move_to_element(
            wd.find_element_by_css_selector('[name="tj_briicon"]')
        ).perform()

        from time import sleep
        sleep(5)
        wd.quit()

    def Xpath(self):
        wd = webdriver.Chrome(r'D:\Chrome\chromedriver_win32\chromedriver.exe')
        wd.implicitly_wait(5)
        wd.get('http://cdn1.python3.vip/files/selenium/test2.html')
        elem = wd.find_elements_by_xpath('//div')
        for ele in elem:
            print(ele.get_attribute('outerHTML'))

        from time import sleep
        sleep(5)

        wd.quit()


if __name__ == '__main__':
    selenium_test = Selenium_Test()
    # selenium_test.Baidu_Select_Element_By_ID()
    # selenium_test.Select_Element_By_Class()
    # selenium_test.Select_Element_By_Tag()
    # selenium_test.Select_Element_By_WebElement()
    # selenium_test.Select_Element_By_CSS_Selector()
    # selenium_test.Select_Element_By_CSS_Selector_nth()
    # selenium_test.Select_Frame()
    # selenium_test.Select_Window()
    # selenium_test.Select_Radio_Checkbox_Select()
    # selenium_test.Other()
    selenium_test.Xpath()