from modules.tiles import Tiles

class World:
	def __init__(self, x: int, y: int, tiles: Tiles) -> None:
		self.width = x
		self.height = y
		self.data = [[0]*x for j in range(y)]
		self.tiles = tiles
	
	def get_tile_from_pos(self, x: int, y: int):
		if x < 0 or y < 0 or x > self.width or y > self.height:
			return self.tiles.get_tile_from_id(id=1)
		try:
			return self.tiles.get_tile_from_id(self.data[y][x])
		except IndexError:
			return self.tiles.get_tile_from_id(id=1)
			
	