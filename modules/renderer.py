from colorama import Fore
from modules.player import Player
from modules.world import World
from modules.utilities import Utilities

class Renderer:
	def __init__(self, rendering_method: str, player: Player, world: World) -> None:
		self.rendering_method = rendering_method
		self.player = player
		self.world = world

	def render(self):
		global running
		Utilities.clear()
		zoom = 6
		output = []
		if self.rendering_method == "player":
			for i in range(-zoom, zoom):
				for j in range(-zoom, zoom):
					output.append(self.world.get_tile_from_pos(self.player.x + j, self.player.y + i).render())
				output.append("\n")
			output[(zoom*2)*(zoom+1)] = self.player.render()
			# output[(len(list(filter(lambda i: i != "\n",output)))//2)+6] = self.player.render()
		elif self.rendering_method == "classic":
			for i in range(len(self.world.data)):
				for j in range(len(self.world.data[i])):
					if i == self.player.y and j == self.player.x:
						output.append(self.player.render())
					else:
						output.append(self.world.get_tile_from_pos(j, i).render())
				output.append("\n")
		else:
			print(f"{Fore.LIGHTMAGENTA_EX}[FATL]{Fore.RED} unknown rendering method \"{str(self.rendering_method)}\", shutting down {Fore.RESET}")
			running = False
			quit(1)

		print(''.join(map(str, output)))