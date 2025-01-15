from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from django.core.management import call_command
import unittest
import time
from selenium.common.exceptions import TimeoutException

User = get_user_model()


class HobbiesConnectTests(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.live_server_url = 'http://localhost:5173'
        self.live_server_url = 'http://localhost:8000'
        # Test user object
        self.test_user = User.objects.create_user(
            email='newuser@email.com',
            password='newUser123',
            first_name='New',
            last_name='User',
            dob='1999-01-01'
        )

    def tearDown(self):
        self.test_user.delete()
        User.objects.filter(email='newuser@email.com').delete()
        self.driver.quit()
        super().tearDown()

    def signup(self):
        '''
        Test the signup
        '''
        try:
            driver = self.driver
            driver.get(f'{self.live_server_url}/signup/')

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'first_name'))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'last_name'))
            )
            dob_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'dob'))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password1'))
            )
            password_confirmation_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password2'))
            )

            # Enter the user details
            email_input.send_keys(self.test_user.email)
            first_name_input.send_keys(self.test_user.first_name)
            last_name_input.send_keys(self.test_user.last_name)
            dob_input.send_keys('01-01-1999')
            password_input.send_keys('newPassword123')
            password_confirmation_input.send_keys('newPassword123')

            # Submit the form
            password_input.send_keys(Keys.RETURN)

            # Wait for the profile page to load
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, 'profile-page'))
            )
            time.sleep(2)

            # Log out
            driver.find_element(By.XPATH, '//button[text()="Logout"]').click()
            time.sleep(1)

        except Exception as e:
            print(f'Error: {e}')
            raise

    def login(self):
        try:
            driver = self.driver
            driver.get(f'{self.live_server_url}/login/')

            # Find the username and password input elements
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = driver.find_element(By.NAME, 'password')

            # Enter the username and password
            username_input.send_keys(self.test_user.email)
            password_input.send_keys('newPassword123')

            # Click the login button
            login_button = driver.find_element(By.ID, 'login-button')
            login_button.click()
            time.sleep(2)

            # Wait for the profile page to load
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, 'profile-page'))
            )
            time.sleep(1)

        except Exception as e:
            print(f'Error: {e}')
            raise

    def test_new_user(self):
        '''
        Test the signup and login functionality
        '''
        self.signup()
        self.login()

if __name__ == "__main__":
    unittest.main()