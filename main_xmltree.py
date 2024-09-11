import xml.etree.ElementTree as ET

# Load the xml file
tree = ET.parse('xml_files/stocks.xml')

# Get the root tree tag
root = tree.getroot()

# print(root.tag)
# print(len(root))

# List every tag and value
for child in root:
    print("------")
    for g_child in child:
        print(f"{g_child.tag}: {g_child.text}")


