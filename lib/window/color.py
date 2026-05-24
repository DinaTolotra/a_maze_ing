from typing import Self


class Color:
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        self._r: int
        self._g: int
        self._b: int
        self._a: int
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_int(self, is_big_indian: bool = False) -> int:
        if is_big_indian:
            return int(bytes((self.g, self.b, self.r, self.a)).hex(), 16)
        else:
            return int(bytes((self.a, self.r, self.g, self.b)).hex(), 16)

    @property
    def r(self) -> int:
        return self._r

    @r.setter
    def r(self, value: int) -> None:
        self._r = max(0, min(255, value))

    @property
    def g(self) -> int:
        return self._g

    @g.setter
    def g(self, value: int) -> None:
        self._g = max(0, min(255, value))

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    def b(self, value: int) -> None:
        self._b = max(0, min(255, value))

    @property
    def a(self) -> int:
        return self._a

    @a.setter
    def a(self, value: int) -> None:
        self._a = max(0, min(255, value))

    @staticmethod
    def colorscheme(scheme: str) -> dict[str, Self]:
        colorscheme: dict[str, dict[str, Color]] = {
            "gruvbox": {
                "bg": Color(0x50, 0x49, 0x45, 0xff),
                "fg": Color(0xeb, 0xdb, 0xb2, 0xff),
                "red": Color(0xfb, 0x49, 0x34, 0xff),
                "green": Color(0xb8, 0xbb, 0x26, 0xff),
                "blue": Color(0x83, 0xa5, 0x98, 0xff),
                "yellow": Color(0xfa, 0xbd, 0x2f, 0xff),
                "purple": Color(0xd3, 0x86, 0x9b, 0xff)
            }
        }
        if colorscheme.get(scheme) is not None:
            return colorscheme[scheme]
        else:
            raise ValueError("undefined  colorscheme: " + scheme)
