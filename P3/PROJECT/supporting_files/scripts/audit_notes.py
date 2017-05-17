import xml.etree.ElementTree as ET

OSM_FILE = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"

def find_note_tag(osm_file):
    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    
    for event, elem in context:
        if event == 'end' and (elem.tag == 'node' or elem.tag == 'way' or elem.tag == 'relation'):
            for tag_elem in elem.iter("tag"):
                if tag_elem.attrib['k'] == 'NHD:ComID':
                    for tag_elem in elem.iter("tag"):
                        if tag_elem.attrib['k'] == 'note':
                            print(ET.dump(elem))
        root.clear()

if __name__ == '__main__':
    find_note_tag(OSM_FILE)
