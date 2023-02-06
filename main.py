from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import extract_data



if __name__ == '__main__':
    with open("links.txt","r") as file:
        links = eval(file.read())
    extract_data(links)
