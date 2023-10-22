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

