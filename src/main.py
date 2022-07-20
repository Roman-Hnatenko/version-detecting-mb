from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.maxbet.ro/ro/cazino-online/egtgames'


def load_all_content(driver: WebDriver):
    waiter = WebDriverWait(driver, 5)
    try:
        waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > .btn.btn-red-restyle'))).click()  # Accept notification
    except TimeoutException:
        pass
    while True:
        try:
            waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.item-img-arrow-down'))).click()
        except TimeoutException:
            break
        except Exception:
            pass


def handle_game(driver: WebDriver):
    waiter = WebDriverWait(driver, 8)
    game = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.game')))
    ActionChains(driver).move_to_element(game).perform()  # place the cursor
    driver.implicitly_wait(5)
    driver.execute_script("document.getElementsByClassName('ui-bottom-inner')[0].click()")  # TO DO


def main(driver: WebDriver):
    load_all_content(driver)
    handle_game(driver)


if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    driver.implicitly_wait(5)
    main(driver)
