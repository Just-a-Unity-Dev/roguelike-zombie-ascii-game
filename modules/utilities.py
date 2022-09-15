import os

class Utilities:
	def __init__(self) -> None:
		pass

	def clear():
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")