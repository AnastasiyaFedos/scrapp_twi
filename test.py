import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementClickInterceptedException

counter = int(input("с какого числа начинаем: "))

def download_image(image_url, file_name, link):
    # Отправляем GET-запрос на URL изображения
    response = requests.get(image_url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Открываем файл для записи в бинарном режиме
        with open(file_name, 'wb') as file:
            file.write(response.content)  # Записываем содержимое изображения в файл
        print(f"Изображение сохранено как {file_name}")

        with open("download_arts_reze.txt", "a", encoding="utf-8") as file:
            file.write(file_name + " " + link + '\n') 
    else:
        print("Не удалось скачать изображение. Статус:", response.status_code)

# Укажите путь к скачанному chromedriver (или используйте его, если он в PATH)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://x.com/login")
time.sleep(7)

#close_button_start = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="xMigrationBottomBar"]')
#close_button_start.click()

#cookie_accept_button = driver.find_element(By.XPATH, "//span[text()='Принять все файлы cookie']")
#cookie_accept_button.click()

#вход на твиттер

input_element = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
#input_element.send_keys("+79279205004")
input_element.send_keys("khrystalq@gmail.com")
input_element.send_keys(Keys.ENTER)

time.sleep(5)

pass_element = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
#pass_element.send_keys(">p_JqE%<d26Uz%z")
pass_element.send_keys("627015394MINd"),
pass_element.send_keys(Keys.ENTER)

time.sleep(5)

#counter = 53

for i in range(300):
    counter += 1

    driver.get("https://x.com/i/bookmarks")
    time.sleep(7)
    post_element = driver.find_element(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
    #print(post_element.get_attribute("outerHTML"))
    post_element.send_keys(Keys.ENTER)

    #photo_child_link = post_element.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetPhoto"]')
    post = driver.find_elements(By.CSS_SELECTOR, '[role="link"]')


    for link in post:

        href = link.get_attribute("href")
        if href is None:  # Проверяем, если href == None
            continue  # Пропускаем эту итерацию
        
        link_split = href.split('/')
        if 'photo' in link_split:
            photo_child_link = href
            break


        '''link_split = link.get_attribute("href").split('/')
        if 'photo' in link_split:
            photo_child_link = link.get_attribute("href")
            break'''

    driver.get(photo_child_link)
    time.sleep(6)

    try:
        post = driver.find_element(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
        print(post.get_attribute("outerHTML"))
        images = post.find_elements(By.CSS_SELECTOR, 'img[alt="Изображение"]')

        for el in images:
            print(el.get_attribute("outerHTML"))
    
        # Перебираем каждое изображение в посте
        for idx, image in enumerate(images):
            # Получаем ссылку на изображение
            link = image.get_attribute("src")
            # Обрабатываем ссылку для лучшего качества
            '''if "large" in link:
                link = link.replace("large", "4096x4096")
            elif "small" in link:
                link = link.replace("small", "4096x4096")
            elif "medium" in link:
                link = link.replace("medium", "4096x4096")
            elif "900x900" in link:
                link = link.replace("900x900", "4096x4096")'''
            
            link_split = link.split("=")
            link_split[-1] = '4096x4096'
            link = '='.join(link_split)
            # Скачиваем изображение, добавляя индекс к имени файла
            download_image(link, f"{counter}_{idx + 1}.png", photo_child_link)

        try:
        
            like_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="like"]')
            print('like_button' + like_button .get_attribute("outerHTML"))
            actions = ActionChains(driver)
            actions.move_to_element(like_button).perform()  
            #like_button.click()
            driver.execute_script("arguments[0].click();", like_button)

        except NoSuchElementException:
            like_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="unlike"]')
            print('unlike_button   ' + like_button .get_attribute("outerHTML"))

        time.sleep(2)

        try:
            bookmark_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="removeBookmark"]')
            print('1 rbookmark        ' + bookmark_button .get_attribute("outerHTML"))
            driver.execute_script("arguments[0].click();", bookmark_button)

        except NoSuchElementException:
            bookmark_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="bookmark"]')
            print('1 bookmark     ' + bookmark_button .get_attribute("outerHTML"))
            bookmark_button.click()

            time.sleep(2)

            rbookmark_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="removeBookmark"]')
            print('2 rbookmark       ' + bookmark_button .get_attribute("outerHTML"))
            rbookmark_button.click()  

            time.sleep(2)  
        
        time.sleep(2)

        """close_button = driver.find_element(By.CSS_SELECTOR, 'button[arial-label="Закрыть"]')
        close_button.click()

        time.sleep(3)"""

    except NoSuchElementException:

        retweet_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="retweet"]')
        print('retweet     ' + retweet_button .get_attribute("outerHTML"))
        retweet_button.click()

        time.sleep(2)

        bookmark_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="removeBookmark"]')
        print('rbookmark     ' + bookmark_button .get_attribute("outerHTML"))
        bookmark_button.click()

        time.sleep(2)

        close_button = driver.find_element(By.CSS_SELECTOR, 'button[arial-label="Закрыть"]')
        close_button.click()

""" current_links_post = []
links_post = driver.find_elements(By.CSS_SELECTOR, '[role="link"]')
for link in links_post:
    link_split = link.get_attribute("href").split('/')
    if 'photo' in link_split:
        current_links_post.append(link.get_attribute("href")) 

print(current_links_post)

current_links_photo = []
links_photo = driver.find_elements(By.CSS_SELECTOR, 'img[alt="Изображение"]')
for link in links_photo: 
    current_links_photo.append(link.get_attribute("src")) """

time.sleep(5)

"""with open("links.txt", "w") as file:
    for i in range(len(current_links_post) - 1):
        string = current_links_post[i] + " " + current_links_photo[i] 
        file.write(string + '/n')"""

driver.quit()
