_ROOT = Path(__file__).resolve().parent / "ui"
 import base64


def stylesheet():
    css = (_ROOT / "shell.css").read_text(encoding="utf-8")
    font = _ROOT / "Syne-Variable.ttf"
    if font.is_file():
        data = base64.b64encode(font.read_bytes()).decode("ascii")
        css += '\n@font-face{font-family:"Applio Syne";font-style:normal;font-weight:400 800;font-display:swap;src:url(data:font/ttf;base64,' + data + ') format("truetype");}'
    for key, svg in _ICONS.items():
        css += f'\n.applio-nav-{key}::before,.applio-link-{key}::before{{mask-image:url("data:image/svg+xml,{quote(svg)}");}}'
    return css

