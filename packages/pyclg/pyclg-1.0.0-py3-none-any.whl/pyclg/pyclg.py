from os import system
class Display:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = []
		for i in range(self.width*self.height):
			self.grid.append(" ")
		if self.height != height or self.width != width:
			self.height = height; self.width = width;
	def getPx(self, x, y):
		return (self.width*(y-2)+x+1)
	def update(self):
		self.clear()
		out = ""
		for i in range(self.width*self.height):
			out = out + self.grid[i]
			if i % self.width == 0:
				out = out + "|\n"
		out = out + " |\n"
		for i in range(self.width):
			out = out + "_"
		out = out + "|"
		print(out)
	def draw(self, x, y, type):
		if 0>x or x>(self.width) or 0>y or y>(self.height+2):
			print(f"Out Of Bounds Error")
			exit()
		else:
			if type == 0:
				self.grid[self.getPx(x,y)] = "#"
			else:
				if len(type) > 1:
					print("Illegal Size: Must be 1 character in length")
					exit()
				else:
					self.grid[self.getPx(x,y)] = type
	def print(self, str, x, y):
		for i in range(0,len(str)):
			self.draw(x+i,y,str[i])
	def clear(self,par='s'):
		system('cls||clear')
		if par != 's':
			for i in range(self.width*self.height):
				self.grid[i] = " "