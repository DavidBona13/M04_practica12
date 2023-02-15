import xml.etree.ElementTree as ET

#genera un archivo XML con valores fijos
def genXml():

    #root
    root     = ET.Element("students")

    #childs1, 2, 3 ...
    child1   = ET.SubElement(root  , "student")
    child1.set("Country", "Spain")

    name1    = ET.SubElement(child1, "name")
    name1.text = "Roc"

    surname1 = ET.SubElement(child1, "surname")
    surname1.text = "Bigas"

    email1   = ET.SubElement(child1, "email")
    email1.text = "rbigas@gmail.net"

    dni1     = ET.SubElement(child1, "dni")
    dni1.text = "494586675P"


    child2   = ET.SubElement(root  , "student")
    child2.set("Country", "Australia")

    name2    = ET.SubElement(child2, "name")
    name2.text = "Jhameo"

    surname2 = ET.SubElement(child2, "surname")
    surname2.text = "Garcia"

    email2   = ET.SubElement(child2, "email")
    email2.text = "jfunes@gmail.net"

    dni2     = ET.SubElement(child2, "dni")
    dni2.text = "987123465E"


    child3   = ET.SubElement(root  , "student")
    child3.set("Country", "U.S")

    name3    = ET.SubElement(child3, "name")
    name3.text = "david"

    surname3 = ET.SubElement(child3, "surname")
    surname3.text = "bona"

    email3   = ET.SubElement(child3, "email")
    email3.text = "dbona@gmail.es"

    dni3     = ET.SubElement(child3, "dni")
    dni3.text = "876234567Y"


    child4   = ET.SubElement(root  , "student")
    child4.set("Country", "Kazajistan")

    name4    = ET.SubElement(child4, "name")
    name4.text = "roger"

    surname4 = ET.SubElement(child4, "surname")
    surname4.text = "blanes"

    email4   = ET.SubElement(child4, "email")
    email4.text = "peepn@yahoo.net"

    dni4     = ET.SubElement(child4, "dni")
    dni4.text = "982347435R"


    child5   = ET.SubElement(root  , "student")
    child5.set("Country", "Polonia")

    name5    = ET.SubElement(child5, "name")
    name5.text = "papa"

    surname5 = ET.SubElement(child5, "surname")
    surname5.text = "seco"

    email5   = ET.SubElement(child5, "email")
    email5.text = "jaumebalmes@hehe.na"

    dni5     = ET.SubElement(child5, "dni")
    dni5.text = "78433221F"

    ET.indent(root)
    dump = ET.dump(root)

    tree = ET.ElementTree(root)
    tree.write("students.xml")

    return dump