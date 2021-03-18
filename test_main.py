# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get(link)
# try:
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time, math
#
# page = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser.get(page)
#     link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
#     link.click()
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     answer = browser.switch_to.alert.text
#     print(answer)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     i1 = browser.find_element_by_css_selector('input[required]')
#     i1.send_keys('ivan')
#     i2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
#     i2.send_keys('ivanov')
#     i3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#     i3.send_keys('ivanov@gmail.com')
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     time.sleep(1)
#
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#
#     welcome_text = welcome_text_elt.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time, math
# browser = webdriver.Chrome(ChromeDriverManager().install())

# try:
#     link = 'http://suninjuly.github.io/math.html'
#     browser.get(link)
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_elem = browser.find_element_by_id('input_value')
#     x = x_elem.text
#     y = calc(int(x))
#
#     i1 = browser.find_element_by_id('answer')
#     i1.send_keys(y)
#
#     o1 = browser.find_element_by_id('robotCheckbox')
#     o1.click()
#
#     o2 = browser.find_element_by_id('robotsRule')
#     o2.click()
#
#     b1 = browser.find_element_by_tag_name('button')
#     b1.click()
#
#     a1 = browser.switch_to.alert
#     a1_text = a1.text
#     print(a1_text)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# import time, math
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/selects1.html'
#
# try:
#     browser.get(link)
#     n1 = browser.find_element_by_id('num1').text
#     n2 = browser.find_element_by_id('num2').text
#     res = str(int(n1) + int(n2))
#     s1 = Select(browser.find_element_by_tag_name("select"))
#     s1.select_by_value(res)
#     browser.find_element_by_css_selector(".btn").click()
#
#     a1 = browser.switch_to.alert.text
#     print(a1)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time, math
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://SunInJuly.github.io/execute_script.html'
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser.get(link)
#
#     x_elem = browser.find_element_by_id('input_value')
#     x = x_elem.text
#
#     i1 = browser.find_element_by_id('answer')
#     i1.send_keys(calc(x))
#
#     c1 = browser.find_element_by_id('robotCheckbox')
#     browser.execute_script('return arguments[0].scrollIntoView(true);', c1)
#     c1.click()
#
#     r1 = browser.find_element_by_id('robotsRule')
#     browser.execute_script('return arguments[0].scrollIntoView(true);', r1)
#     r1.click()
#
#     button = browser.find_element_by_css_selector('button[type="submit"]')
#     browser.execute_script('return arguments[0].scrollIntoView(true);', button)
#     button.click()
#
#     a1 = browser.switch_to.alert
#     print(a1.text)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time, os
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/file_input.html'
#
# try:
#     browser.get(link)
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'file.txt')
#
#     fn = browser.find_element_by_css_selector('input[name="firstname"]')
#     fn.send_keys('ivan')
#
#     ln = browser.find_element_by_css_selector('input[name="lastname"]')
#     ln.send_keys('ivanov')
#
#     em = browser.find_element_by_css_selector('input[name="email"]')
#     em.send_keys('ivanov@gmail.com')
#
#     up = browser.find_element_by_id('file')
#     up.send_keys(file_path)
#
#     btn = browser.find_element_by_css_selector('button[type="submit"]')
#     btn.click()
#
#     a1 = browser.switch_to.alert
#     print(a1.text)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time, math
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/alert_accept.html'
#
# try:
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     browser.get(link)
#
#     btn = browser.find_element_by_css_selector('button')
#     btn.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_elem = browser.find_element_by_id('input_value')
#     x = x_elem.text
#
#     a = browser.find_element_by_id('answer')
#     a.send_keys(calc(x))
#
#     btn1 = browser.find_element_by_tag_name('button')
#     btn1.click()
#
#     a1 = browser.switch_to.alert
#     print(a1.text)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time, math
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/redirect_accept.html'
#
# try:
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     browser.get(link)
#
#     btn = browser.find_element_by_class_name('trollface')
#     btn.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x_elem = browser.find_element_by_id('input_value')
#     x = x_elem.text
#
#     a = browser.find_element_by_id('answer')
#     a.send_keys(calc(x))
#
#     btn1 = browser.find_element_by_tag_name('button')
#     btn1.click()
#
#     a1 = browser.switch_to.alert
#     print(a1.text)
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()




# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math, time
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/explicit_wait2.html'
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser.get(link)
#     WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
#     browser.find_element(By.ID, 'book').click()
#     browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
#     browser.find_element_by_id("solve").click()
#     print(browser.switch_to.alert.text)
#
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.quit()




# import unittest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import math, time
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# link = 'http://suninjuly.github.io/registration1.html'
#
# class TestLesson(unittest.TestCase):
#     def test_reg(self):
#         try:
#             browser.get(link)
#             i1 = browser.find_element_by_css_selector('input[required]')
#             i1.send_keys('ivan')
#             i2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
#             i2.send_keys('ivanov')
#             i3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#             i3.send_keys('ivanov@gmail.com')
#             button = browser.find_element_by_css_selector("button.btn")
#             button.click()
#             time.sleep(1)
#             welcome_text_elt = browser.find_element_by_tag_name("h1")
#             welcome_text = welcome_text_elt.text
#             self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
#         except Exception as e:
#             print(e)
#         finally:
#             time.sleep(2)
#             browser.quit()
#
# if __name__ == "__main__":
#     unittest.main()



# import pytest, time, math
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# def sum(n,m):
#     return n+m
# @pytest.mark.parametrize('n1, n2, exp', [(3,5,8), (1,2,3), (-3,3,0)])
# def test_sum(n1, n2, exp):
#     assert sum(n1, n2) == exp


# import pytest, time, math
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser.maximize_window()
#     browser.implicitly_wait(10)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.mark.parametrize('pages', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
# def test_guest_should_see_login_link(browser, pages):
#     link = "https://stepik.org/lesson/{}/step/1".format(pages)
#     browser.get(link)
#     browser.find_element_by_css_selector('textarea').send_keys(str(math.log(int(time.time()))))
#     browser.find_element_by_class_name('submit-submission ').click()
#     res = browser.find_element_by_class_name('smart-hints__hint').text
#     assert res == 'Correct!', res

