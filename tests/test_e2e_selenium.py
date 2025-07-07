import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestTodoE2E(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_create_todo_from_browser(self):
        self.driver.get(f"{self.live_server_url}/todos/")
        text_box = self.driver.find_element(By.NAME, "text")
        text_box.send_keys("Leer un libro")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        assert any("Leer un libro" in r.text for r in rows)

    def test_mark_complete(self):
        self.driver.get(f"{self.live_server_url}/todos/")
        first_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        first_checkbox.click()
        time.sleep(1)
        assert first_checkbox.is_selected()
