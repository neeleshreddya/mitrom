import os
import glob
import json
from bs4 import BeautifulSoup

BLOG_FOLDER = 'blogs'
OUTPUT_FILE = os.path.join(BLOG_FOLDER, 'blogs-list.json')

def extract_blog_info(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    title_tag = soup.find('h1') or soup.title
    title = title_tag.get_text(strip=True) if title_tag else os.path.splitext(os.path.basename(html_path))[0]

    first_p = soup.find('p')
    description = first_p.get_text(" ", strip=True) if first_p else ''

    image_url = ''
    meta_img = soup.find('meta', property='og:image')
    if meta_img and meta_img.get('content'):
        image_url = meta_img['content']
    else:
        img_tag = soup.find('img')
        if img_tag and img_tag.get('src'):
            image_url = img_tag['src']

    filename = os.path.basename(html_path)
    url = f'/{BLOG_FOLDER}/{filename}'

    return {
        "title": title,
        "url": url,
        "description": description,
        "image": image_url
    }

def main():
    blog_files = glob.glob(os.path.join(BLOG_FOLDER, '*.html'))
    blogs = []
    for blog_file in blog_files:
        if os.path.basename(blog_file).lower() == 'blog.html':
            continue  # skip the blog listing page
        blog_info = extract_blog_info(blog_file)
        blogs.append(blog_info)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        json.dump(blogs, f_out, ensure_ascii=False, indent=2)

    print(f"Generated blogs-list.json with {len(blogs)} entries at {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
