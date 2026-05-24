from .point import Point
from .color import Color


class Image:
    def __init__(self, ptr: int, data: memoryview,
                 bpp: int, line_len: int, is_big_endian: bool
                 ) -> None:
        if ptr == 0:
            raise ValueError(
                "invalid image pointer: " +
                str(ptr) + "\n" +
                "use Window.create_image")
        self._ptr: int = ptr
        self._data: memoryview
        self._bpp: int
        self._line_len: int
        self._is_big_endian: bool

        self.data = data
        self.bpp = bpp
        self.line_len = line_len
        self.is_big_endian = is_big_endian

    @property
    def ptr(self) -> int:
        return self._ptr

    @property
    def data(self) -> memoryview:
        return self._data

    @data.setter
    def data(self, value: memoryview) -> None:
        self._data = value

    @property
    def bpp(self) -> int:
        return self._bpp

    @bpp.setter
    def bpp(self, value: int) -> None:
        if value <= 0:
            raise ValueError(
                "invalid bit per pixel value(bpp): " +
                str(value))
        self._bpp = value

    @property
    def line_len(self) -> int:
        return self._line_len

    @line_len.setter
    def line_len(self, value: int) -> None:
        if value <= 0:
            raise ValueError(
                "invalid line length value: " +
                str(value))
        self._line_len = value

    @property
    def is_big_endian(self) -> bool:
        return self._is_big_endian

    @is_big_endian.setter
    def is_big_endian(self, value: bool) -> None:
        self._is_big_endian = value

    def draw_pixel(self, pos: Point, color: Color) -> None:
        index: int = (pos.x * 4 + pos.y * self.line_len)
        self.data[index:index + 4] = memoryview(
            color.to_int(self.is_big_endian).to_bytes(4, 'little'))

    def draw_rect(self, size: Point, pos: Point, color: Color) -> None:
        index: int
        for y in range(pos.y, size.y):
            index = (pos.x * 4 + y * self.line_len)
            self.data[index:index + 4 * size.x] = memoryview(bytes(
                (color.to_int(self.is_big_endian).to_bytes(4, 'little')) *
                size.x))

    def fill(self, color: Color) -> None:
        self.data[:] = memoryview(bytes(
            (color.to_int(self.is_big_endian).to_bytes(4, 'little')) *
            int(len(self.data) / 4)))
