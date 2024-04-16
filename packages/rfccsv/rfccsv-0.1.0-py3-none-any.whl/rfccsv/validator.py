import csv
import sys

def validate_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            num_fields = len(headers)
            if not all(headers):
                return "Invalid CSV: Empty header field detected."

            for row_number, row in enumerate(reader, start=2):
                if len(row) != num_fields:
                    return f"Invalid CSV: Row {row_number} has incorrect number of fields."

        return "CSV is valid according to RFC 4180."

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

