import xml.etree.ElementTree as ET
import collections as col
import pprint

OSM_FILE = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"

def make_elem_dict(osm_file, tags=('node', 'way', 'relation')):
    
    elem_dict = col.defaultdict(set)
    
    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    
    # opportunity for 'continue' here...
    # also, pull out - make function to find correct element
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'NHD:ComID':
                    # am overwriting tag here from prev. loop - call something else
                    for tag in elem.iter("tag"):
                        elem_dict[tag.attrib['k']].add(tag.attrib['v'])
        root.clear()
    return elem_dict

if __name__ == '__main__':
    pprint.pprint(make_elem_dict(OSM_FILE))
