from modules.generation import Generation
from modules.player import Player
from modules.renderer import Renderer
from modules.tiles import Tiles
from modules.world import World
from random import randint
RENDERING_METHOD = "player" # Can either be "player" or "classic"
WORLD_WIDTH = 64
WORLD_HEIGHT = 64
seed = randint(1,2147483647)

tiles = Tiles()
gen = Generation()
world = gen.generate(tiles=tiles, size_x=WORLD_WIDTH, size_y=WORLD_HEIGHT, seed=randint(1,2147483647))
player = Player(world=world)
renderer = Renderer(rendering_method=RENDERING_METHOD, player=player, world=world)

player.randomizePosition()

# def parseMap():
# 	print("beginning to parse map")
# 	with open(r"./map.csv", "r") as f:
# 		currentLine = 1
# 		for line in f.readlines():
# 			values = line.strip().split(",")
# 			world.append(values)
# 			print(f"loaded line #{currentLine}")
# 			currentLine += 1
# 	if world == []:
# 		print(f"{Fore.LIGHTMAGENTA_EX}[FATL]{Fore.RED} world is still empty (is the CSV file filled?), shutting down {Fore.RESET}")
# 		quit(1)
# 	print("finished parsing the map")

# parseMap()

running = True

while running:
	renderer.render()
	print(f"Seed: {seed}")
	print(f"X: {player.x} | Y: {player.y}")
	# print(f"Current Tile: {getTileFromPos(player.x, player.y).render()}")
	# rinp = keyboard.read_key()
	rinp = input("Input: ")
	inp = rinp.lower()
	if inp == "q":
		print("Goodbye!")
		quit()
	elif inp.startswith("w"):
		player.movePlayer(0,-1)
	elif inp.startswith("s"):
		player.movePlayer(0,1)
	elif inp.startswith("a"):
		player.movePlayer(-1,0)
	elif inp.startswith("d"):
		player.movePlayer(1,0)
	elif inp.startswith("g"):
		seed = randint(1,2147483647)
		world.data = gen.generate(tiles=tiles, size_x=WORLD_WIDTH, size_y=WORLD_HEIGHT, seed=seed).data
