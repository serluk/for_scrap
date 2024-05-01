import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://code-white.com/blog/'

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

driver.get(url)

ELEMENTS_ARTICLES = [elem.get_attribute('href') for elem in
                     driver.find_elements(By.CSS_SELECTOR, ".blog-post_title")]

n = 1
for elem in ELEMENTS_ARTICLES:
    driver.get(elem)
    article_dict = {}
    article_dict["title"] = driver.find_element(By.CSS_SELECTOR, ".single-blog-post-content-wrapper > h1").get_attribute("innerText")
    article_dict["text"] = driver.find_element(By.CSS_SELECTOR, ".single-blog-post-content-wrapper").get_attribute("innerText")
    # article_dict["date"] = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")
    date_field = driver.find_element(By.CSS_SELECTOR, ".article-header > div").get_attribute("innerText")
    article_dict["date"] = datetime.strptime(date_field, '%b %d, %Y').isoformat()
    images = [elem.get_attribute('src') for elem in driver.find_elements(By.CSS_SELECTOR, 'p > img')]
    article_dict["images"] = images
    article_dict["author"] = driver.find_element(By.CSS_SELECTOR, ".blog-header_author").get_attribute("innerText")
    with open(str(n) + ".json", "w") as file:
        json.dump(article_dict, file, indent=4)
    print(f'{n}.json saved')
    n += 1

driver.quit()




