import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    data = []
    with open(INPUT_FILENAME) as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            data.append(row)
        with open(OUTPUT_FILENAME, "w") as output_file:
            output_file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
