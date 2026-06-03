from window import Window, Image
from maze import Cell, MazeModel
from utils import Point, Color
from maze import get_view


def key_handler(keynum: int, win: Window) -> None:
    if chr(keynum) == "q":
        print("Quitting...")
        win.loop_exit()


def mouse_handler(button: int, x: int, y: int, win: Window) -> None:
    print(f"Mouse press: [{button}, {x}, {y}]")


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
        Point(size.x - 20, size.y - 110),
        Point(10, 70), scheme["gray1"])
    win.draw_image(win_deco, Point(0, 0))
    win.draw_text(
        title,
        title_pos,
        scheme["fg"])
    for i, key in enumerate(key_map):
        win.draw_text(
            f"{key[0]}:",
            Point(10 + 11 * 15 * i, size.y - 30),
            scheme["fg"])
        win.draw_text(
            key[1],
            Point(3 * 11 + 10 + 11 * 15 * i, size.y - 30),
            scheme["fg_dim"])


def draw_maze(win: Window, maze: MazeModel, size: int, color: Color) -> None:
    cell_view: dict[Cell, Image]
    img: Image

    cell_view = get_view(size, 4, color)
    for x in range(maze.size.x):
        for y in range(maze.size.y):
            img = cell_view[maze.get(Point(x, y))]
            win.draw_image(img, Point(10 + x * size, 70 + y * size))


def test_maze(win: Window, color: Color) -> None:
    maze: MazeModel

    maze = MazeModel(Point(3, 3))
    maze.set(Point(0, 0), Cell(True, False, False, True))
    maze.set(Point(1, 0), Cell(True, True, True, False))
    maze.set(Point(0, 1), Cell(False, False, True, True))
    maze.set(Point(1, 1), Cell(True, True, True, False))
    draw_maze(win, maze, 50, color)


if __name__ == "__main__":
    win: Window = Window()
    win_size: Point = Point(800, 600)
    scheme: dict[str, Color] = Color.colorscheme("gruvbox")

    win.create_window(win_size, "MLX")
    set_window_deco(win, win_size, scheme)
    test_maze(win, scheme["fg"])
    win.set_key_handler(key_handler)
    win.set_mouse_handler(mouse_handler)
    win.loop()
    win.destroy_window()
