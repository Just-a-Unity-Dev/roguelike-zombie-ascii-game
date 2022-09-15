from colorama import Fore
import random

from modules.world import World

class Player:
	"""
	The player character, including the transform and functions.
	"""
	def __init__(self, world: World) -> None:
		self.x: int = 0
		self.y: int = 0
		self.sprite: str = "@"
		self.color: str = Fore.LIGHTGREEN_EX
		self.world: World = world
	
	def render(self) -> str:
		return f"{self.color}{self.sprite}{Fore.RESET}"
	
	def setPosition(self, x: int, y: int, solid: bool = False) -> None:
		tile = self.world.get_tile_from_pos(x, y)
		if solid:
			if tile.solid:
				# don't move there if it's solid
				return False
		self.x = x
		self.y = y
	
	def randomizePosition(self) -> None:
		self.setPosition(random.randint(0, self.world.width), random.randint(0, self.world.height))

	def offsetPosition(self, x: int, y: int) -> None:
		self.setPosition(self.x + x, self.y + y, False)
	
	def movePlayer(self, x: int, y: int) -> None:
		self.setPosition(self.x + x, self.y + y, True)