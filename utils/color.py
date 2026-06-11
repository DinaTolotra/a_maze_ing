from sys import byteorder


class Color:
    colorscheme_list: dict[str, dict[str, "Color"]] = {}

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
        if byteorder == "big":
            return int(
                self.r << 24 |
                self.g << 16 |
                self.b << 8 |
                self.a << 0
            )
        else:
            return int(
                self.a << 24 |
                self.r << 16 |
                self.g << 8 |
                self.b << 0
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
    def load_colorscheme(cls) -> None:
        colorscheme: dict[str, Color]
        colorscheme_name_list: list[str] = []
        color_class: str
        color_value: str

        with open("res/color/color.txt") as lst_file:
            for scheme_name in lst_file:
                colorscheme_name_list.append(scheme_name.strip())
        for scheme_name in colorscheme_name_list:
            with open("res/color/" + scheme_name + ".txt") as scheme_file:
                colorscheme = {}
                for line in scheme_file:
                    color_class, color_value = line.split(":")
                    color_class = color_class.strip()
                    color_value = color_value.strip()
                    colorscheme[color_class] = cls.from_hex(color_value)
                cls.colorscheme_list[scheme_name] = colorscheme

    @classmethod
    def colorscheme(cls, scheme: str) -> dict[str, "Color"]:
        if cls.colorscheme_list.get(scheme) is not None:
            return cls.colorscheme_list[scheme]
        else:
            raise ValueError("undefined  colorscheme: " + scheme)