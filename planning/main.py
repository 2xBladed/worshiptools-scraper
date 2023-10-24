import scraping_functions


swd = scraping_functions.SeleniumWebDriver()
swd.my_get()
print(swd.get_current_url())
