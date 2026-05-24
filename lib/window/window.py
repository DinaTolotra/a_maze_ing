from typing import Callable, Any
from mlx import Mlx

from .color import Color
from .point import Point
from .image import Image


class Window:
    mlx: Mlx = Mlx()
    mlx_ptr: int = mlx.mlx_init()

    def __init__(self) -> None:
        self._win_ptr: int = 0
        self._key_handler: Callable[[int, "Window"], None] = None
        self._mouse_handler: Callable[[int, int, int, "Window"], None] = None

    @classmethod
    def _check_mlx_ptr(cls) -> None:
        if not cls.mlx_ptr:
            raise RuntimeError("MLX not initialized")

    def _check_win_ptr(self) -> None:
        if not self._win_ptr:
            raise RuntimeError("Window not created")

    def create_window(self, size: Point, title: str) -> None:
        Window._check_mlx_ptr()
        self._win_ptr = Window.mlx.mlx_new_window(
            Window.mlx_ptr, size.x, size.y, title)
        if not self._win_ptr:
            raise RuntimeError("Failed to create window")

    @classmethod
    def get_screen_size(cls) -> Point:
        x: int
        y: int
        (_, x, y) = cls.mlx.mlx_get_screen_size(cls.mlx_ptr)
        return Point(x, y)

    def clear_window(self) -> None:
        Window._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_clear_window(
            Window.mlx_ptr, self._win_ptr)

    def destroy_window(self) -> None:
        Window._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_destroy_window(
            Window.mlx_ptr, self._win_ptr)
        self._win_ptr = 0

    def set_key_handler(
        self,
        key_handler: Callable[[int, "Window"], None]
    ) -> Any:
        self._key_handler = key_handler

    def set_mouse_handler(
        self,
        mouse_handler: Callable[[int, int, int, "Window"], None]
    ) -> None:
        self._mouse_handler = mouse_handler

    def loop(self) -> None:
        Window._check_mlx_ptr()
        self._check_win_ptr()
        if self._key_handler:
            Window.mlx.mlx_key_hook(
                self._win_ptr,
                self._key_handler,
                self)
        if self._mouse_handler:
            Window.mlx.mlx_mouse_hook(
                self._win_ptr,
                self._mouse_handler,
                self)
        Window.mlx.mlx_loop(
            Window.mlx_ptr)

    def loop_exit(self) -> None:
        Window._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_loop_exit(
            Window.mlx_ptr)

    def draw_image(self, image: Image, pos: Point) -> None:
        Window._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_put_image_to_window(
            Window.mlx_ptr, self._win_ptr,
            image.ptr, pos.x, pos.y)
    
    @classmethod
    def create_image(cls, size: Point) -> Image:
        cls._check_mlx_ptr()
        img_ptr: int
        data: memoryview
        bpp: int
        line_len: int
        is_big_indian: bool

        img_ptr = cls.mlx.mlx_new_image(
            cls.mlx_ptr, size.x, size.y)
        (data, bpp, line_len, is_big_indian) = (
            cls.mlx.mlx_get_data_addr(img_ptr))
        return Image(img_ptr, data, bpp, line_len, is_big_indian)
