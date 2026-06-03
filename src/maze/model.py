from typing import Self

from src.utils import Point


class Cell:
    def __init__(self, n: bool = True, e: bool = True,
                 s: bool = True, w: bool = True) -> None:
        self._n = n
        self._e = e
        self._s = s
        self._w = w

    @property
    def n(self) -> bool:
        return self._n

    @n.setter
    def n(self, value: bool) -> None:
        self._n = value

    @property
    def e(self) -> bool:
        return self._e

    @e.setter
    def e(self, value: bool) -> None:
        self._e = value

    @property
    def s(self) -> bool:
        return self._s

    @s.setter
    def s(self, value: bool) -> None:
        self._s = value

    @property
    def w(self) -> bool:
        return self._w

    @w.setter
    def w(self, value: bool) -> None:
        self._w = value

    def __eq__(self, other: Self) -> bool:
        return (
            self.n == other.n and
            self.e == other.e and
            self.s == other.s and
            self.w == other.w
        )

    def __hash__(self) -> int:
        return hash((self.n, self.e, self.s, self.w))

    def __str__(self) -> str:
        return format(int(
            self.w << 3 |
            self.s << 2 |
            self.e << 1 |
            self.n << 0
        ), 'X')


class MazeModel:
    def __init__(self, size: Point) -> None:
        self._data: list[list[Cell]]
        self._size: Point = size
        self._data = [[Cell() for _ in range(size.x)] for _ in range(size.y)]

    def get(self, pos: Point) -> Cell:
        return self._data[pos.y][pos.x]

    def set(self, pos: Point, value: Cell) -> None:
        self._data[pos.y][pos.x] = value

    @property
    def size(self) -> Point:
        return self._size
