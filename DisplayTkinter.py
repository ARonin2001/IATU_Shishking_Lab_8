import tkinter as tk

class DisplayTkinter:
	__root = None

	def __init__(self, title = 'Contracts For Additional Education', width = 700, height = 700):
		self.title = title
		self.width = width
		self.height = height
		self.geometry = f'{width}x{height}'

		self.__root = tk.Tk()
		self.__root.title(title)
		self.__root.geometry(self.geometry)

	def __center_window(self):
		screen_width = self.__root.winfo_screenwidth()
		screen_height = self.__root.winfo_screenheight()
		x = (screen_width - self.width) // 2
		y = (screen_height - self.height) // 2
		self.__root.geometry(f"{self.geometry}+{x}+{y}")

	def get_root(self):
		return self.__root

	def display(self):
		self.__center_window()
		self.__root.mainloop()