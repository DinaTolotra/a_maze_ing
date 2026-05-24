from lib.window import Window, Image, Color, Point
from lib.window import colorscheme


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Key press: [{button}, {x}, {y}]")


if __name__ == "__main__":
    win: Window = Window()
    win_size: Point = Window.get_screen_size()
    win_deco: Image = Window.create_image(win_size)
    scheme: dict[str, Color] = colorscheme["gruvbox"]
    win.create_window(win_size, "MLX")
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win_deco.fill(scheme["bg"])
    win.draw_image(win_deco, Point(0, 0))
    win.loop()
    win.destroy_window()
