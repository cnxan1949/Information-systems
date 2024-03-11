from selenium import webdriver
import time
import requests
import os

# 设置 Chrome WebDriver 的路径
driver_path = 'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe'

# 目标网站的URL
base_url = 'https://www.shutterstock.com/zh/search/asians-with-sad-expressions?people_number=1&sort=relevant&category=People&ethnicity=chinese&ethnicity=japanese&ethnicity=southeast_asian&ethnicity=south_asian&mreleased=true&authentic=true&page='


start_page = 1
end_page = 3

download_folder = 'C:/Users/韩韩/Desktop/my_downloaded_images'


driver = webdriver.Chrome(driver_path)


for page in range(start_page, end_page + 1):
    url = base_url + str(page)
    print(f'Scraping page {page}...')
    
    driver.get(url)
    time.sleep(2)  

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  
    

    img_elements = driver.find_elements_by_tag_name('img')
    img_urls = [img.get_attribute('src') for img in img_elements if img.get_attribute('src')]
    

    count = 1
    for img_url in img_urls:
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_name = f'{page}_{count}.jpg'
            img_path = os.path.join(download_folder, img_name)
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print(f'Downloaded: {img_name}')
            count += 1


driver.quit()
