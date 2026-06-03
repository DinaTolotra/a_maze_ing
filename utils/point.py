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
