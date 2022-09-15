from modules.player import Player
from modules.renderer import Renderer
from modules.tiles import Tiles
from modules.world import World
RENDERING_METHOD = "player" # Can either be "player" or "classic"

tiles = Tiles()
world = World(8,8,tiles=tiles)
player = Player(world=world)
renderer = Renderer(rendering_method=RENDERING_METHOD, player=player, world=world)

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

# def renderWorld():
# 	global running
# 	clear()
# 	zoom = 3
# 	output = []
# 	if renderingMethod == "player":
# 		for i in range(-zoom, zoom):
# 			for j in range(-zoom, zoom):
# 				output.append(getTileFromPos(player.x + j, player.y + i).render())
# 			output.append("\n")
# 		output[(len(list(filter(lambda i: i != "\n",output)))//2)+6] = player.render()
# 	elif renderingMethod == "classic":
# 		for i in range(len(world)):
# 			for j in range(len(world[i])):
# 				if i == player.y and j == player.x:
# 					output.append(player.render())
# 				else:
# 					output.append(getTileFromPos(j, i).render())
# 			output.append("\n")
# 	else:
# 		print(f"{Fore.LIGHTMAGENTA_EX}[FATL]{Fore.RED} unknown rendering method \"{str(renderingMethod)}\", shutting down {Fore.RESET}")
# 		running = False
# 		quit(1)

# 	print(''.join(map(str, output)))

# print(world)

while running:
	renderer.render()
	print(f"X: {player.x} | Y: {player.y}")
	# print(f"Current Tile: {getTileFromPos(player.x, player.y).render()}")
	# rinp = keyboard.read_key()
	rinp = input("Input: ")
	inp = rinp.lower()
	if inp == "q":
		print("Goodbye!")
		print(world)
		quit()
	elif inp.startswith("w"):
		player.movePlayer(0,-1)
	elif inp.startswith("s"):
		player.movePlayer(0,1)
	elif inp.startswith("a"):
		player.movePlayer(-1,0)
	elif inp.startswith("d"):
		player.movePlayer(1,0)

print(world.data)