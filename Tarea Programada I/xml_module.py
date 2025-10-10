import csv
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

def csv_to_xml(csv_path, xml_filename=None, campos=None, root_name="dataset", item_name="registro"):
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        root = ET.Element(root_name)
        
        for row in reader:
            elem = ET.SubElement(root, item_name)
            if campos:
                # Solo las columnas seleccionadas
                for campo in campos:
                    if campo in row:
                        child = ET.SubElement(elem, campo.replace(" ", "_"))
                        child.text = escape(str(row[campo]))
            else:
                # Todas las columnas
                for k, v in row.items():
                    child = ET.SubElement(elem, k.replace(" ", "_"))
                    child.text = escape(str(v))
    
    ET.indent(root)
    xml_path = xml_filename or csv_path.replace('.csv', '.xml')
    ET.ElementTree(root).write(xml_path, encoding='utf-8', xml_declaration=True)
    return xml_path