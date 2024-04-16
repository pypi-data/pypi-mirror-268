import xml.etree.ElementTree as ET


class XMLUtil:
    @staticmethod
    def format_xml(xml_str: str) -> str:
        """ To get formatted xml from an xml str """
        formatd_xml = None
        try:
            xmlobj = ET.XML(xml_str)
            ET.indent(xmlobj)
            formatd_xml = ET.tostring(xmlobj, encoding='unicode')
        except Exception as e:
            print('Exception during xml formatting: ' + str(e))
        return formatd_xml

    # TODO check if require
    @staticmethod
    def get_xml_obj(xml_str: str) -> object:
        """ To get an xml object from an xml str """
        xmlobj = ET.fromstring(xml_str)
        return xmlobj
        # xmlobj = ET.XML(xml_str)
        # ET.indent(xmlobj)
        # print(type(ET.tostring(xmlobj, encoding='unicode')))
        # return ET.tostring(xmlobj, encoding='unicode')

    # TODO not tested
    @staticmethod
    def get_xml_from_file(filepath: str) -> object:
        """ To get json object from an xml file """
        xmlobj = ET.parse(filepath)
        return xmlobj

    @staticmethod
    def get_xml_dict(xml_str: str) -> dict:
        """ To convert xml to dict type - easy to read xml """
        # xml_asdict = xmltodict.parse(xml_str) # Use xmltodict lib from requirements
        # return xml_asdict
        pass
