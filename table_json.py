#!/usr/bin/env python

import argparse
import csv
import json

def parse_properties_table(path_to_properties_table):
    datatype_map = {
        "String": "string",
        "Date": "string",
        "Int": "integer",
        "Float": "number",
    }

    format_map = {
        "String": None,
        "Date": "date",
        "Int": None,
        "Float": None,
    }

    properties = {}

    with open(path_to_properties_table) as f:
        reader = csv.DictReader(f)
        for row in reader:
            property_key = row['Interface Label'].lower().replace(' ', '_')
            properties[property_key] = {}
            properties[property_key]['description'] = row['Definition']
            type = datatype_map[row['Value Type']]
            properties[property_key]['type'] = type
            format = format_map[row['Value Type']]
            if format:
                properties[property_key]['format'] = format
            properties[property_key]['examples'] = [row['Example']]

    return properties


def main(args):
    
    schema = {
        "$schema": "http://json-schema.org/draft/2019-09/schema#",
        "type": "object",
        "properties": {},
        "required": [],
    }
    
    schema['properties'] = parse_properties_table(args.input)
    
    print(json.dumps(schema))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', help='Input schema attributes table')

    args = parser.parse_args()
    main(args)
