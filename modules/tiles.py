from colorama import Fore

class Tile:
	def __init__(self, sprite: str = " ", color = Fore.RESET, solid=False) -> None:
		self.sprite = sprite
		self.color = color
		self.solid = solid

	def render(self) -> str:
		return f"{self.color}{self.sprite}{Fore.RESET}"

class Tiles:
	tileref = [
		Tile(), # air
		Tile(sprite="?", color=Fore.LIGHTRED_EX, solid=True), # error
		Tile(sprite="#", color=Fore.YELLOW, solid=True), # wood wall
		Tile(sprite=u"\u2588", color=Fore.WHITE, solid=True) # rock ungabunga
	]

	def get_tile_from_id(self, id: int):
		try:
			return self.tileref[int(id)]
		except IndexError:
			return self.tileref[1]
		except KeyError:
			return self.tileref[1]