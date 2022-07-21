import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

GAME_URL = 'https://www.maxbet.ro/ro/jocuri-pacanele-online/vampire-night-egt'


def get_build_timestamp(driver: WebDriver) -> str:
    waiter = WebDriverWait(driver, 5)
    main_window = driver.current_window_handle

    outer_frame = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-one-games-container > iframe')))
    driver.switch_to.frame(outer_frame)
    driver.switch_to.frame(driver.find_element(By.ID, 'ifmGame'))

    inner_frame = driver.find_element(By.CSS_SELECTOR, 'iframe')
    src_link = inner_frame.get_attribute('src')
    match = re.search(r'buildTimestamp=(\d+)', src_link)
    print(match)
    driver.switch_to.window(main_window)
    return match[1]


if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(GAME_URL)
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > .btn.btn-red-restyle'))).click()  # Accept notification
    except TimeoutException:
        pass
    driver.implicitly_wait(5)
    get_build_timestamp(driver)


