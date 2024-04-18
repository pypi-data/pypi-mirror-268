class Tensor:
	filename = None
	level = None

	def __init__(self, filename, level):
		self.filename = str(filename)
		self.level = int(level)

	def readline(self):
		try:
			f = open(f"{self.path}")
			raw = f.readlines()
			f.close()
			return raw
		except FileNotFoundError:
			print("Something went wrong...")

	def readlines(self):
		try:
			f = open(f"{self.path}")
			raw = f.readline()
			f.close()
			return raw
		except FileNotFoundError:
			print("Something went wrong...")