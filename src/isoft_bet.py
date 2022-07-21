from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from base import ScriptLinkExtractorBase

GAME_URL = 'https://www.maxbet.ro/ro/jocuri-pacanele-online/ghosts-and-gold-isoftbet'


class ISoftBetExtractor(ScriptLinkExtractorBase):
    def switch_to_provider_iframe(self) -> None:
        self.driver.switch_to.frame(self._wait_and_find_element(By.CSS_SELECTOR, 'iframe'))
        self.driver.switch_to.frame(self._wait_and_find_element(By.ID, 'gameiframe'))


if __name__ == '__main__':
    extractor = ISoftBetExtractor(page_url=GAME_URL)
    print(extractor.get_value(attr_value='/vendor.js'))
