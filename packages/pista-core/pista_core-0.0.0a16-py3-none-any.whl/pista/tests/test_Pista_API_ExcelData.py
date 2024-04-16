from pista.core.json_service import JsonService
from pista.root import PISTA_RESOURCE_DIR
from pista.tests import *


@class_marker
class Test_Pista_API_ExcelData(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista_API_ExcelData")
    def test_Pista_API_ExcelData(self):
        """Test pista with API data from excel"""
        printit('API ExcelData')

        filepath = os.path.join(PISTA_RESOURCE_DIR, 'data', 'json_data_Cubing.xlsx')

        '''Get request json'''
        jsonDict, jsonStr = JsonService.get_json_from_excel(xlfilepath=filepath, sheet='Cubing', column='CUBING_002')

        print(jsonDict)
        print(jsonStr)

        # Call API and validate
