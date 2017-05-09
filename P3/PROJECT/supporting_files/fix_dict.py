def fix_tags_dict(tags_dict):
    if tags_dict['key'] == 'FTYPE':
        tags_dict['key'] = 'FType'
    if tags_dict['key'] == 'RESOLUTION':
        tags_dict['key'] = 'Resolution'
    if tags_dict['key'] == 'water':
        tags_dict['value'] = tags_dict['value'].lower()
    if tags_dict['key'] == 'source':
        if tags_dict['value'] == 'bing':
            tags_dict['value'] = 'Bing'
        elif tags_dict['value'] == 'landsat':
            tags_dict['value'] = 'Landsat'
    if tags_dict['key'] == 'name':
        tags_dict['value'] = tags_dict['value'].title()



def fix_dict(dict_el):
    for k, v in dict_el.items():
        if k == "node_tags" or k == "way_tags" or k == "relation_tags":
            # here, value is a list of dicts
            for tags_dict in v:
                fix_tags_dict(tags_dict)
    return dict_el
