import unittest

import settings
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.courses import CoursesPage
from pages.main_nav import MainNavigation
from pages.course_details import CourseDetailsPage
from pages.checkout import CheckoutPage


class UIAutomationBase(unittest.TestCase):

    login_required = False
    credentials = settings.LOGIN_CREDENTIALS

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.courses_page = CoursesPage(cls.driver)
        cls.main_navigation = MainNavigation(cls.driver)
        cls.course_details_page = CourseDetailsPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)

        cls.home_page.load_home_page()

        if cls.login_required:
            cls.login_page.login(credentials=cls.credentials)

    @classmethod
    def tearDownClass(cls):

        if cls.login_required:
            cls.main_navigation.logout()

        cls.driver.quit()
