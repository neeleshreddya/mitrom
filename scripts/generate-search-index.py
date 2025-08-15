import os
import json
from bs4 import BeautifulSoup

# List of folders to scan (your existing content folders)
FOLDERS = ['about', 'disclaimer', 'forms', 'jobs', 'privacypolicy']

OUTPUT_FILE = '../search-index.json'  # Go up one level to root

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        body = soup.body.get_text(separator=' ', strip=True) if soup.body else ''
        snippet = body[:300]
    return title, snippet

def main():
    pages = []
    for folder in FOLDERS:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.html'):
                    full_path = os.path.join(root, file)
                    url_path = '/' + full_path.replace(os.path.sep, '/')
                    title, snippet = extract_text_from_html(full_path)
                    pages.append({
                        "title": title,
                        "url": url_path,
                        "content": snippet,
                        "snippet": snippet
                    })

    # Write search-index.json in root folder
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)

    print(f"Search index generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
