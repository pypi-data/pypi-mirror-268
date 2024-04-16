from pista.tests import *


@class_marker
@m.usefixtures("invoke_web_driver")
class Test_Pista_UI_WebBrowser(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista_UI_WebBrowser")
    def test_Pista_UI_WebBrowser(self):
        """Test pista with web browser"""
        printit('Web driver', self.driver)
