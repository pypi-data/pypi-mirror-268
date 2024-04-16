import csv
import sys

def validate_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the header row
            num_fields = len(headers)
            row_count = 0  # Initialize row count
            errors = []  # List to store error messages

            if not all(headers):  # Check for empty header fields
                errors.append("Empty header field detected.")

            for row_number, row in enumerate(reader, start=2):
                row_count += 1
                if len(row) != num_fields:  # Check each row for correct number of fields
                    errors.append(f"Row {row_number} has incorrect number of fields.")

            # Prepare a summary of the file's structure and any errors found
            result = f"Total rows checked: {row_count + 1}, Fields per row: {num_fields}."
            if errors:
                return result + " Errors: " + ", ".join(errors)
            
            return result + " CSV is valid according to RFC 4180."

    except csv.Error as e:
        return f"CSV parsing error: {str(e)}"
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Please enter the path to the CSV file to validate: ")

    result = validate_csv(file_path)
    print(result)

if __name__ == "__main__":
    main()
