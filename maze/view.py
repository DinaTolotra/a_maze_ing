from window import Image, Window
from utils import Point, Color
from .model import Cell


def draw_h(img: Image, pos: Point, length: int,
           width: int, color: Color) -> None:
    img.draw_rect(Point(length, width), pos, color)


def draw_v(img: Image, pos: Point, length: int,
           width: int, color: Color) -> None:
    img.draw_rect(Point(width, length), pos, color)


def get_view(cell_size: int, border_width: int,
             color: Color) -> dict[Cell, Image]:
    comb_list: list[tuple[bool, bool, bool, bool]]
    cell_view: dict[Cell, Image] = dict()
    image: Image
    cell: Cell

    comb_list = [
        (n, e, s, w)
        for w in [True, False]
        for s in [True, False]
        for e in [True, False]
        for n in [True, False]
    ]
    for comb in comb_list:
        cell = Cell(*comb)
        image = Window.create_image(Point(cell_size, cell_size))
        image.draw_rect(Point(cell_size, cell_size),
                        Point(0, 0), Color(0, 0, 0, 0))
        if cell.n:
            draw_h(image, Point(0, 0), cell_size,
                   border_width, color)
        if cell.e:
            draw_v(image, Point(cell_size - border_width, 0),
                   cell_size, border_width, color)
        if cell.s:
            draw_h(image, Point(0, cell_size - border_width),
                   cell_size, border_width, color)
        if cell.w:
            draw_v(image, Point(0, 0), cell_size,
                   border_width, color)
        cell_view[cell] = image
    return cell_view
