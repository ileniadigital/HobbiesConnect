from datetime import date
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from api.models import *
import time

User= get_user_model()

class HostTest(StaticLiveServerTestCase):
    def setUp(self):
        # Set up the test user
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            email='test@user.email',
            password='testPassword123',
            dob=date(1990, 1, 1),
        )
        self.user.save()
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        '''
        Test user log in
        '''
        driver = self.driver
        driver.get(self.live_server_url + '/login/')
        # Find the username and password input elements
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        # Enter the username and password
        username_input.send_keys('test@user.email')
        password_input.send_keys('testPassword123')

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Check that the user is redirected to the profile page
        time.sleep(3)
        self.assertIn("Profile", driver.page_source)