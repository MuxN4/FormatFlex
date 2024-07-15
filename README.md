# FormatFlex

FormatFlex Utility is a Python script designed to convert data between various formats including CSV, JSON, and XML. This utility provides command-line functionality to perform conversions based on user input.

## Features

CSV to JSON Conversion: Convert CSV data to JSON format.
JSON to XML Conversion: Convert JSON data to XML format.
JSON to CSV Conversion: Convert JSON data back to CSV format.
XML to JSON Conversion: Convert XML data to JSON format.

## Prerequisites

Before using FormatFlex, ensure you have the following installed:
 - Python 3.x
 - Required Python packages (install using pip install -r requirements.txt)

## Installation and Setup

Clone the repository:

    ```bash
    Copy code
    git clone https://github.com/MuxN4/FormatFlex.git
    cd data-converter
    ```
Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
# Usage

## Command-line Interface
To use FormatFlex, run the data_converter.py script from the command line with the following options:

    ```bash
    python data_converter.py <conversion_type> <input_file> <output_file>
    ```
Replace `<conversion_type>` with one of the following options:

`csv_to_json`: Convert CSV to JSON
`json_to_xml`: Convert JSON to XML
`json_to_csv`: Convert JSON to CSV
`xml_to_json`: Convert XML to JSON

Replace `<input_file>` and `<output_file>` with the paths to your input and output files respectively.

## Examples
## Convert input.csv from CSV to JSON:

    ```bash
    python data_converter.py csv_to_json input.csv output.json
    ```

## Convert input.json from JSON to XML:

    ```bash
    python data_converter.py json_to_xml input.json output.xml
    ```
## Sample Data
The input.csv file in the project contains sample data that you can use for testing purposes.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

