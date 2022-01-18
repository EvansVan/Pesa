from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def scraper():
    try:
        unique = {}
        url = 'https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer?ft_source=LinkedIn_1000080706&ft_medium=Job%20Boards_1000074720'
        #using chrome to access web
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        #options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        driver.implicitly_wait(20)
        #store  scraped text
        info = driver.find_element_by_xpath("/html/body").text.replace(',', '').replace('.', '')

        #convert  text data into list with 
        words = info.split()
        
        #use words as dictionary key to filter and remove  repeat values
        unique = list(dict.fromkeys(words))
        print(len(unique))
        
        return unique
    except NoSuchElementException as e:
        print(e)


scraper()
