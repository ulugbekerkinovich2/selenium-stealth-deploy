import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from test import wait_t, telebots, telebots2, telebots3
from django.db import connection

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.headless = True
# driver = webdriver.Chrome(executable_path="C:\Users\ulugbek\PycharmProjects\deployed\chromedriver.exe")
driver = webdriver.Chrome(options=options)

stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)


def selenium_upload():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM upload_data")
    all_data = cursor.fetchall()
    wait_ti = wait_t()
    wait_ti1 = wait_ti[-1][8]

    print("wait_ti10", wait_ti1)
    telebots2("wait_ti10", wait_ti1)
    # cursor.execute("SELECT * FROM mylevel")
    # all_data1 = cursor.fetchall()
    # my_data = all_data[0][-1]
    # print(my_data)
    print(all_data)
    telebots(all_data)
    arr = []
    for i in range(len(all_data)):
        print(all_data[i])
        # telebots(all_data[i])
        arr.append(all_data[i])
    arr1 = arr[-1]
    # print(arr1)
    link_for_get_data = arr1[1]
    # login_for_that_site = arr1[2]
    # password_for_that_site = arr1[3]
    link_for_that_site2 = arr1[2]
    login_for_that_site2 = arr1[3]
    password_for_that_site2 = arr1[4]
    folder_path = str(arr1[5])
    which_level = arr1[6]
    course_name = arr1[7]
    title = str(arr1[9])
    print(link_for_get_data,link_for_that_site2,login_for_that_site2,password_for_that_site2,folder_path,which_level,course_name, 'shu')
    # telebots(link_for_get_data+link_for_that_site2+login_for_that_site2+password_for_that_site2+folder_path+which_level+course_name, 'shu')
    # telebots(link_for_get_data, link_for_that_site2, login_for_that_site2,
    #       password_for_that_site2, folder_path, which_level, course_name, 'shu')
    replace_folder_path = folder_path.replace("str(\\)", "str(\)")
    print('replace_folder_path', replace_folder_path)
    telebots2('replace_folder_path', replace_folder_path)
    input_link = f"{link_for_get_data}"

    # chrome_options = Options()
    # chrome_options.headless = True
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-notifications')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("window-size=1280,720")

    # chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)




    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    # driver = webdriver.Chrome(executable_path="")
    # driver = webdriver.Chrome(executable_path="/root/pixlfy/projectenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/root/chromedriver")


    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    time.sleep(5)
    driver.get("https://intranet.ytit.uz/login/index.php")
    driver.find_element(By.NAME, 'username').send_keys('ier20037')
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys('AC2558243')
    time.sleep(3.2)
    button = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div[2]/div[1]/form/button')
    button.click()
    time.sleep(2.5)
    driver.get(input_link)
    time.sleep(2.5)
    driver.refresh()
    all_data = driver.find_element(By.XPATH, '//*[@id="region-main"]').text
    data = all_data.split(' ')
    data1 = ' '.join(map(str, data))
    data2 = data1.split('\n')
    for i in data2:
        print(i)
    url_link = []
    yotube_links = []
    lists = []
    folder_link = []
    elems = driver.find_elements(By.TAG_NAME, 'a')
    for elem in elems:
        link = elem.get_attribute('href')
        if 'https://intranet.ytit.uz/mod/resource/' in str(link):
            # print(link)  # todo bu linklar
            lists.append(link)
        if 'https://intranet.ytit.uz/mod/url/' in str(link):
            url_link.append(link)
        if 'https://intranet.ytit.uz/mod/folder' in str(link) or 'https://intranet.ytit.uz/pluginfile' in str(link):
            folder_link.append(link)
            print('folder yoq ekan')
            telebots('folder yoq ekan')
    my_folder_file_length_list = []
    for folder in folder_link:
        driver.get(folder)
        all_links = driver.find_elements(By.TAG_NAME, 'a')
        my_folder_links = []
        for links in all_links:
            link1 = links.get_attribute('href')
            if 'https://intranet.ytit.uz/pluginfile.php/' in link1:
                my_folder_links.append(link1)
        print('my_folder_links', my_folder_links)
        telebots2('my_folder_links', my_folder_links)
        telebots(len(my_folder_links))
        my_folder_file_length_list.append(len(my_folder_links))
    # print(my_folder_file_length_list, 'my_folder_file_length_list')
    for i in url_link:
        driver.get(i)
        # print(driver.current_url)
        a = driver.current_url
        if 'https://intranet.ytit.uz/mod/url' not in a:
            a = driver.current_url
            yotube_links.append(a)
            # print(a)
    time.sleep(1.5)
    # print(link_for_get_data)
    telebots(link_for_get_data)
    driver.get(f"{link_for_get_data}")
    # print(len(lists))  # todo bu linklar soni
    time.sleep(2)
    all_texts = []  # todo all_texts
    all_data = driver.find_element(By.XPATH, '//*[@id="region-main"]').text
    data = all_data.split(' ')
    data1 = ' '.join(map(str, data))
    data2 = data1.split('\n')
    all_h3 = []
    h3 = driver.find_elements(By.TAG_NAME, 'h3')
    for i in h3:
        if i.text != '':
            # print(i.text, 'h3 tags')
            all_h3.append(i.text)
    fake_data = ['Ваши достижения', 'Тематический план', 'Объявления', 'Форум', "O'quv qo'llanma", 'Общее', '']
    for i in data2:
        if i not in fake_data and i != '':
            # print(i)
            all_texts.append(i)
        else:
            continue
    f_data = []

    for el in all_h3:
        indeks_of_week = [i for i in range(0, len(all_texts)) if el == all_texts[i]]
        # print('indeks of week ', indeks_of_week)
        for i in indeks_of_week:
            if i not in f_data:
                f_data.append(i)
    try:
        for k in range(0, len(f_data)):
            if all_texts[f_data[k]] == all_texts[f_data[k + 1]]:
                del f_data[k + 1]
    except:
        # print('bajarildi')
        telebots('bajarildi')
    telebots2('yangilangan ', f_data)
    telebots(all_h3)
    f_data.sort(reverse=False)
    indeks_files_video_urok = [i for i in range(0, len(all_texts)) if all_texts[i] == "Видео-урок"]
    telebots2('indeks_files_video_urok', indeks_files_video_urok)
    indeks_files = [i for i in range(0, len(all_texts)) if all_texts[i] == "Файл"]
    telebots2('indeks_files', indeks_files)
    folder_path1 = folder_path.replace("str(\\)", "str('\')")
    all_files = []
    all_sizes = []
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(replace_folder_path, x)), os.listdir( replace_folder_path))
    list_of_files = sorted(list_of_files, key=lambda x: os.path.getmtime(os.path.join(replace_folder_path, x)))
    for file_name in list_of_files:
        # file_path = os.path.join(dir_name, file_name)
        timestamp_str = time.strftime('%m/%d/%Y :: %H:%M:%S',
                                      time.gmtime(os.path.getmtime(f'{folder_path1}/{file_name}')))
        # file_size = os.stat(f'C:/Users/ulugbek/Downloads/{dir_path}/{file_name}')
        file_size = os.stat(folder_path)
        # telebots(file_size)
        # telebots2("timestamp_str", timestamp_str)
        file_size = os.stat(f'{folder_path1}/{file_name}')
        # telebots2("file_size.st_size", file_size.st_size)
        mb = file_size.st_size / 1048576
        # telebots2('file_size', file_size.st_size)
        # telebots2('mb',mb)
        # telebots4(timestamp_str, ' -->', file_name, mb, 'MB')
        all_files.append(file_name)
        all_sizes.append(mb)
    counts = 0
    telebots(all_files)
    telebots(all_sizes)
    # driver.get("https://lms.spprt.uz/#/auth/login")
    driver.get(f"{link_for_that_site2}")
    if len(all_data) >= 100:
        cursor.execute(f"DELETE FROM upload_data WHERE id = {counts}")
    time.sleep(2)
    driver.refresh()
    driver.maximize_window()
    time.sleep(5)
    login = driver.find_element(By.NAME, 'number')
    time.sleep(3)
    login.send_keys(f"{login_for_that_site2}")
    time.sleep(1)
    password = driver.find_element(By.NAME, 'passwordField')
    time.sleep(0.5)
    password.send_keys("password")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/section/div/form/div[3]/button').click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/div[1]/nav/div[2]/nav/div/a[2]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH, f'{which_level}').click()
    time.sleep(1)
    for eles in range(1, 12):
        time.sleep(1)
        course_names = driver.find_element(By.XPATH,  f'/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[{eles}]/div[2]/div[1]/div/div[1]/div[2]/h3').text
        print('course_names', course_names)
        telebots2('course_names', course_names)
        time.sleep(1)
        course_detail = driver.find_element(By.XPATH,
                                            f'/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[{eles}]/div[2]/div[3]/div[2]/button')
        time.sleep(1)
        print("course_name", course_name)
        telebots2("course_name", course_name)
        try:
            if course_names.lower() == course_name.lower():
                time.sleep(2)
                # print(course_names, course_name, 'shu edi')
                telebots3(course_names, course_name, 'shu edi')
                course_detail.click()
                time.sleep(1.5)
                break
        except:
            print('course names topilmadi')
            telebots('course names topilmadi')
    time.sleep(1)
    SPAN = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/ul/li[2]/a/span')
    time.sleep(2)
    SPAN.click()
    time.sleep(2)
    try:
        for i in range(0, len(all_h3) + 1):
            if i > 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
            if i == 0:
                cycle = all_texts[0:f_data[i]]
            if i != 0:
                cycle = all_texts[f_data[i - 1]:f_data[i]]
            if i == 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
            if (len(cycle) >= 2) or ('Файл' in cycle) or ('Папка' in cycle):
                time.sleep(0.5)
                driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/button').click()
                time.sleep(3)
                input_week = driver.find_element(By.NAME, 'week_number')
                input_week.send_keys(i)
                input_topic_name = driver.find_element(By.NAME, 'name')
                if title == "True":
                    input_topic_name.send_keys(all_h3[i])
                else:
                    input_topic_name.send_keys(all_files[0].split('.')[0])
                input_description = driver.find_element(By.TAG_NAME, 'textarea')
                telebots2('youtube_links', yotube_links)
                try:
                    for i3 in range(0, len(cycle)):
                        telebots2('kelgan cycle', cycle)
                        if 'Гиперссылка' in cycle[i3]:
                            input_description.click()
                            time.sleep(0.2)
                            input_description.send_keys(yotube_links[0] + '\n')
                            telebots2('Гиперссылка', yotube_links[0])
                            time.sleep(0.2)
                            del yotube_links[0]
                except:
                    try:
                        print('gipersilka yoq')
                        telebots('gipersilka yoq')
                        for i2 in range(0, len(cycle)):
                            if len(cycle[i]) >= 0:
                                if cycle[i] == 'Файл' or cycle[i2] == 'Папка':
                                    continue
                                input_description.click()
                                input_description.send_keys(cycle[i2] + ' ')
                    except:
                        print('description yoq')
                        telebots('description yoq')
                time.sleep(0.4)
                # print('len cycle up', len(cycle))
                telebots2('len cycle up', len(cycle))
                all1 = []
                all_sizes1 = []
                for i1 in range(0, len(cycle)):
                    telebots2('cycle', cycle)
                    if ('Видео-урок' in cycle[i1] or 'Proyeksiyalash mashqlar' in cycle[i1]) and cycle[i1 + 1] == 'Файл' or 'Гиперссылка' in cycle[i1].strip():
                        continue
                    if cycle[i1] == 'Файл':
                        all_file = f"{folder_path1}\{all_files[0]}"
                        all_sizes1.append(all_sizes[0])
                        all1.append(all_file)
                        del all_files[0]
                        del all_sizes[0]
                    else:
                        continue
                count = 0
                telebots2('all_files3'+'\n\n', all_files)
                for get_folder in range(0, len(cycle)):
                    if cycle[get_folder] == 'Папка':
                        telebots('PAPKA GA KIRDI')
                        telebots2('len my_folder_file_length_list', len(my_folder_file_length_list))
                        telebots2('len my_folder_file_length_list', my_folder_file_length_list)
                        for k in range(0, my_folder_file_length_list[count]):
                            all_file1 = f"{folder_path1}\{all_files[0]}"
                            telebots2('all_file1', all_file1)
                            all_sizes1.append(all_sizes[0])
                            all1.append(all_file1)
                            telebots2('all_file1', all_file1)
                            del all_files[0]
                            del all_sizes[0]
                            if len(all1) == sum(my_folder_file_length_list):
                                count += 1
                                break
                            # print('k', k)
                print('barcha olingan fayllar ', all1)
                all2 = ' \n '.join(all1)
                all3 = sum(all_sizes1)
                telebots(all_sizes1)
                telebots2(all3, 'MB')
                telebots2('yuklanvotgan faylla', all2)
                input_file = driver.find_element(By.NAME, 'file')
                try:
                    telebots(all3)
                    input_file.send_keys(all2)
                    time.sleep(wait_ti1)
                except:
                        print('file yoq ekan')
                        telebots('file yoq ekan')
                try:
                    time.sleep(0.5)
                    # driver.save_screenshot('')
                    driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/button[2]').click()
                    print('successfully saved ✅ ')
                    telebots('successfully saved ✅ ')
                    counts += 1
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(0.5)
                except:
                    print('fail ❌ ')
                    telebots('fail ❌ ')
    except:
        print('finished')
        telebots('finished')
        time.sleep(1)
        driver.close()
