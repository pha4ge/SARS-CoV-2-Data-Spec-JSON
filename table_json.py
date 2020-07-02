#!/usr/bin/env python

import argparse
import csv
import json
import re


def interface_label_to_property_key(interface_label):
    property_key = re.sub(r'[^\w {}]', '_', interface_label).replace(' ', '_').replace('__', '_').lower()
    property_key = re.sub(r'_$', '', property_key)

    return property_key


def parse_properties_table(path_to_properties_table):
    datatype_map = {
        "String": "string",
        "Date": "string",
        "Int": "integer",
        "Float": "number",
        "Email": "string",
        "Bioproject_ID": "string",
        "Biosample_ID": "string",
        "SRA_ID": "string",
        "Genbank_ID": "string",
        "GISAID_ID": "string"
    }

    format_map = {
        "String": None,
        "Date": "date",
        "Int": None,
        "Float": None,
        "Email": "email",
        "Bioproject_ID": None,
        "Biosample_ID": None,
        "SRA_ID": None,
        "Genbank_ID": None,
        "GISAID_ID": None
    }

    pattern_map = {
        "String": None,
        "Date": None,
        "Int": None,
        "Float": None,
        "Email": None,
        "Bioproject_ID": "([a-zA-Z]{5})\d*",
        "Biosample_ID": "([a-zA-Z]{5})\d*",
        "SRA_ID": "([a-zA-Z]{3})\d*",
        "Genbank_ID": "([a-zA-Z]{2})\d*.\d{1}",
        "GISAID_ID": "([a-zA-Z]{3}_)+\d*"
    }

    properties = {}

    with open(path_to_properties_table) as f:
        reader = csv.DictReader(f)
        for row in reader:
            property_key = interface_label_to_property_key(row['Interface Label'])
            properties[property_key] = {}
            properties[property_key]['description'] = row['Definition']
            type = datatype_map[row['Value Type']]
            properties[property_key]['type'] = type
            format = format_map[row['Value Type']]
            if format:
                properties[property_key]['format'] = format
            pattern = pattern_map[row['Value Type']]
            if pattern:
                properties[property_key]['pattern'] = pattern
            properties[property_key]['examples'] = list(map(str.strip, row['Example'].split(';')))  # examples separated by semicolon

    return properties


def get_required_fields(path_to_properties_table):
    required_fields = []
    with open(path_to_properties_table) as f:
        reader = csv.DictReader(f)
        for row in reader:
            property_key = interface_label_to_property_key(row['Interface Label'])
            if row['Required/Optional'] == 'Required':
                required_fields.append(property_key)

    return required_fields


def main(args):
    
    schema = {
        "$schema": "http://json-schema.org/draft/2019-09/schema#",
        "type": "object",
        "properties": {},
        "required": [],
    }
    
    schema['properties'] = parse_properties_table(args.input)
    schema['required'] = get_required_fields(args.input)
    
    print(json.dumps(schema))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', help='Input schema attributes table')

    args = parser.parse_args()
    main(args)
