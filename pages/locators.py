from selenium.webdriver.common.by import By


class HomePageLocators(object):

    MAIN_BLOCK = (By.CLASS_NAME, 'view-school')
    COURSE_LIST_BLOCK = (By.CLASS_NAME, 'course-list')


class MainNavLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/sign_in"]')
    MY_PROFILE_ICON = (By.CLASS_NAME, 'open-my-profile-dropdown')
    ALL_COURSES_LINK = (By.CSS_SELECTOR, 'a[href="/courses"]')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="/sign_out"]')
    BRAND_LOGO = (By.CLASS_NAME, 'header-logo')


class LoginPageLocators(object):

    LOGIN_BUTTON = (By.CLASS_NAME, 'login-button')
    EMAIL_INPUT = (By.ID, 'user_email')
    PASSWORD_INPUT = (By.ID, 'user_password')


class CoursesPageLocators(object):
    COURSE_DIRECTORY = (By.CLASS_NAME, 'course-directory')
    COURSE_BLOCK = (By.CLASS_NAME, 'course-listing')
    COURSE_TITLE = (By.CLASS_NAME, 'course-listing-title')
    COURSE_PRICE = (By.CLASS_NAME, 'course-price')
    SEARCH_BOX = (By.ID, 'search-courses')


class CourseDetailsPageLocators(object):
    MAIN_BLOCK = (By.CLASS_NAME, 'blocks-page-course_sales_page')
    ENROLL_BUTTON_TOP = (By.ID, 'enroll-button-top')


class CheckoutPageLocators(object):
    MAIN_BLOCK = (By.CLASS_NAME, 'spc')
    COURSE_TITLE = (By.XPATH,'(//*[@ class="spc__summary-item spc--text-light"])[1]')
    COURSE_PRICE = (By.XPATH, '(//*[@ class="spc__summary-item text-right mono"])[1]')
    USER_EMAIL = (By.XPATH, '//span[@data-checkout-authentication-email]')
    PAYMENT_OPTION_TABS = (By.XPATH, '//*[@data-checkout-tabs-tab]')
    CREDIT_CARD_TAB = (By.XPATH, '//*[@data-checkout-tabs-tab="credit_card"]')
    CREDIT_CARD_LABEL = (By.XPATH, '//*[@data-checkout-tabs-tab="credit_card"]//*[@class="spc__tabs-label"]')
    PAYPAL_TAB = (By.XPATH, '//*[@data-checkout-tabs-tab="paypal"]')
    PAYPAL_LABEL = (By.XPATH, '//*[@data-checkout-tabs-tab="paypal"]//*[@class="spc__tabs-label"]')


