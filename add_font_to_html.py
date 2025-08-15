import glob

font_links = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
"""

html_files = glob.glob('*.html') + glob.glob('*/**/*.html', recursive=True)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if font link is already present
    if "fonts.googleapis.com/css2?family=Libre+Baskerville" in content:
        continue

    # Insert font links after <head> tag
    if "<head>" in content:
        updated_content = content.replace("<head>", "<head>\n" + font_links)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Font link added to: {filename}")
