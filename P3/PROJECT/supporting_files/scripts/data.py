import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
import pprint
import inspect as ins
import cerberus
import schema_validation
import fix_dict as fd

# path to osm file
OSM_PATH = "/Users/mchana/GitHub/udacity/large_files/new-orleans_region.osm"

# path where CSV files will be saved
exports_path = "/Users/mchana/GitHub/udacity/P3/PROJECT/supporting_files/exports/csv/"

NODES_PATH = exports_path + "nodes.csv"
NODES_TAGS_PATH = exports_path + "nodes_tags.csv"
WAYS_PATH = exports_path + "ways.csv"
WAYS_NODES_PATH = exports_path + "ways_nodes.csv"
WAYS_TAGS_PATH = exports_path + "ways_tags.csv"
RELATIONS_PATH = exports_path + "relations.csv"
RELATIONS_MEMBERS_PATH = exports_path + "relations_members.csv"
RELATIONS_TAGS_PATH = exports_path + "relations_tags.csv"


# regex checks
LOWER_UPPER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+', re.IGNORECASE)
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# schema validation
SCHEMA = schema_validation.project_schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODES_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODES_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAYS_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAYS_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAYS_NODES_FIELDS = ['id', 'node_id', 'position']
RELATIONS_FIELDS = ['id', 'user', 'uid', 'version', 'timestamp', 'changeset']
RELATIONS_TAGS_FIELDS = ['id', 'key', 'value', 'type']
RELATIONS_MEMBERS_FIELDS = ['id', 'mem_id','type', 'role', 'position']


# extracts data from an element and returns a dict
def shape_element(element, node_attr_fields=NODES_FIELDS, way_attr_fields=WAYS_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    # holds dicts of 'tag' elements
    tags = []

    # creates dicts for 'tag' elements
    for child in element:
            if child.tag != 'tag' or PROBLEMCHARS.search(child.attrib['k']):
                continue
            tag_dict = {'id':element.attrib['id'],
                        'key':child.attrib['k'],
                        'value':child.attrib['v'],
                        'type':default_tag_type
                       }

            if LOWER_UPPER_COLON.search(tag_dict['key']):
                key_split = tag_dict['key'].split(':',1)
                tag_dict['key'] = key_split[1]
                tag_dict['type'] = key_split[0]

            tags.append(tag_dict)

    if element.tag == 'node':
        node_attribs = {'id':element.attrib['id'],
                   'user':element.attrib['user'],
                   'uid':element.attrib['uid'],
                   'version':element.attrib['version'],
                   'lat':element.attrib['lat'],
                    'lon':element.attrib['lon'],
                    'timestamp':element.attrib['timestamp'],
                    'changeset':element.attrib['changeset']
                   }
        return {'node': node_attribs, 'node_tags': tags}

    elif element.tag == 'way':
        way_attribs = {'id':element.attrib['id'],
                      'user':element.attrib['user'],
                      'uid':element.attrib['uid'],
                      'version':element.attrib['version'],
                      'timestamp':element.attrib['timestamp'],
                      'changeset':element.attrib['changeset']
                      }

        # holds list of dicts for 'nd' elements
        way_nodes = []

        # counter to increment instances of 'nd' tags
        nd_counter = 0

        for child in element:
            if child.tag == 'nd':
                nd_dict = {'id':element.attrib['id'],
                          'node_id':child.attrib['ref'],
                          'position':nd_counter}
                nd_counter += 1
                way_nodes.append(nd_dict)

        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}

    elif element.tag == 'relation':
        rel_attribs = {
            'id':element.attrib['id'],
            'user':element.attrib['user'],
            'uid':element.attrib['uid'],
            'version':element.attrib['version'],
            'timestamp':element.attrib['timestamp'],
            'changeset':element.attrib['changeset']
        }

        rel_members = []

        mem_counter = 0

        for child in element:
            if child.tag == 'member':
                mem_dict = {
                    'id':element.attrib['id'],
                    'mem_id':child.attrib['ref'],
                    'type':child.attrib['type'],
                    'role':child.attrib['role'],
                    'position':mem_counter
                }
                mem_counter += 1
                rel_members.append(mem_dict)

        return {'relation': rel_attribs, 'relation_members': rel_members, 'relation_tags': tags}

# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_elements(osm_file, tags=('node', 'way', 'relation')):

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)

    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            for tag_elem in elem.iter("tag"):
                if tag_elem.attrib['k'] == 'NHD:ComID':
                    yield elem
        root.clear()

# takes in ET.element obj, validator object, schema
def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.items())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)

        raise Exception(message_string.format(field, error_string))

# ================================================== #
#               Main Function                        #
# ================================================== #

# file_in=OSM file, validate=True or False
def process_map(file_in, validate):

    # with-open files in write mode
    with codecs.open(NODES_PATH, 'w') as nodes_file, \
        codecs.open(NODES_TAGS_PATH, 'w') as nodes_tags_file, \
        codecs.open(WAYS_PATH, 'w') as ways_file, \
        codecs.open(WAYS_NODES_PATH, 'w') as ways_nodes_file, \
        codecs.open(WAYS_TAGS_PATH, 'w') as ways_tags_file, \
        codecs.open(RELATIONS_PATH, 'w') as relations_file, \
        codecs.open(RELATIONS_MEMBERS_PATH, 'w') as relations_members_file, \
        codecs.open(RELATIONS_TAGS_PATH, 'w') as relations_tags_file:

        # create writer objects
        nodes_writer = csv.DictWriter(nodes_file, NODES_FIELDS)
        nodes_tags_writer = csv.DictWriter(nodes_tags_file, NODES_TAGS_FIELDS)
        ways_writer = csv.DictWriter(ways_file, WAYS_FIELDS)
        ways_nodes_writer = csv.DictWriter(ways_nodes_file, WAYS_NODES_FIELDS)
        ways_tags_writer = csv.DictWriter(ways_tags_file, WAYS_TAGS_FIELDS)
        relations_writer = csv.DictWriter(relations_file, RELATIONS_FIELDS)
        relations_members_writer = csv.DictWriter(relations_members_file, RELATIONS_MEMBERS_FIELDS)
        relations_tags_writer = csv.DictWriter(relations_tags_file, RELATIONS_TAGS_FIELDS)

        # write headers using field names specified in DictWriter constructor
        nodes_writer.writeheader()
        nodes_tags_writer.writeheader()
        ways_writer.writeheader()
        ways_nodes_writer.writeheader()
        ways_tags_writer.writeheader()
        relations_writer.writeheader()
        relations_members_writer.writeheader()
        relations_tags_writer.writeheader()

        # the Validator class object instantiated here is callable to normalize
        # and/or validate any mapping against validation schema
        validator = cerberus.Validator()

        # loop over generator obj from get_element()
        for element in get_elements(file_in, tags=('node', 'way', 'relation')):
            # takes in the element from iterator, outputs a dict
            el = shape_element(element)

            # cleans data in dict
            el2 = fd.fix_dict(el)

            if not el:
                continue
            if validate is True:
                validate_element(el2, validator)
            # write each dict to appropriate writer obj
            if element.tag == 'node':
                nodes_writer.writerow(el2['node'])
                nodes_tags_writer.writerows(el2['node_tags'])
            elif element.tag == 'way':
                ways_writer.writerow(el2['way'])
                ways_nodes_writer.writerows(el2['way_nodes'])
                ways_tags_writer.writerows(el2['way_tags'])
            elif element.tag == 'relation':
                relations_writer.writerow(el2['relation'])
                relations_members_writer.writerows(el2['relation_members'])
                relations_tags_writer.writerows(el2['relation_tags'])

if __name__ == '__main__':
    process_map(OSM_PATH, validate=True)
