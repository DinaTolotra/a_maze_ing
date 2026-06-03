from sys import byteorder


class Color:
    is_big_indian: bool = byteorder == "big"

    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        self._r: int
        self._g: int
        self._b: int
        self._a: int
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @classmethod
    def from_hex(cls, raw: str) -> "Color":
        raw = raw[1:]
        if len(raw) == 8:
            return cls(
                int(raw[0:2], 16),
                int(raw[2:4], 16),
                int(raw[4:6], 16),
                int(raw[6:8], 16),
            )
        elif len(raw) == 6:
            return cls(
                int(raw[0:2], 16),
                int(raw[2:4], 16),
                int(raw[4:6], 16),
                0xff,
            )
        else:
            raise ValueError("invalid hex value: " + raw)

    def __int__(self) -> int:
        if Color.is_big_indian:
            return int(
                self.b << 24 |
                self.g << 16 |
                self.r << 8 |
                self.a << 0
            )
        else:
            return int(
                self.a << 24 |
                self.g << 16 |
                self.g << 8 |
                self.r << 0
            )

    def __bytes__(self) -> bytes:
        return int(self).to_bytes(4, byteorder)


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

    @classmethod
    def colorscheme(cls, scheme: str) -> dict[str, "Color"]:
        colorscheme: dict[str, dict[str, Color]] = {
            "gruvbox": {
                "bg": cls.from_hex("#1d2021"),
                "fg": cls.from_hex("#ebdbb2"),
                "fg_dim": cls.from_hex("#7c6f64"),
                "red": cls.from_hex("#cc241d"),
                "green": cls.from_hex("#98971a"),
                "blue": cls.from_hex("#458588"),
                "yellow": cls.from_hex("#d79921"),
                "gray1": cls.from_hex("#282828"),
                "gray2": cls.from_hex("#32302f")
            }
        }
        if colorscheme.get(scheme) is not None:
            return colorscheme[scheme]
        else:
            raise ValueError("undefined  colorscheme: " + scheme)
