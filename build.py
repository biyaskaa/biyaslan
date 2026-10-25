"""Собирает визитку в статический сайт в папке dist/.

Запуск: python build.py
"""
import hashlib
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
    # Версия файлов для защиты от кеша браузера: меняется при каждой правке.
    digest = hashlib.md5()
    for f in sorted((ROOT / "static").rglob("*")):
        if f.is_file():
            digest.update(f.read_bytes())
    html = env.get_template("index.html").render(p=PROFILE, v=digest.hexdigest()[:8])
    (DIST / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ROOT / "static", DIST / "static")
    (DIST / ".nojekyll").touch()
    print(f"Готово: {DIST / 'index.html'}")


if __name__ == "__main__":
    build()
