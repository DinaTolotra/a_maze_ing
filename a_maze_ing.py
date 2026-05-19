from typing import Callable, Any
from mlx import Mlx


class Window:
    mlx: Mlx = Mlx()
    mlx_ptr: int = mlx.mlx_init()

    def __init__(self) -> None:
        self._win_ptr: int = 0
        self._key_handler: Callable[[int, "Window"], None] = None
        self._mouse_handler: Callable[[int, int, int, "Window"], None] = None

    def _check_mlx_ptr(self) -> None:
        if not Window.mlx_ptr:
            raise RuntimeError("MLX not initialized")

    def _check_win_ptr(self) -> None:
        if not self._win_ptr:
            raise RuntimeError("Window not created")

    def create_window(self, size: tuple[int, int], title: str) -> None:
        self._check_mlx_ptr()
        self._win_ptr = Window.mlx.mlx_new_window(
            Window.mlx_ptr, size[0], size[1], title)
        if not self._win_ptr:
            raise RuntimeError("Failed to create window")

    def clear_window(self) -> None:
        self._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_clear_window(
            Window.mlx_ptr, self._win_ptr)

    def destroy_window(self) -> None:
        self._check_mlx_ptr()
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
        self._check_mlx_ptr()
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
        self._check_mlx_ptr()
        self._check_win_ptr()
        Window.mlx.mlx_loop_exit(
            Window.mlx_ptr)


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Key press: [{button}, {x}, {y}]")


if __name__ == "__main__":
    win: Window = Window()
    win.create_window((800, 600), "MLX")
    win.clear_window()
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.loop()
    win.destroy_window()
