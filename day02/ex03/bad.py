#!/usr/bin/env python3
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
        else:
            print("File is corrupted")

