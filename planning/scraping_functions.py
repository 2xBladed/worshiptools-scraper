# Numpy documentation style 
# TODO Generate documentation using Sphinx
# TODO 
# TODO direitos_louvor(): Fazer uma verificação pelo número de divs no elemento em vez verificar se Tonalidade faz parte do texto do elemento.
# TODO tentar em vez de percorrer cada elemento na pág. principal, tentar pegar todos ao mesmo tempo 
# 
# 
# 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

import time
import os
from dotenv import load_dotenv

load_dotenv()

env_id = os.environ['ID']
env_email = os.environ['EMAIL']
env_password = os.environ['PASSWORD']

# TODO add an optional argument debug (self, debug) that when true make use of print() to debug.
class SeleniumWebDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()

    
    def retry_decorator(max_retries=3):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                for tentativa in range(max_retries):
                    try:
                        return func(self, *args, **kwargs)
                    except TimeoutException:
                        if tentativa == max_retries - 1:
                            raise TimeoutError('A internet parece estar lenta, tente novamente mais tarde.')
                        self.driver.back()
                        time.sleep(0.5)
                        self.driver.forward()
                return wrapper
            return decorator

    #@retry_decorator
    def get_current_url(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.execute_script("return window.performance.timing.loadEventEnd > 0"))
        url = self.driver.current_url
        if url is None:
            raise ValueError('A URL não pode ser None.')
        return url



    def my_get(self):
        self.driver.get('http://www.youtube.com')
        print('chegou em google')
        return






if __name__ == '__main__':
    swd = SeleniumWebDriver()
    swd.my_get()
    print(swd.get_current_url())