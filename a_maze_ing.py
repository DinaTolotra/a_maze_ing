from lib.window import Window, Image, Color, Point


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        print("Quitting...")
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Key press: [{button}, {x}, {y}]")


def set_window_deco(
    win: Window, size: Point, scheme: dict[str, Color]
) -> None:
    win_deco: Image
    title_pos: Point
    title: str
    key_map: list[tuple[str, str]]

    title = "A_MAZE_ING"
    key_map = [
        ("q", "quit"),
        ("r", "restart"),
        ("t", "theme")
    ]
    title_pos = Point(
        int((size.x - len(title) * 11) / 2), 20)
    win_deco = Window.create_image(size)
    win_deco.fill(scheme["bg"])
    win_deco.draw_rect(Point(size.x - 20, 50), Point(10, 10), scheme["fg"])
    win_deco.draw_rect(Point(size.x - 22, 48), Point(11, 11), scheme["bg"])
    win_deco.draw_rect(
        Point(size.x - 20, size.y - 40),
        Point(10, 60), scheme["gray1"])
    win.draw_image(win_deco, Point(0, 0))
    win.draw_text(
        title,
        title_pos,
        scheme["fg"])
    for key, i in zip(key_map, range(len(key_map))):
        win.draw_text(
            f"{key[0]}:",
            Point(10 + 11 * 15 * i, size.y - 30),
            scheme["fg"])
        win.draw_text(
            key[1],
            Point(3 * 11 + 10 + 11 * 15 * i, size.y - 30),
            scheme["fg_dim"])
    return win_deco


if __name__ == "__main__":
    win: Window = Window()
    win_size: Point = Point(800, 600)
    scheme: dict[str, Color] = Color.colorscheme("gruvbox")
    win.create_window(win_size, "MLX")
    set_window_deco(win, win_size, scheme)
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.loop()
    win.destroy_window()
