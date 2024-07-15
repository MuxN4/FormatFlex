import argparse
import csv
import json
import xmltodict
import pandas as pd
import os

def validate_file(file_path, expected_extension):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    if not file_path.endswith(expected_extension):
        raise ValueError(f"The file {file_path} does not have the expected {expected_extension} extension.")

def csv_to_json(csv_file, json_file):
    try:
        validate_file(csv_file, '.csv')
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient='records', lines=True)
        print(f"CSV data from {csv_file} has been converted to JSON and saved to {json_file}")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")

def json_to_xml(json_file, xml_file):
    try:
        validate_file(json_file, '.json')
        with open(json_file, 'r') as jf:
            json_data_list = [json.loads(line) for line in jf.readlines()]

        xml_data_list = []
        for json_data in json_data_list:
            xml_data = xmltodict.unparse({"root": json_data}, pretty=True)
            xml_data_list.append(xml_data)

        with open(xml_file, 'w') as xf:
            for xml_data in xml_data_list:
                xf.write(xml_data + '\n')

        print(f"JSON data from {json_file} has been converted to XML and saved to {xml_file}")
    except Exception as e:
        print(f"Error converting JSON to XML: {e}")

def json_to_csv(json_file, csv_file):
    try:
        validate_file(json_file, '.json')
        df = pd.read_json(json_file, lines=True)
        df.to_csv(csv_file, index=False)
        print(f"JSON data from {json_file} has been converted to CSV and saved to {csv_file}")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

def xml_to_json(xml_file, json_file):
    try:
        validate_file(xml_file, '.xml')
        with open(xml_file, 'r') as xf:
            xml_data = xf.read()
        
        json_data = xmltodict.parse(xml_data)
        json_data = json.loads(json.dumps(json_data["root"]))  # Convert to standard JSON format

        with open(json_file, 'w') as jf:
            json.dump(json_data, jf, indent=4)
        
        print(f"XML data from {xml_file} has been converted to JSON and saved to {json_file}")
    except Exception as e:
        print(f"Error converting XML to JSON: {e}")

def main():
    parser = argparse.ArgumentParser(description="Data Converter Utility")
    parser.add_argument('conversion', choices=['csv_to_json', 'json_to_xml', 'json_to_csv', 'xml_to_json'], help="Type of conversion to perform")
    parser.add_argument('input_file', help="Path to the input file")
    parser.add_argument('output_file', help="Path to the output file")

    args = parser.parse_args()

    if args.conversion == 'csv_to_json':
        csv_to_json(args.input_file, args.output_file)
    elif args.conversion == 'json_to_xml':
        json_to_xml(args.input_file, args.output_file)
    elif args.conversion == 'json_to_csv':
        json_to_csv(args.input_file, args.output_file)
    elif args.conversion == 'xml_to_json':
        xml_to_json(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
