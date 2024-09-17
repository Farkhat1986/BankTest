import time

from selenium import webdriver



driwer = webdriver.Chrome()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument('--headless=new')
    #options.add_argument('--start-maximized')
    #driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
driwer.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")
time.sleep(5)
driwer.quit()
