import pytest
from ..lib.Convert_Soap_Rest import XML_JSON_XML

# Fixtures
@pytest.fixture
def converter():
    """
    Fixture to initialize an instance of XML_JSON_XML for testing.
    """
    return XML_JSON_XML()

# Path to the XML test file
file_path = (r'C:\Repos_Arion\ArionLibrary\processors\Convert_xml_json_xml\tests\Input_File_test\CERT.xml')

def test_detect_file_type_json(converter):
    """
    Test to verify if the detect_file_type method correctly detects JSON file type.

    Args:
        converter: Instance of XML_JSON_XML.
    """
    assert converter.detect_file_type(file_path) == 'json'


def test_convert_file_json(converter):
    """
    Test to verify if the convert_file method correctly converts a JSON file to XML.

    Args:
        converter: Instance of XML_JSON_XML.
    """
    # Convert the JSON file to XML using the convert_file method
    converter.convert_file(file_path)

# Tests
def test_detect_file_type_xml(converter):
    """
    Test to verify if the detect_file_type method correctly detects XML file type.

    Args:
        converter: Instance of XML_JSON_XML.
    """
    assert converter.detect_file_type(file_path) == 'xml'


def test_convert_file_xml(converter):
    """
    Test to verify if the convert_file method correctly converts an XML file to JSON.

    Args:
        converter: Instance of XML_JSON_XML.
    """
    # Convert the XML file to JSON using the convert_file method
    converter.convert_file(file_path)
