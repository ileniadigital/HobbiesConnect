from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

User=get_user_model()

class HobbiesConnectTests(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.frontend_url = 'http://localhost:5173'
        self.backend_url = self.live_server_url

        # Test user object
        self.test_user = User.objects.create_user(
            id=4,
            email='ec22792@qmul.ac.uk',
            password='helloworld123',
            first_name='Ilenia',
            last_name='Maietta',
            dob='2004-11-22'
        )

    def tearDown(self):
        self.driver.quit()

    def test_login_and_check_authentication(self):
        try:
            driver = self.driver
            driver.get(f'{self.backend_url}/login/')

            # Find the username and password input elements
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = driver.find_element(By.NAME, 'password')

            # Enter the username and password
            username_input.send_keys('ec22792@qmul.ac.uk')
            password_input.send_keys('helloworld123')

            # Click the login button
            login_button = driver.find_element(By.ID, 'login-button')
            login_button.click()

            # Wait for the profile page to load
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, 'profile-page'))
            )

            # Check if the user is authenticated
            driver.get(f'{self.backend_url}/api/authenticated/')
            auth_status = driver.find_element(By.TAG_NAME, 'body').text
            self.assertIn('"isAuthenticated": true', auth_status)

            # Check if the profile page contains user information
            # driver.get(f'{self.frontend_url}/')
            # WebDriverWait(driver, 20).until(
            #     EC.presence_of_element_located((By.ID, 'first_name'))
            # )
            # user_info = driver.find_element(By.ID, 'first_name').get_attribute('value')
            # self.assertIn('Ilenia', user_info)
        except Exception as e:
            print(f'Error: {e}')
            driver.save_screenshot('error_screenshot.png')
            raise

if __name__ == "__main__":
    unittest.main()