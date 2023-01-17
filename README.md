# JSON Comparison Script

This script compares two JSON files and creates a new file with the differences commented out.

## Usage

The script takes three arguments:

- `file1`: the path to the first JSON file
- `file2`: the path to the second JSON file
- `output_file`: the path to the file where the differences will be written

Example usage:
compare_json('file1.json', 'file2.json', 'differences.json')


## How it works
1. The script loads the two JSON files using the `json.load()` function from the json module.
2. It compares the two JSON files by comparing keys and values of both JSONs.
3. It creates a dictionary `differences` where it stores the key-value pair where the key is different in both JSONs or the value is different for same key.
4. It writes the `differences` dictionary in the output file using the `write()` method.

## Note

This script is a basic example and may not handle all cases and edge scenarios. Depending on the complexity of your JSON files, you may need to modify the script to handle those cases. Also, this script doesn't handle nested JSONs.

## How to deploy

1. Make sure you have python installed. You can check by running `python --version` in your command line.
2. Make sure you have the necessary modules installed. The script uses the `json` module, which should come with a standard python installation.
3. Run the script by navigating to the directory where the script is located and run the command `python Compare_json.py file1.json file2.json output_file.json`
4. The output_file will be created in the same directory as the script with the differences between the two JSONs commented out.
