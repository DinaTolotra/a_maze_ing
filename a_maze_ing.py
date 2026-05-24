from lib.window import Window, Image, Color, Point


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Key press: [{button}, {x}, {y}]")


if __name__ == "__main__":
    win: Window = Window()
    win_size: Point = Window.get_screen_size()
    win_deco: Image = Window.create_image(win_size)
    scheme: dict[str, Color] = Color.colorscheme("gruvbox")
    win_deco.fill(scheme["bg"])
    win.create_window(win_size, "MLX")
    win.draw_image(win_deco, Point(0, 0))
    win.draw_text(
        "A_MAZE_ING",
        Point(int((win_size.x - len("a_maze_ing") * 11) / 2), 10),
        scheme["fg"])
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.loop()
    win.destroy_window()
