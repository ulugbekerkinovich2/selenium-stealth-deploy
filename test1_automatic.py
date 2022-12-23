import os
import time
from test import speedtest1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from django.db import connection
def selenium_upload():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM upload_data")
    all_data = cursor.fetchall()
    cursor.execute("SELECT * FROM mylevel")
    all_data1 = cursor.fetchall()
    my_data = all_data1[0][-1]
    # print(my_data)
    # print(all_data)
    arr = []
    for i in range(len(all_data)):
        print(all_data[i])
        arr.append(all_data[i])
    arr1 = arr[-1]
    # print(arr1)
    link_for_get_data = arr1[1]
    login_for_that_site = arr1[2]
    password_for_that_site = arr1[3]
    link_for_that_site2 = arr1[4]
    login_for_that_site2 = arr1[5]
    password_for_that_site2 = arr1[6]
    folder_path = str(arr1[7])
    which_level = arr1[8]
    course_name = arr1[9]

    print(link_for_get_data, login_for_that_site, password_for_that_site, link_for_that_site2, login_for_that_site2,
          password_for_that_site2, folder_path,which_level,course_name, 'shu')
    replace_folder_path = folder_path.replace("str(\\)", "str(\)")
    print('replace_folder_path', replace_folder_path)

    input_link = 'https://intranet.ytit.uz/course/view.php?id=3577'
    input_link = f"{link_for_get_data}"
    # dir_path = 'ORAL BIOLOGY (RUS)'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://intranet.ytit.uz/login/index.php")
    driver.find_element(By.NAME, 'username').send_keys('ier20037')
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys('AC2558243')
    time.sleep(3.2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div[2]/div[1]/form/button').click()
    time.sleep(2.5)
    # link = input("linkni kiriting >>>  ")
    driver.get(input_link)
    # title1 = driver.find_element(By.TAG_NAME, 'h1').text
    # print(title1, type(title1))
    time.sleep(2.5)
    driver.refresh()
    # title = driver.find_elements(By.TAG_NAME, 'h3')
    # data = [element.text for element in title]

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
        if 'https://intranet.ytit.uz/mod/folder' in str(link):
            folder_link.append(link)
            print('folder yoq ekan')
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
        print(len(my_folder_links))
        my_folder_file_length_list.append(len(my_folder_links))
    print(my_folder_file_length_list,'my_folder_file_length_list')
    for i in url_link:
        driver.get(i)
        print(driver.current_url)
        a = driver.current_url
        if 'https://intranet.ytit.uz/mod/url' not in a:
            a = driver.current_url
            yotube_links.append(a)
            print(a)
    time.sleep(1.5)
    print(link_for_get_data)
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

    for k in range(0, len(f_data)):
        try:
            if all_texts[f_data[k]] == all_texts[f_data[k + 1]]:
                del f_data[k + 1]
        except:
            print('bajarildi')
    print('yangilangan ', f_data)

    print(all_h3)
    f_data.sort(reverse=False)
    print('f_data', f_data)
    print(all_texts)

    indeks_files_video_urok = [i for i in range(0, len(all_texts)) if all_texts[i] == "Видео-урок"]
    print('indeks_files_video_urok', indeks_files_video_urok)

    indeks_files = [i for i in range(0, len(all_texts)) if all_texts[i] == "Файл"]
    print('indeks_files', indeks_files)
    print('len indeks_files', len(indeks_files))
    folder_path1 = folder_path.replace("str(\\)","str(\)")
    print('replace',folder_path1)
    # newpath = rf'C:\Users\ulugbek\Downloads\{dir}'
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    all_files = []
    all_sizes = []
    # 'C:\Users\ulugbek\Downloads\Russian language 1 (English groups) D. Kambarova'
    dir_name = f"{folder_path1}"
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(replace_folder_path, x)), os.listdir(replace_folder_path ))
    list_of_files = sorted(list_of_files, key=lambda x: os.path.getmtime(os.path.join(replace_folder_path, x)))
    for file_name in list_of_files:
        # file_path = os.path.join(dir_name, file_name)
        # timestamp_str = time.strftime('%m/%d/%Y :: %H:%M:%S',
        #                               time.gmtime(os.path.getmtime(file_path)))
        # file_size = os.stat(f'C:/Users/ulugbek/Downloads/{dir_path}/{file_name}')
        file_size = os.stat(f'{folder_path1}/{file_name}')
        print("file_size.st_size", file_size.st_size)
        mb = file_size.st_size / 1048576
        # print('file_size', file_size.st_size)
        # print('mb',mb)
        # print(timestamp_str, ' -->', file_name, mb, 'MB')
        all_files.append(file_name)
        all_sizes.append(mb)
    print("all_files", all_files)
    print('all_sizes', all_sizes)
    # time.sleep(1000)

    # driver.get("https://lms.spprt.uz/#/auth/login")
    driver.get(f"{link_for_that_site2}")
    time.sleep(2)
    driver.refresh()
    time.sleep(4)
    login = driver.find_element(By.NAME, 'number')
    time.sleep(6)
    login.send_keys(f"{login_for_that_site2}")
    time.sleep(0.5)
    password = driver.find_element(By.NAME, 'passwordField')
    time.sleep(0.5)
    password.send_keys("password")
    time.sleep(0.1)
    driver.find_element(By.XPATH, '/html/body/div[1]/section/div/form/div[3]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        # '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/button[1]').click()
                            '/html/body/div/div[2]/div[1]/nav/div[2]/nav/div/a[2]/div').click()
    time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/nav/div[2]/nav/div/a[2]/div').click()
    time.sleep(2.1)
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div[2]/div[1]/div').click()
    driver.find_element(By.XPATH, f'{my_data}').click()
    time.sleep(1)
    text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/h3').text
    print('text', text, course_name)
    for eles in range(1, 12):
        try:
            course_names = driver.find_element(By.XPATH,  f'/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[{eles}]/div[2]/div[1]/div/div[1]/div[2]/h3').text
            time.sleep(1)
            course_detail = driver.find_element(By.XPATH,
                                                f"/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/div[{eles}]/div[2]/div[3]/div[2]/button")
            print("course_name",course_name)
            if course_names == course_name:
                time.sleep(2)
                print(course_names, course_name, 'shu edi')
                course_detail.click()
                time.sleep(3)
        except:
            print('course names topilmadi')

    time.sleep(1.2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/ul/li[2]/a/span').click()
    time.sleep(1)
    try:
        for i in range(0, len(all_h3) + 1):
            if i > 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
                print('cycle02', cycle)
            if i == 0:
                cycle = all_texts[0:f_data[i]]
                print('cycle0', cycle)
            if i != 0:
                cycle = all_texts[f_data[i - 1]:f_data[i]]
                print('cycle1', cycle)
            if i == 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
                print('cycle01', cycle)

            if len(cycle) >= 2 or 'Файл' in cycle or ('Папка' in cycle):
                time.sleep(0.5)
                driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/button').click()
                time.sleep(3)
                input_week = driver.find_element(By.NAME, 'week_number')
                input_week.send_keys(i)
                input_topic_name = driver.find_element(By.NAME, 'name')
                # input_topic_name.send_keys(all_h3[i])
                input_topic_name.send_keys(all_files[0].split('.')[0])
                input_description = driver.find_element(By.TAG_NAME, 'textarea')
                print('yotube_links', yotube_links)
                try:
                    for i in range(0, len(cycle)):
                        print('kelgan cycle', cycle)
                        if 'Гиперссылка' in cycle[i]:
                            input_description.click()
                            time.sleep(0.2)
                            input_description.send_keys(yotube_links[0] + '\n')
                            print('Гиперссылка', yotube_links[0])
                            time.sleep(0.2)
                            del yotube_links[0]
                except:
                    print('gipersilka yoq')
                try:
                    for i in range(0, len(cycle)):
                        if len(cycle[i]) >= 0:
                            if cycle[i] == 'Файл' or cycle[i] == 'Папка':
                                continue
                            input_description.click()
                            input_description.send_keys(cycle[i] + ' ')
                except:
                    print('description yoq')
                time.sleep(0.4)
                print('len cycle up', len(cycle))
                all1 = []
                all_sizes1 = []
                for i1 in range(0, len(cycle)):
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
                    time.sleep(0.5)
                    if cycle[i1] == 'Папка':
                        print(my_folder_file_length_list[0])
                        for k1 in range(0, len(my_folder_file_length_list)):
                            print('k1',k1)
                            for k in range(0, my_folder_file_length_list[k1]):
                                print('k',k)
                                all_file1 = f"{folder_path1}\{all_files[k]}"
                                print('all_file1',all_file1)
                                all_sizes1.append(all_sizes[k])
                                print('all_sizes[k]',all_sizes[k])
                                all1.append(all_file1)
                                print('all_file1', all_file1)
                                del all_files[k]
                                del all_sizes[k]
                    else:
                        continue
                print('barcha olingan fayllar ',all1)
                all2 = ' \n '.join(all1)
                all3 = sum(all_sizes1)
                print(all_sizes1)
                print(all3, 'MB')
                print(all2)
                input_file = driver.find_element(By.NAME, 'file')

                try:
                    print(all3)
                    # if all3 <= 0.1:
                    time_speed = speedtest1()
                    print(time_speed, 'time_speed----------------------------------------')
                    input_file.send_keys(all2)
                    if all3<=1:
                        a = (all3*800)/time_speed
                        print("a",a)
                        time.sleep(a)
                    b = (all3*8)/time_speed
                    print('b',b)
                    time.sleep(b)
                except:
                    print('file yoq ekan')
                try:
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/button[2]').click()
                    print('successfully saved ✅ ')
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(0.5)
                except:
                    print('fail ❌ ')
        driver.close()
    except:
        print('finished')