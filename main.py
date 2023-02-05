from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def find_url_restaurants(driver):
    print('Started Scrapping the page...')
    wait = WebDriverWait(driver, 2)
    while True:
        try:
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.load-more-holder button')))
            driver.execute_script("arguments[0].click();", button)
        except:
            break
    restaurants = driver.find_element(By.CLASS_NAME, 'rest-list.clearfix').find_elements(By.CLASS_NAME ,'r-i')
    links = [restaurant.get_attribute('href') for restaurant in restaurants]
    print(f'Scrapping finished.')
    print(f'Number of links: {len(links)}')
    return links



def link_city(cities):
    DOMAIN = 'https://www.delino.com'
    all_restuarant_types_link = {}
    restuarants_types = ['Pizza', 'Kebab','Soup', 'Sandwich','Persian_food','Crispy','Pasta',
    'Salad','Breakfast', 'Steak']
    for city in cities:
        URL = f'{DOMAIN}/{city}'
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.implicitly_wait(2)
        catagories_links = [link.get_attribute('href') for link in driver.find_elements(By.CSS_SELECTOR, '.thin-scrollbar.clearfix a')]
        for j, link in enumerate(catagories_links):
            driver.get(link)
            all_restuarant_types_link[restuarants_types[j]] = find_url_restaurants(driver)
            driver.execute_script("window.history.go(-1)")
        driver.quit()
    return all_restuarant_types_link



if __name__ == '__main__':
    cities = ['tehran', 'qom', 'bandarAbbas', 'karaj', 'rasht',
    'gorgan', 'hamedan', 'yazd', 'urmia', 'gonbad', 'arak']
    link_city(cities)


