from colorama import Fore

from modules.world import World

class Player:
	def __init__(self, world: World) -> None:
		self.x = 0
		self.y = 0
		self.sprite = "@"
		self.color = Fore.LIGHTGREEN_EX
		self.world = world
	
	def render(self) -> str:
		return f"{self.color}{self.sprite}{Fore.RESET}"
	
	def setPosition(self, x: int, y: int, solid: bool) -> None:
		tile = self.world.get_tile_from_pos(x, y)
		if solid:
			if tile.solid:
				# don't move there if it's solid
				return False
		self.x = x
		self.y = y

	def offsetPosition(self, x: int, y: int) -> None:
		self.setPosition(self.x + x, self.y + y, False)
	
	def movePlayer(self, x: int, y: int) -> None:
		self.setPosition(self.x + x, self.y + y, True)