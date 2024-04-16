from pista.core.excel_service import ExcelUtil
from pista.root import PISTA_RESOURCE_DIR
from pista.tests import *


@class_marker
class Test_Pista_VariableDataFile(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista_VariableDataFile")
    def test_Pista_VariableDataFile(self):
        """Test pista with variable data file"""
        printit('Variable data file')

        filepath = os.path.join(PISTA_RESOURCE_DIR, 'data', 'variable_data.xlsx')

        vardata = ExcelUtil.read_excel_col_data(filepath=filepath, sheet='Demo', col_header='DC-ABC-100')

        print(vardata)
