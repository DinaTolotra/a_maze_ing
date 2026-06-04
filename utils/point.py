class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __str__(self) -> str:
        return f"(x={self.x}, y={self.y})"

    def __add__(self, other: object) -> "Point":
        if isinstance(object, Point):
            return NotImplemented
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if (isinstance(other, tuple) and
            all(isinstance(elem, int) for elem in other)):
            return Point(self.x + other[0], self.y + other[1])

    def __sub__(self, other: object) -> "Point":
        if isinstance(object, Point):
            return NotImplemented
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        if (isinstance(other, tuple) and
            all(isinstance(elem, int) for elem in other)):
            return Point(self.x - other[0], self.y - other[1])
