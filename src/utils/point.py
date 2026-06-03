class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int
        self.y: int
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @y.setter
    def y(self, value: int) -> None:
        self._y = value

    def __str__(self) -> str:
        return f"(x={self.x}, y={self.y})"
