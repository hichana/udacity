import xml.etree.ElementTree as ET

OSM_FILE = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"
SAMPLE_FILE = "/Users/mchana/GitHub/udacity/P3/PROJECT/supporting_files/samples/new-orleans_samplek10"

k = 10 # Parameter: take every k-th top level element

def get_element(osm_file, tags=('node', 'way', 'relation')):

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            for tag_elem in elem.iter("tag"):
                if tag_elem.attrib['k'] == 'NHD:ComID':
                    yield elem
        root.clear()


def make_file(osm_read, osm_write):
    with open(osm_write, 'w') as output:
        output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output.write('<osm>\n  ')

        for i, element in enumerate(get_element(osm_read)):
            if i % k == 0:
                output.write(ET.tostring(element, encoding='unicode'))

        output.write('</osm>')

if __name__ == '__main__':
    make_file(OSM_FILE, SAMPLE_FILE)
