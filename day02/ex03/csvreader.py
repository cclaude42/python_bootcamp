


class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file_obj = open(file_name, 'r')

    def __enter__(self):
        return self.file_obj

    def __exit__(self, *args):
        self.file_obj.close()

    def getdata(self):
        pass

    def getheader(self):
        pass

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
