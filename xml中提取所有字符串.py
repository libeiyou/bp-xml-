import xml.etree.ElementTree as ET
import re

def extract_strings_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    extracted_strings = set()

    regex = r'\b\w+\b'
    for element in root.iter():
        if element.text:
            matches = re.findall(regex, element.text)
            extracted_strings.update(matches)

    return extracted_strings

def main():
    xml_file = input("Enter the path to the XML file exported from Burp Suite: ")
    extracted_strings = extract_strings_from_xml(xml_file)

    # Save the extracted strings to a file
    output_file = "output.txt"
    with open(output_file, "w") as file:
        for string in extracted_strings:
            file.write(string + '\n')

    print(f"The extracted strings have been saved to the file {output_file}.")

if __name__ == "__main__":
    main()
