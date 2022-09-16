from colorama import Fore, Style

class Tile:
	def __init__(self, sprite: str = " ", color = Fore.RESET, solid=False) -> None:
		self.sprite = sprite
		self.color = color
		self.solid = solid

	def render(self) -> str:
		return f"{self.color}{self.sprite}{Fore.RESET}{Style.RESET_ALL}"

class Tiles:
	tileref = [
		Tile(), # air
		Tile(sprite="?", color=Fore.LIGHTRED_EX, solid=True), # error
		Tile(sprite="#", color=Fore.YELLOW, solid=True), # wood wall
		Tile(sprite=u"\u2588", color=Fore.WHITE, solid=True), # rock ungabunga
		Tile(sprite=u"\u2591", color=Fore.WHITE, solid=False), # rock roof
		Tile(sprite=u"\u2588", color=Fore.RED, solid=False), # lava oogh
		Tile(sprite=".", color=Style.BRIGHT + Fore.BLACK, solid=False), # tile
	]

	def get_tile_from_id(self, id: int):
		try:
			return self.tileref[int(id)]
		except IndexError:
			return self.tileref[1]
		except KeyError:
			return self.tileref[1]