# import os
# import time
#
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# from test import telebots
# def yukla():
#     input_link = "https://intranet.ytit.uz/course/view.php?id=3508"
#
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#     driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://intranet.ytit.uz/login/index.php")
#     driver.find_element(By.NAME, 'username').send_keys('ier20037')
#     time.sleep(2)
#     driver.find_element(By.NAME, 'password').send_keys('AC2558243')
#     time.sleep(3.2)
#     button = driver.find_element(By.XPATH,
#                                  '/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div[2]/div[1]/form/button')
#     button.click()
#     time.sleep(2.5)
#     driver.get(input_link)
#     time.sleep(2.5)
#     driver.refresh()
#     all_data = driver.find_element(By.XPATH, '//*[@id="region-main"]').text
#     data = all_data.split(' ')
#     data1 = ' '.join(map(str, data))
#     data2 = data1.split('\n')
#     all = []
#     super_link = []
#     for i in data2:
#         # print(i)
#         all.append(i)
#     # url_link = []
#     # yotube_links = []
#     lists = []
#     # folder_link = []
#     elems = driver.find_elements(By.TAG_NAME, 'a')
#     for elem in elems:
#         link = elem.get_attribute('href')
#         if 'https://intranet.ytit.uz/mod/resource/' in str(link):
#             # print(link)  # todo bu linklar
#             lists.append(link)
#     # print(len(lists), lists)
#
#     for k in lists:
#         time.sleep(0.5)
#         driver.get(k)
#         super_link.append(driver.current_url)
#         driver.back()
#         time.sleep(2)
#     telebots(super_link)
#     print(super_link)
#
#
