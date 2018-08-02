import time

from pages.locators import MainNavLocators, CoursesPageLocators, HomePageLocators
from common.waits import DriverWaits


class MainNavigation(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def go_to_all_courses_page(self):
        self.driver.find_element(*MainNavLocators.ALL_COURSES_LINK).click()
        self.driver_waits.wait_till_element_is_visible(CoursesPageLocators.COURSE_DIRECTORY)

        time.sleep(5)

    def go_to_home(self):
        self.driver.find_element(*MainNavLocators.BRAND_LOGO).click()
        self.driver_waits.wait_till_element_is_visible(HomePageLocators.COURSE_LIST_BLOCK)

    def logout(self):
        self.driver.find_element(*MainNavLocators.MY_PROFILE_ICON).click()

        self.driver_waits.wait_till_element_is_clickable(MainNavLocators.LOGOUT_LINK)
        time.sleep(1)
        self.driver.find_element(*MainNavLocators.LOGOUT_LINK).click()

        self.driver_waits.wait_till_element_is_visible(MainNavLocators.LOGIN_LINK)
