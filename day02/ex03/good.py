#!/usr/bin/env python3
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader("good.csv", sep=",", header=True) as file:
        if file:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
        else:
            print("File is corrupted")
