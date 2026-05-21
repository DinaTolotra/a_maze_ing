class Color:
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        self.r = r 
        self.g = g
        self.b = b
        self.a = a

    def to_int(self) -> int:
        return (
            self.a << 24 |
            self.b << 16 |
            self.g << 8 |
            self.r
        )

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
