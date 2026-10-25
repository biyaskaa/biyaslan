"""Собирает визитку в статический сайт в папке dist/.

Запуск: python build.py
"""
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from profile_data import PROFILE

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    html = env.get_template("index.html").render(p=PROFILE)
    (DIST / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ROOT / "static", DIST / "static")
    (DIST / ".nojekyll").touch()
    print(f"Готово: {DIST / 'index.html'}")


if __name__ == "__main__":
    build()
