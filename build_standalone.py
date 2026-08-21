from pathlib import Path

html = Path("index.html").read_text()
base = "https://sjwross.github.io/pawsofkilmacolm"

for old, new in [
    ('href="assets/', f'href="{base}/assets/'),
    ('src="assets/', f'src="{base}/assets/'),
    ("'media/", f"'{base}/media/"),
    ('"media/', f'"{base}/media/'),
    ("`media/", f"`{base}/media/"),
    ('data-photo="media/', f'data-photo="{base}/media/'),
]:
    html = html.replace(old, new)

Path("preview-standalone.html").write_text(html)
print("updated preview-standalone.html", len(html))
