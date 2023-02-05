from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def links_in_page(url):
    options = Options()
    options.add_argument('--headless')

    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(6)
    result_number = int(driver.find_element(By.CSS_SELECTOR, '.result-container header>small').text.split()[0])
    print(f'Expected number of restaurants: {result_number}')
    print('Scrapping...')

    wait = WebDriverWait(driver, 5)
    try:
        while True:
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.load-more-holder button')))
            driver.execute_script("arguments[0].click();", button)
    except TimeoutException:
        pass

    restaurants = driver.find_element(By.CLASS_NAME, 'rest-list.clearfix').find_elements(By.CLASS_NAME ,'r-i')
    links = [restaurant.get_attribute('href') for restaurant in restaurants]
    print(f'Scrapping finished.')
    print(f'Number of links: {len(links)}')
    return links