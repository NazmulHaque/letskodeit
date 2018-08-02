from tests.base import UIAutomationBase
from settings import course_id_price_map


class TestSearchCourse(UIAutomationBase):
    login_required = True

    def setUp(self):
        self.query_string = 'java'

        self.main_navigation.go_to_all_courses_page()

    def test_search_course(self):
        """
        Validate search courses by keyword
        :return:
        """

        courses = self.courses_page.search_and_get_courses_by_keyword(query_string=self.query_string)

        assert courses['no_of_courses'] > 0, 'No course found for selenium'

        print(str(courses))

        assert all(self.query_string in course['title'].lower() for course in courses['courses']), 'Selenium must be in the course title'

    def test_validate_course_fees(self):

        """
        Validate course fees are showing accurately for each courses
        :return:
        """

        courses_data = self.courses_page.search_and_get_courses_by_keyword(query_string=self.query_string)

        for course in courses_data['courses']:
            course_id = course['course_id']
            actual_course_price = course['price']
            expected_course_price = course_id_price_map[course_id]

            error_msg = 'Course fee should be {} instead of {} for course id: {}'.format(
                expected_course_price, actual_course_price, course_id)

            assert actual_course_price == expected_course_price, error_msg

