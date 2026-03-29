class CountSquares:

    def __init__(self):
        self.pointsDict = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsDict[(x, y)] = self.pointsDict.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        for a, b in self.pointsDict:
            if (a, y) in self.pointsDict and (x, b) in self.pointsDict \
            and abs(y - b) != 0 and abs(x - a) != 0:
                total += (self.pointsDict[(a, b)] * self.pointsDict[(a, y)] * self.pointsDict[(x, b)])
        
        return total