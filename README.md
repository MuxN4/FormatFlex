## Features

 - CSV to JSON Conversion: Convert CSV data to JSON format.
 - JSON to XML Conversion: Convert JSON data to XML format.
 - JSON to CSV Conversion: Convert JSON data back to CSV format.
 - XML to JSON Conversion: Convert XML data to JSON format.

# Usage ℹ️

## Command-line Interface

To use FormatFlex, run the data_converter.py script from the command line with the following options:

    bash
    python data_converter.py <conversion_type> <input_file> <output_file>
    
Replace `<conversion_type>` with one of the following options:

`csv_to_json`: Convert CSV to JSON
`json_to_xml`: Convert JSON to XML
`json_to_csv`: Convert JSON to CSV
`xml_to_json`: Convert XML to JSON

Replace `<input_file>` and `<output_file>` with the paths to your input and output files respectively.

## Examples
## Convert input.csv from CSV to JSON:

    bash
    python data_converter.py csv_to_json input.csv output.json
    

## Convert input.json from JSON to XML:

    bash
    python data_converter.py json_to_xml input.json output.xml
    
## Sample Data
The input.csv file in the project contains sample data that you can use for testing purposes.
