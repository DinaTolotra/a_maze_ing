# a_maze_ing

Small terminal/GUI maze project written in Python. Provides maze model,
view rendering, and simple windowing utilities.

## Description

- Minimal, educational project to generate and display mazes.
- Uses a small custom window/image wrapper and color themes in `res/`.

## Features

- Maze generation and representation (`maze/model.py`).
- Rendering layers and color themes (`maze/view.py`, `res/color`).
- Lightweight window/image helpers in `window/`.

## Requirements

- Python 3.10+ (virtualenv recommended)
- Optional: `mlx-2.2-py3-none-any.whl` for macOS-like windowing if used.

## Install

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install any needed wheel or deps (if applicable):

```bash
pip install ./mlx-2.2-py3-none-any.whl
```

## Run

From project root with the venv activated:

```bash
python a_maze_ing.py
```

## Project Structure

- `a_maze_ing.py` — entrypoint
- `maze/` — model and view
- `window/` — window and image helpers
- `res/` — color themes
- `utils/` — small utilities (`point.py`, `color.py`)

## Author

- todina-r <todina-r@student.42antananarivo.mg>

## License

Public domain / permissive for educational use.
