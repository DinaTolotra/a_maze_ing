from lib.window import Window, Color, Point


def key_handler(keynum: int, win: Window) -> None:
    win.clear_window()
    if chr(keynum) == "q":
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Key press: [{button}, {x}, {y}]")


if __name__ == "__main__":
    win: Window = Window()
    win.create_window(Point(800, 600), "MLX")
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.loop()
    win.destroy_window()
