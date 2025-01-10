from django.test import LiveServerTestCase
from selenium import webdriver

class HostTest(LiveServerTestCase):
    def testProfile(self):
        driver= webdriver.Chrome()
        driver.get("http://localhost:5173/")
        assert "ECS639 Web Programming - Group CW Template" in driver.title