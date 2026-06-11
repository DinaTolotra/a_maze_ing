from window import Window, Image
from utils import Point, Color


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        print("Quitting...")
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Mouse press: [{button}, {x}, {y}]")


def create_button(size: Point, text: str,
                  border: Color, bg: Color,
                  fg: Color) -> Image:
    btn: Image
    btn_text: Image

    btn = Window.create_image(size)
    btn_text = Window.load_png("res/" + text + ".png")
    btn.fill(border)
    btn.draw_rect(size - Point(2, 2), Point(1, 1), bg)
    btn_text.replace_color(Color.from_hex("#000000"), bg)
    btn.put_image(btn_text, Point(
        int((size.x - btn_text.size.x) / 2),
        int((size.y - btn_text.size.y) / 2)
    ))
    return btn


def create_memu(scheme: dict[str, Color]) -> Image:
    menu: Image
    btn_start: Image
    btn_about: Image
    btn_quit: Image
    btn_size: Point

    btn_size = Point(200, 50)
    menu = Window.create_image(Point(800, 600))
    btn_start = create_button(btn_size, "start",
                              scheme["yellow"],
                              scheme["bg"],
                              scheme["fg"])
    btn_about = create_button(btn_size, "about",
                              scheme["yellow"],
                              scheme["bg"],
                              scheme["fg"])
    btn_quit = create_button(btn_size, "quit",
                             scheme["yellow"],
                             scheme["bg"],
                             scheme["fg"])
    menu.fill(scheme["bg"])
    menu.put_image(btn_start, Point(300, 200))
    menu.put_image(btn_about, Point(300, 300))
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
