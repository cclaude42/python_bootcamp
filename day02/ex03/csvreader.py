class CsvReader():
	def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.name = file_name
		self.sep = sep
		self.hbool = header
		self.top = skip_top
		self.bot = skip_bottom

	def __enter__(self):
		try:
			self.file_obj = open(self.name, 'r')
		except:
			return None
		lst = self.file_obj.read().split('\n')
		if self.hbool:
			self.header = lst[0].split(self.sep)
			lst = lst[1:]
		else:
			self.header = "[ No header ]"
		lst = lst[self.top : len(lst) - self.bot - 1]
		self.data = [i.split(self.sep) for i in lst]
		return self

	def __exit__(self, *args):
		if hasattr(self, "file"):
			self.file_obj.close()

	def getheader(self):
		return self.header

	def getdata(self):
		return self.data

print("=== Good ===")
with CsvReader("good.csv", ',', False) as reader:
	if reader == None:
		print("File corrupted!")
	else:
		print(reader.getheader())
		for val in reader.getdata():
			print(val)

print("\n=== Bad ===")
with CsvReader("bad.csv", ',', True) as reader:
	if reader == None:
		print("File corrupted!")
	else:
		print(reader.getheader())
		for val in reader.getdata():
			print(val)
