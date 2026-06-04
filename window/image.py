from utils import Point, Color


class Image:
    def __init__(self, ptr: int, size: Point,
                 data: memoryview, bpp: int,
                 line_len: int) -> None:
        if ptr == 0:
            raise ValueError("invalid image pointer: " + str(ptr))
        self._ptr: int
        self._data: memoryview
        self._bpp: int
        self._line_len: int
        self._size: Point

        self._ptr = ptr
        self._data = data
        self._bpp = bpp
        self._line_len = line_len
        self._size = size

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
    
    @property
    def size(self) -> Point:
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

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
        self.data[:] = memoryview(bytes((raw_color) * bit_count))

    def put_image(self, img: "Image", pos: Point) -> None:
        byte_per_pixel: int
        src_index: int
        dst_index: int
        src_end: int
        dst_end: int

        byte_per_pixel = int(self.bpp / 8)
        for y in range(img.size.y):
            src_index = y * img.line_len
            src_end = src_index + img.line_len
            dst_index = pos.x * byte_per_pixel + (pos.y + y) * self.line_len
            dst_end = dst_index + min(img.line_len, self.line_len)
            self.data[dst_index:dst_end] = img.data[src_index:src_end]
