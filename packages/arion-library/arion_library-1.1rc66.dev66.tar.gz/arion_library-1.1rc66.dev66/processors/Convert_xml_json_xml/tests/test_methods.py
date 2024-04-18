import pytest
import os
from ..lib.Convert_Soap_Rest import XML_JSON_XML

# Fixtures
@pytest.fixture
def converter():
    return XML_JSON_XML()

file_path= (r'C:\Repos_Arion\ArionLibrary\processors\Convert_xml_json_xml\tests\Input_File_test\CERT.xml')

def test_detect_file_type_json(converter):
    assert converter.detect_file_type(file_path) == 'json'
    
    
def test_convert_file_json(converter):
    # Convertir le fichier JSON en XML en utilisant la méthode convert_file
    converter.convert_file(file_path)

# Tests
def test_detect_file_type_xml(converter):
    assert converter.detect_file_type(file_path) == 'xml'


def test_convert_file_xml(converter):

    # Convertir le fichier XML temporaire en JSON en utilisant la méthode convert_file
    converter.convert_file(file_path)
    
