from datetime import date
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    # def test_login(self):
    #     '''
    #     Test user log in
    #     '''
    #     driver = self.driver
    #     driver.get(self.live_server_url + '/login/')
    #     # Find the username and password input elements
    #     username_input = driver.find_element(By.NAME, 'username')
    #     password_input = driver.find_element(By.NAME, 'password')

    #     # Enter the username and password
    #     username_input.send_keys('test@user.email')
    #     password_input.send_keys('testPassword123')

    #     # Submit the form
    #     password_input.send_keys(Keys.RETURN)

    #     # Check that the user is redirected to the profile page
    #     time.sleep(3)
    #     self.assertIn("Profile", driver.page_source)

    def test_signup(self):
        '''
        Test user sign up
        '''
        driver = self.driver
        driver.get(self.live_server_url + '/signup/')
        
        # Add explicit waits for the elements to be present
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'first_name'))
        )
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'last_name'))
        )
        dob_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'dob'))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password1'))
        )
        password__confirmation_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password2'))
        )
        # Enter the user details
        email_input.send_keys('new@user.email')
        first_name_input.send_keys('New')
        last_name_input.send_keys('User')
        dob_input.send_keys('1990-01-01')
        password_input.send_keys('newPassword123')
        password__confirmation_input.send_keys('newPassword123')

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Check that the user is redirected to the login page
        time.sleep(5)
        self.assertIn("Login", driver.page_source)