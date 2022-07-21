from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class ScriptLinkExtractorBase:
    def __init__(self, driver: WebDriver | None = None, page_url: str | None = None) -> None:
        self.driver = driver or webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.waiter = WebDriverWait(self.driver, 5)
        if page_url:
            self._open_page(page_url)

    def _open_page(self, page_url: str) -> None:
        self.driver.get(page_url)
        # Accept the notification
        try:
            self.waiter.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > .btn.btn-red-restyle'))
            ).click()
        except TimeoutException:
            """The notification did not appear"""

    def _wait_and_find_element(self, by: str, value: str):
        return self.waiter.until(EC.presence_of_element_located((by, value)))

    def switch_to_general_iframe(self) -> None:
        outer_frame = self._wait_and_find_element(By.CSS_SELECTOR, '.ui-one-games-container > iframe')
        self.driver.switch_to.frame(outer_frame)
        self.driver.switch_to.frame(self._wait_and_find_element(By.ID, 'ifmGame'))

    def switch_to_provider_iframe(self) -> None:
        """Switch to inner provider iframe"""

    def get_value(self, *, attr_value: str, attr_name: str = 'src*',) -> str:
        main_window = self.driver.current_window_handle
        self.switch_to_general_iframe()
        self.switch_to_provider_iframe()
        script = self.waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'script[{attr_name}="{attr_value}"]')))
        src_link = script.get_attribute('src')
        self.driver.switch_to.window(main_window)
        return src_link
