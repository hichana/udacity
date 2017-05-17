import xml.etree.ElementTree as ET

OSM_FILE = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"

def count_elem(osm_file, tags=('node', 'way', 'relation')):
    tag_set = set() 
    
    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            for tag_elem in elem.iter("tag"):
                if tag_elem.attrib['k'] == 'NHD:ComID':
                    for tag_elem in elem.iter("tag"):
                        tag_set.add(tag_elem.attrib['k'])
        root.clear()
    return tag_set

keys_list = list(count_elem(OSM_FILE))

if __name__ == '__main__':
    for i in sorted(keys_list):
        print(i)
