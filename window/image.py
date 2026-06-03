from utils import Point, Color


class Image:
    def __init__(self, ptr: int, data: memoryview,
                 bpp: int, line_len: int) -> None:
        if ptr == 0:
            raise ValueError("invalid image pointer: " + str(ptr))
        self._ptr: int = ptr
        self._data: memoryview
        self._bpp: int
        self._line_len: int

        self._data = data
        self._bpp = bpp
        self._line_len = line_len

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def data(self) -> memoryview:
        return self._data

    @property
    def bpp(self) -> int:
        return self._bpp

    @property
    def line_len(self) -> int:
        return self._line_len

    def draw_pixel(self, pos: Point, color: Color) -> None:
        byte_per_pixel: int
        index: int

        byte_per_pixel = int(self.bpp / 8)
        index = pos.x * byte_per_pixel + pos.y * self.line_len
        self._data[index:index + byte_per_pixel] = memoryview(
            bytes(color))

    def draw_rect(self, size: Point, pos: Point, color: Color) -> None:
        byte_per_pixel: int
        raw_color: bytes
        index: int
        end: int

        raw_color = bytes(color)
        byte_per_pixel = int(self.bpp / 8)
        for y in range(pos.y, pos.y + size.y):
            index = (pos.x * byte_per_pixel + y * self.line_len)
            end = index + byte_per_pixel * size.x
            self.data[index:end] = memoryview(bytes((raw_color) * size.x))

    def fill(self, color: Color) -> None:
        byte_per_pixel: int
        raw_color: bytes
        bit_count: int

        raw_color = bytes(color)
        byte_per_pixel = int(self.bpp / 8)
        bit_count = int(len(self.data) / byte_per_pixel)
        self.data[:] = memoryview(bytes(raw_color) * bit_count)
