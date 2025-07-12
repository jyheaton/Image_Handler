import marimo

app = marimo.App()

with app.setup:
    import sys
    import marimo as mo
    from pathlib import Path

    notebook_dir = mo.notebook_dir() if mo.running_in_notebook() else Path(__file__).parent
    src_dir = (notebook_dir / "../src").resolve()
    sys.path.insert(0, str(src_dir))
    import dedup

@app.cell
def _():
    ui_mod = mo.plain_text(f"Hello world from {dedup.__name__!r} version {dedup.__version__!r}")
    ui_mod


if __name__ == "__main__":
    # print(dedup)

    app.run()