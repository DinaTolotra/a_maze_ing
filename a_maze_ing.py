from window import Window, Image
from maze import Cell, MazeModel
from utils import Point, Color

import sys


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        print("Quitting...")
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Mouse press: [{button}, {x}, {y}]")


def create_memu(scheme: dict[str, Color]) -> Image:
    menu: Image
    btn_start: Image
    btn_option: Image
    btn_quit: Image
    btn_size: Point

    btn_size = Point(200, 50)
    menu = Window.create_image(Point(800, 600))
    btn_start = Window.create_image(btn_size)
    btn_option = Window.create_image(btn_size)
    btn_quit = Window.create_image(btn_size)
    menu.fill(scheme["bg"])
    btn_start.fill(scheme["yellow"])
    btn_option.fill(scheme["yellow"])
    btn_quit.fill(scheme["yellow"])
    btn_start.draw_rect(btn_size - Point(2, 2), Point(1, 1), scheme["bg"])
    btn_option.draw_rect(btn_size - Point(2, 2), Point(1, 1), scheme["bg"])
    btn_quit.draw_rect(btn_size - Point(2, 2), Point(1, 1), scheme["bg"])
    menu.put_image(btn_start, Point(300, 200))
    menu.put_image(btn_option, Point(300, 300))
    menu.put_image(btn_quit, Point(300, 400))
    return menu


if __name__ == "__main__":
    win: Window
    win_size: Point
    scheme: dict[str, Color]

    win = Window()
    win_size = Point(800, 600)
    scheme = Color.colorscheme("gruvbox")
    win.create_window(win_size, "MLX")
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.draw_image(create_memu(scheme), Point(0, 0))
    win.loop()
    win.destroy_window()
