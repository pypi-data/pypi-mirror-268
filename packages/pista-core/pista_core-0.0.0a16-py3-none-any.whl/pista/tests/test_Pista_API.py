from pista.core.api_service import APIService
from pista.tests import *


@class_marker
class Test_Pista_API(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista_API")
    def test_Pista_API(self):
        """Test pista with API code"""
        printit('API')

        baseUrl = ENV_CONFIG.get('api', 'module1_base_url')
        appUrl = ENV_CONFIG.get('api', 'module1_get_userById')

        response = APIService.call_get_api(baseUrl + appUrl)
        jsonDict = response.json()

        APIService.assert_statuscode(response, 200)
