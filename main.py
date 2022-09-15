from colorama import Fore
from colorama import Style
import keyboard
import pyfiglet
import math
import os
renderingMethod = "player" # Can either be "player" or "classic"

class Player:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.sprite = "@"
        self.color = Fore.GREEN
    
    def render(self) -> str:
        return f"{self.color}{self.sprite}{Fore.RESET}"
    
    def setPosition(self, x: int, y: int, forceful: bool) -> None:
        tile = getTileFromPos(x, y)
        if forceful:
            if tile.solid:
                # don't move there if it's solid
                return False
        self.x = x
        self.y = y

    def offsetPosition(self, x: int, y: int) -> None:
        self.setPosition(self.x + x, self.y + y, False)
    
    def movePlayer(self, x: int, y: int) -> None:
        self.setPosition(self.x + x, self.y + y, True)

class Tile:
    def __init__(self, sprite: str = " ", color = Fore.RESET, solid=False) -> None:
        self.sprite = sprite
        self.color = color
        self.solid = solid

    def render(self) -> str:
        return f"{self.color}{self.sprite}{Fore.RESET}"
        
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

player = Player()
tileref = {
    "air": Tile(),
    "error": Tile(sprite="?", color=Fore.RED, solid=True),
    "wall": Tile(sprite="#", color=Fore.LIGHTYELLOW_EX, solid=True)
}

world = []
def parseMap():
    with open(r"./maps/map.csv", "r") as f:
        currentLine = 1
        for line in f.readlines():
            values = line.split(",")
            world.append(values)
            print(f"loaded line #{currentLine}")
            currentLine += 1
    print("finished parsing the map")

parseMap()

running = True

def getTileFromId(id: str):
    try:
        return tileref[id]
    except IndexError:
        return tileref["error"]
    except KeyError:
        return tileref["error"]

def getTileFromPos(x: int, y: int):
    if x < 0 or y < 0:
        return getTileFromId("error")
    try:
        return getTileFromId(world[y][x])
    except IndexError:
        return getTileFromId("error")

def renderWorld():
    global running
    clear()
    output = []
    zoom = 3
    if renderingMethod == "player":
        for i in range(-zoom, zoom):
            for j in range(-zoom * 2, zoom * 2):
                output.append(getTileFromPos(player.x + j, player.y + i).render())
            output.append("\n")
    elif renderingMethod == "classic":
        for i in range(len(world)):
            for j in range(len(world[i])):
                if i == player.y and j == player.x:
                    output.append(player.render())
                else:
                    output.append(getTileFromPos(j, i).render())
            output.append("\n")
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}[FATL]{Fore.RED}Unknown rendering method \"{str(renderingMethod)}\", shutting down! {Fore.RESET}")
        running = False
        quit(1)

    print(''.join(map(str, output)))

print(world)

while running:
    renderWorld()
    print(f"X: {player.x} | Y: {player.y}")
    print(f"Current Tile: {getTileFromPos(player.x, player.y).render()}")
    rinp = keyboard.read_key()
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