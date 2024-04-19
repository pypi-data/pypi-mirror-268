import pytest
from ..lib.Convert_Soap_Rest import XML_JSON_XML

# Fixtures
@pytest.fixture
def converter():
    """
    Fixture pour initialiser une instance de XML_JSON_XML pour les tests.
    """
    return XML_JSON_XML()

# Chemin du fichier de test XML
file_path= (r'C:\Repos_Arion\ArionLibrary\processors\Convert_xml_json_xml\tests\Input_File_test\CERT.xml')

def test_detect_file_type_json(converter):
    """
    Test pour vérifier si la méthode detect_file_type détecte correctement le type de fichier JSON.
    
    Args:
        converter: Instance de XML_JSON_XML.
    """
    assert converter.detect_file_type(file_path) == 'json'
    
    
def test_convert_file_json(converter):
    """
    Test pour vérifier si la méthode convert_file convertit correctement un fichier JSON en XML.
    
    Args:
        converter: Instance de XML_JSON_XML.
    """
    # Convertir le fichier JSON en XML en utilisant la méthode convert_file
    converter.convert_file(file_path)

# Tests
def test_detect_file_type_xml(converter):
    """
    Test pour vérifier si la méthode detect_file_type détecte correctement le type de fichier XML.
    
    Args:
        converter: Instance de XML_JSON_XML.
    """
    assert converter.detect_file_type(file_path) == 'xml'

def test_convert_file_xml(converter):
    """
    Test pour vérifier si la méthode convert_file convertit correctement un fichier XML en JSON.
    
    Args:
        converter: Instance de XML_JSON_XML.
    """
    # Convertir le fichier XML en JSON en utilisant la méthode convert_file
    converter.convert_file(file_path)
