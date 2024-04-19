import xmltodict
import json
import os

class XML_JSON_XML:
    """
    Classe pour la conversion entre les formats XML et JSON.
    """

    def detect_file_type(self, file_path):
        """
        Détermine le type de fichier en fonction de son extension.

        Args:
            file_path (str): Chemin du fichier.

        Returns:
            str: Type de fichier ('xml', 'json') ou None si le type n'est pas pris en charge.
        """
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.xml':
            return 'xml'
        elif file_extension == '.json':
            return 'json'
        else:
            return None

    def convert_xml_to_json(self, xml_content):
        """
        Convertit le contenu XML en JSON.

        Args:
            xml_content (str): Contenu XML sous forme de chaîne de caractères.

        Returns:
            str: Contenu JSON résultant.
        """
        data_dict = xmltodict.parse(xml_content)
        json_data = json.dumps(data_dict, indent=4)
        return json_data

    def convert_json_to_xml(self, json_content):
        """
        Convertit le contenu JSON en XML.

        Args:
            json_content (str): Contenu JSON sous forme de chaîne de caractères.

        Returns:
            str: Contenu XML résultant.
        """
        # Remplacer "None" par "null" dans le contenu JSON
        json_content = json_content.replace("None", "null")

        # Analyse du contenu JSON
        data_list = json.loads(json_content)

        # Créer une chaîne XML pour chaque élément racine
        xml_data_list = []
        for item in data_list:
            xml_data_list.append(xmltodict.unparse({"root": item}, pretty=True))

        # Joindre les chaînes XML
        xml_data = "\n".join(xml_data_list)
        return xml_data

    def convert_file(self, file_path):
        """
        Convertit un fichier du format source (XML ou JSON) au format cible (JSON ou XML).

        Args:
            file_path (str): Chemin du fichier source.

        Raises:
            ValueError: Si le type de fichier n'est pas pris en charge.
        """
        file_type = self.detect_file_type(file_path)
        if file_type == 'xml':
            with open(file_path, 'r') as xml_file:
                xml_content = xml_file.read()
                json_data = self.convert_xml_to_json(xml_content)
                with open('Output.json', 'w') as json_file:
                    json_file.write(json_data)
            print("Conversion XML vers JSON réussie.")
            print(json_data)
        elif file_type == 'json':
            with open(file_path, 'r') as json_file:
                json_content = json_file.read()
                xml_data = self.convert_json_to_xml(json_content)
                with open('Output.xml', 'w') as xml_file:
                    xml_file.write(xml_data)
            print("Conversion JSON vers XML réussie.")
            print(xml_data)
        else:
            raise ValueError("Type de fichier non pris en charge.")

# Exemple d'utilisation de la classe
xml_json_xml_instance = XML_JSON_XML()
xml_json_xml_instance.convert_file(r'C:\Repos_Arion\ArionLibrary\processors\Convert_xml_json_xml\tests\Input_File_test\CERT.xml')
