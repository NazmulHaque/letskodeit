import time

from selenium.webdriver.common.keys import Keys

from pages.locators import MainNavLocators
from pages.locators import CoursesPageLocators, CourseDetailsPageLocators
from common.waits import DriverWaits


class CoursesPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def get_courses(self):
        courses = {
            'no_of_courses': 0,
            'courses': [],
        }
        course_elements = self.driver.find_elements(*CoursesPageLocators.COURSE_BLOCK)
        courses['no_of_courses'] = len(course_elements)

        for course_element in course_elements:
            course_title = course_element.find_element(*CoursesPageLocators.COURSE_TITLE).text
            course_price = course_element.find_element(*CoursesPageLocators.COURSE_PRICE).text
            course_id = course_element.get_attribute('data-course-id')

            course_details = {
                'title': course_title,
                'price': course_price,
                'course_id': course_id,
            }

            courses['courses'].append(course_details)

        return courses

    def search_course_by_keyword(self, query_string=''):
        search_box = self.driver.find_element(*CoursesPageLocators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(query_string)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

    def search_and_get_courses_by_keyword(self, query_string=''):
        self.search_course_by_keyword(query_string=query_string)
        return self.get_courses()

    def go_to_course_details_page(self, course_id):
        course_elements = self.driver.find_elements(*CoursesPageLocators.COURSE_BLOCK)

        course_found = False
        for element in course_elements:
            if element.get_attribute('data-course-id') == str(course_id):
                course_found = True
                element.click()
                self.driver_waits.wait_till_element_is_visible(CourseDetailsPageLocators.MAIN_BLOCK)
                break

        assert course_found, 'No course found by id: {}'.format(str(course_id))
        # if not course_found:
        #     raise AssertionError('No course found by id: {}'.format(str(course_id)))
