from tkinter import W
from modules.tiles import Tiles
from modules.world import World
import random

class Generation:
	def __init__(
		self,
		chance_to_start_alive: int = 40,
		starvation_limit: int = 2,
		birth_number: int = 4,
		overpop_limit: int = 5,
		number_of_steps: int = 5
	) -> None:
		self.chance_to_start_alive = chance_to_start_alive
		self.starvation_limit = starvation_limit
		self.birth_number = birth_number
		self.overpop_limit = overpop_limit
		self.number_of_steps = number_of_steps
	
	def generate(self, tiles: Tiles, x: int = 32, y: int = 32) -> World:
		world = World(x,y,tiles)

		# Thank you.
		# https://gamedevelopment.tutsplus.com/tutorials/generate-random-cave-levels-using-cellular-automata--gamedev-9664
		
		# Rules
		# If a living cell has less than two living neighbours, it dies.
		# If a living cell has two or three living neighbours, it stays alive.
		# If a living cell has more than three living neighbours, it dies.
		# If a dead cell has exactly three living neighbours, it becomes alive.

		choices = [0,3]

		# fill in the world
		for y,v in enumerate(world.data):
			for x,c in enumerate(v):
				world.data[y][x] = random.choices(choices, weights=(self.chance_to_start_alive,60), k=2)[0]
		
		# now do the automata!
		def sim_step():
			for y,v in enumerate(world.data):
				for x,c in enumerate(v):
					cell = world.data[y][x]
					try:
						children = [
							world.data[y + 1][x + 1],
							world.data[y + 1][x],
							world.data[y + 1][x - 1],
							world.data[y][x + 1],
							world.data[y][x - 1],
							world.data[y - 1][x + 1],
							world.data[y - 1][x],
							world.data[y - 1][x - 1],
						]
						total = len([ elem for elem in children if children[elem] != 0])
						if total < self.starvation_limit:
							world.data[y][x] = 0
						elif total == self.birth_number:
							world.data[y][x] = 3
						elif total > self.overpop_limit:
							world.data[y][x] = 0
						else:
							world.data[y][x] = 3
					except IndexError:
						world.data[y][x] = 0

		for i in range(self.number_of_steps):
			sim_step()
		
		return world
