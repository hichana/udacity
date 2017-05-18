import xml.etree.ElementTree as ET
import collections as col
import pprint

# path to osm file
OSM_FILE = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"

def make_elem_dict(osm_file, tags=('node', 'way', 'relation')):

    # defaultdict holds all unique values
    elem_dict = col.defaultdict(set)

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)

    # adds to defaultdict only if element has a child tag element with 'NHD:ComID'
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'NHD:ComID':
                    # am overwriting tag here from prev. loop - call something else
                    for tag in elem.iter("tag"):
                        elem_dict[tag.attrib['k']].add(tag.attrib['v'])
        # clear root element to save memory
        root.clear()
    return elem_dict

if __name__ == '__main__':
    pprint.pprint(make_elem_dict(OSM_FILE))
