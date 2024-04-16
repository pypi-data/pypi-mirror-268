# rfccsv

`rfccsv` is a lightweight, easy-to-use Python package designed to validate CSV files according to RFC 4180 standards. It ensures that CSV files are properly formatted and meet the criteria necessary for standardized data processing tasks.

## Features

- Validate any CSV file to check its compliance with RFC 4180.
- Easy integration into existing Python projects.
- Detailed error reporting for quick troubleshooting of CSV files.

## Installation

Install `rfccsv` using pip:

```bash
pip install rfccsv
```

Or, if you are using Poetry:

```bash
poetry add rfccsv
```

## Usage

Here’s how you can use `rfccsv` to validate a CSV file:

```python
from rfccsv import validate_csv

# Validate a CSV file
result = validate_csv('path/to/your/file.csv')
print(result)
```

### Validating Files

You can validate CSV files by providing the path to the file:

```python
validate_csv('example.csv')
```

## License

Distributed under the MIT License. 

## Contact

Project Link: [https://github.com/trygu/rfccsv](https://github.com/trygu/rfccsv)

## Acknowledgements

- [RFC 4180 Standard](https://tools.ietf.org/html/rfc4180)

