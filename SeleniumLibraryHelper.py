import allure
from robot.libraries.BuiltIn import BuiltIn

class SeleniumLibraryHelper(object):
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, name, attrs):
         BuiltIn().set_library_search_order('SeleniumLibraryHelper')

    def capture_page_screenshot(self):
        ul = BuiltIn().get_library_instance('SeleniumLibrary')
        path = ul.capture_page_screenshot()
        allure.attach.file(path, name="Screenshot | " + (BuiltIn().get_variable_value("${TEST NAME}")), attachment_type=allure.attachment_type.JPG)
        return path