from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
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


class HobbiesConnectTests(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.frontend_url = f'{self.live_server_url}/static/'

        # Delete all users
        User.objects.filter(email='newuser@email.com').delete()
        User.objects.filter(email='otheruser@email.com').delete()

        # Test user object
        self.test_user_email = 'newuser@email.com'
        self.test_user_password = 'newHelloWorld123'
        self.test_user_first_name = 'New'
        self.test_user_last_name = 'User'
        self.test_user_dob = '1999-01-01'

        # self.test_user = User.objects.create_user(
        #     email=self.test_user_email,
        #     password=self.test_user_password,
        #     first_name=self.test_user_first_name,
        #     last_name=self.test_user_last_name,
        #     dob=self.test_user_dob,
        # )
        # print(f"Test User ID: {self.test_user.id}")

        # Test other user object
        self.other_user = User.objects.create_user(
            email='otheruser@email.com',
            password='otherUser123',
            first_name='Other',
            last_name='User',
            dob='1999-01-02',
        )
        super().setUp()

    def tearDown(self) -> None:
        # self.test_user.delete()
        User.objects.filter(email='newuser@email.com').delete()
        User.objects.filter(email='otheruser@email.com').delete()
        self.driver.quit()
        super().tearDown()

    def signup(self) -> None:
        '''
        Helper function to sign up
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
            email_input.send_keys(self.test_user_email)
            first_name_input.send_keys(self.test_user_first_name)
            last_name_input.send_keys(self.test_user_last_name)
            dob_input.send_keys('01-01-1999')
            password_input.send_keys(self.test_user_password)
            password_confirmation_input.send_keys(self.test_user_password)

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

    def login(self, email, password) -> None:
        try:
            driver = self.driver
            driver.get(f'{self.live_server_url}/login/')

            # Find the username and password input elements
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = driver.find_element(By.NAME, 'password')

            # Enter the username and password
            username_input.send_keys(email)
            password_input.send_keys(password)

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
    
    '''
    Edit user profile tests
    - Update first name
    - Update last name
    - Update email
    - Update date of birth
    - Update password
    '''

    def update_password(self) -> None:
        '''
        Helper function to update the password
        '''
        try:
            # Find the current password, new password, and confirm new password input elements
            current_password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'current_password'))
            )
            new_password_input = self.driver.find_element(By.ID, 'new_password')
            # Enter the current password, new password, and confirm new password
            current_password_input.send_keys(self.test_user_password)
            new_password_input.send_keys('updatedPassword123')

            # Submit the form
            self.driver.find_element(By.XPATH, '//button[text()="Update Password"]').click()
            # Wait for the profile page to load
            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.ID, 'profile-page'))
            )
            time.sleep(3)

            # Log out
            self.driver.find_element(By.XPATH, '//button[text()="Logout"]').click()
            time.sleep(1)

            # Log in with the new password
            self.test_user_password = 'updatedPassword123'
            self.login(self.test_user_email, self.test_user_password)   

        except Exception as e:
            print(f'Error: {e}')
            raise

    '''
    Find Friends with filtering
    - ENsure a list of users is displayed
    - Apply filter by age
    - Verify the filtered results
    '''
    def filter_users_by_age(self) -> None:
        try:
            # Find the users page
            self.driver.get(f'{self.live_server_url}/findfriends/')
            # Find the filter button
            # filter_button = WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located((By.ID, 'filter-button'))
            # )
            # filter_button.click()
            # time.sleep(1)

            # # Find the age filter input
            # age_filter_input = WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located((By.ID, 'age-filter'))
            # )
            # age_filter_input.send_keys('22')
            # time.sleep(1)

            # # Click the filter button
            # filter_button.click()
            # time.sleep(2)

            # # Verify the filtered results
            # users = self.driver.find_elements(By.CLASS_NAME, 'user
        except Exception as e:
            print(f'Error: {e}')
            raise
    '''
    Send friend request
    - Search for another user
    - Send request
    - Verify request sent
    '''

    '''
    Accept friend request
    - Log in with another user
    - Go to friend request section
    - Accept the request
    - Verify the user is now a friend
    '''
    def accept_friend_request(self) -> None:
        '''
        Helper function to accept friend request
        '''
        try:
            # Log in with the other user
            self.login(self.other_user.email, 'otherUser123')
        except Exception as e:
            print(f'Error: {e}')
            raise


    def test_new_user(self) -> None:
        '''
        Test the following user actions:
        1) User sign up
        2) User login
        3) Update user details
        4) Users page with testing of filtering by age
        5) Sending a friend request
        6) Login as the other user and accept the friend requests sent
        '''
        # self.signup()
        # self.login(self.test_user_email, self.test_user_password)
        # self.update_password()
        # self.filter_users_by_age()
        self.accept_friend_request()

if __name__ == "__main__":
    unittest.main()