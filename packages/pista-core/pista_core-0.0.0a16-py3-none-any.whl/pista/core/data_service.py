from datetime import datetime, timedelta

from pista.core.common_service import Commons
from pista.core.excel_service import ExcelUtil
from pista.core.file_service import FileUtil


class DataGeneric:
    """ Provides func to replace all pre-defined placeholders at run time
    eg: #ABC# means developer has to replace during coding (user defined - manual)
        {ABC} means system has to replace with dynamic data during run (system dynamic - automatic)
        #{ABC} means system has to replace with user defined data (variable file) """

    '''System variables, eg: {MMDDYYYY_S-1}'''
    DATE_PLACEHOLDERS = {'MMDDYYYY_S': '%m/%d/%Y'}

    # MMDDYYYY_S means '02/21/2022'

    @classmethod
    def replace_dyn(cls, data: str) -> str:
        """Provided data will be returned with all dynamic data replaced at run time
           Placeholder eg: {MMDDYYYY_S+0} """
        today = datetime.today()
        for key in cls.DATE_PLACEHOLDERS.keys():  # 'MMDDYYYY_S'
            initial_var = '{' + key  # '{MMDDYYYY_S'
            while data.count(initial_var) > 0:
                start_index = data.index(initial_var)  # 100
                end_index = data.index('}', start_index)  # 113
                actual_var = data[start_index:end_index + 1]  # '{MMDDYYYY_S-1}'
                opertr_with_val = actual_var.replace(key, '').replace('{', '').replace('}', '')  # '-1'
                only_val = opertr_with_val[1:]  # '1'

                if opertr_with_val.startswith('+'):
                    finaldate_unformtd = today + timedelta(days=float(only_val))
                else:
                    finaldate_unformtd = today + timedelta(days=-float(only_val))  # today-1

                # finaldate_formtd = final_dt_unformtd.strftime(cls.DATE_DICT[key])  # today-1 as formatted
                finaldate_formtd = Commons.format_date(finaldate_unformtd, cls.DATE_PLACEHOLDERS[key])
                data = data.replace(actual_var, str(finaldate_formtd))  # data with current placeholer replaced
        # TODO code for other placeholders
        return data

    @classmethod
    def get_vardata(cls, exlfilepath: str, sheet: str, column: str) -> dict:
        """Excel file has rows & cols
        rows: attributes (1st row is row header)
        cols: dataset (1st col is col header)
        """
        vardata = ExcelUtil.read_excel_col_data(filepath=exlfilepath, sheet=sheet, col_header=column)
        return vardata

    @classmethod
    def _replace_data_with_varfile(cls, data: str, exlfilepath: str, sheet: str, column: str) -> (str, dict):
        """Provided data will be returned with all user variables replaced at run time
           Placeholder eg: #{ITEM_HEIGHT} """
        varfiledict = DataGeneric.get_vardata(exlfilepath, sheet, column)
        for k, v in varfiledict.items():
            actual_var = '#{' + str(k) + '}'
            while data.count(actual_var) > 0:
                data = data.replace(actual_var, str(v))
        return data, varfiledict

    @classmethod
    def _replace_file_with_varfile(cls, filepath: str, exlfilepath: str, sheet: str, column: str) -> (str, dict):
        filedata = FileUtil.read_from_file(filepath)
        filedata, varfiledict = cls._replace_data_with_varfile(filedata, exlfilepath, sheet, column)
        FileUtil.write_to_file(filepath, filedata)
        return filedata, varfiledict

    @classmethod
    def replace_from_varfile(cls, exlfilepath: str, sheet: str, column: str, data: str = None, filepath: str = None) \
            -> (str, dict):
        """Replaces: data/filepath data (str) with exlfilepath data (excel).
            Returns: Replaced data (str), Var file data (dict)"""
        if data is not None:
            return cls._replace_data_with_varfile(data, exlfilepath, sheet, column)
        elif filepath is not None:
            return cls._replace_file_with_varfile(filepath, exlfilepath, sheet, column)

# data = """<ExternalSystemPurchaseOrderNbr>{MMDDYYYY_S-1} 00:01</ExternalSystemPurchaseOrderNbr>
#             <OriginFacilityAliasId>{MMDDYYYY_S+1} 123</OriginFacilityAliasId>
#             <OriginFacilityAliasId>#MMDDYYYY_S+1# 123</OriginFacilityAliasId>
#             <PickupStartDttm>{MMDDYYYY_S+0} 00:01</PickupStartDttm>
#             <PickupEndDttm>02/22/2022 00:01</PickupEndDttm>
#             <DestinationFacilityName>{MMDDYYYY_S+1} ABC</DestinationFacilityName>
#             <DestinationFacilityName>#{QTY_UOM} ABC</DestinationFacilityName>"""
#
# filepath = 'D:/Practice/AutomationService/resources/data/data_variable.xlsx'
# dataout = DataGeneric.replace_var(data, filepath, 'DO', 'DATA2')
# # print(dataout)
#
# dataout = DataGeneric.replace_dyn(dataout)
# print(dataout)
#
# filepath = 'D:/4_GPC/AutomationPrep/MASTER/AutomationService/resources/data/data_variable.xlsx'
# vardata = DataGeneric.get_var(filepath, 'DO', 'DATA1')
# print(vardata)
# print(vardata['QTY_UOM'])
# print(vardata['BU_UNIT'])
