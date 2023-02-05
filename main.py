# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def find_url_restaurants(driver):    
    #result_number = driver.find_element(By.CSS_SELECTOR, '.result-container header>small').text.split()[0]
    #print(f'Expected number of restaurants: {result_number}')
    #print('Scrapping...')
    wait = WebDriverWait(driver, 5)
    while True:
        try:
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.load-more-holder button')))
            driver.execute_script("arguments[0].click();", button)
        except:
            break
    restaurants = driver.find_element(By.CLASS_NAME, 'rest-list.clearfix').find_elements(By.CLASS_NAME ,'r-i')
    links = [restaurant.get_attribute('href') for restaurant in restaurants]
    #print(f'Scrapping finished.')
    #print(f'Number of links: {len(links)}')
    return links



def link_city(url):
    all_restuarant_types_link = {}
    restuarants_types = ['Pizza', 'Kebab','Soup', 'Sandwich','Persian_food','Crispy','Pasta',
    'Salad','Breakfast', 'Steak']

    for j in range(1,11):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.implicitly_wait(6)
        driver.find_element(By.XPATH, f'//*[@id="mo-c"]/section/div/ul/li[{j}]').click()
        all_restuarant_types_link[restuarants_types[j-1]] = find_url_restaurants(driver)
        driver.driver.quit()
    
    return all_restuarant_types_link


cities = ['tehran', 'qom', 'bandarAbbas', 'karaj', 'rasht',
'gorgan', 'hamedan', 'yazd', 'urmia', 'gonbad', 'arak']

url = f'https://www.delino.com/'+{cities}
link_city(url)


    




    


