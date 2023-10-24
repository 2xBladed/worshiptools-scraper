import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

'''
def rept_decorator(func):
    def wrapper(self, *args, **kwargs):
        results = []
        for i in range(3):
            print(f'vai executar a função: {func.__name__}')
            result = func(self, *args, **kwargs)
            results.append(result)
            print('executou a função.')
        return results
    return wrapper
'''
    
def rept_decorator(func):
    def wrapper(self, *args, **kwargs):
        for i in range(3):
            try:
                print(f'vai executar a função: {func.__name__}')
                result = func(self, *args, **kwargs)
                print('executou a função.')
                return result
            except:
                print('chegou')
                if i == 2:
                    return 'sem condicao'
                continue
    return wrapper

class SeleniumWebDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()        

    def my_get(self):
        self.driver.get('https://www.google.com')
        print('chegou na página')
        return

    @rept_decorator
    def get_current_url(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script("return window.performance.timing.loadEventEnd > 0"))
        url = self.driver.execute_script("return window.location.href")
        url = None
        if url is None:
            raise ValueError()
        return url

swd = SeleniumWebDriver()
swd.my_get()
time.sleep(1)
result = swd.get_current_url()

# Printar o resultado 'url' três vezes
print(result)
