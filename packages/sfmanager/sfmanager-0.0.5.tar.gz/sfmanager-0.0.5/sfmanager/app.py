class FileManager:
	filename = None
	level = None

	def __init__(self, filename, level):
		self.filename = str(filename)
		self.level = int(level)

	def readline(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r") as f:
					raw = f.readline()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")

	def readlines(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r") as f:
					raw = f.readlines()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")
	def set(self, text):
		if self.level >= 2:
			try:
				with open(f"{self.filename}", "w") as f:
					f.write(text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
				return 0
		else:
			return 0
	def add(self, text):
		if self.level >= 2:
			try:
				with open(f"{self.filename}", "w") as f:
					f.write(f.read() + text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
				return 0
		else:
			return 0
	def add(self, target, text):
		if self.level >= 2:
			try:
				with open(f"{self.filename}", "w") as f:
					f.write(f.read().replace(target, text))
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
				return 0
		else:
			return 0