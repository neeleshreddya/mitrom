import os
import glob
import json
from bs4 import BeautifulSoup

JOB_FOLDER = 'jobs'
OUTPUT_FILE = os.path.join(JOB_FOLDER, 'jobs-list.json')

def extract_job_info(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Get title – try h1, h2, or title tag
    title_tag = soup.find('h1') or soup.find('h2') or soup.title
    title = title_tag.get_text(strip=True) if title_tag else os.path.splitext(os.path.basename(html_path))[0]

    # URL relative to site root
    url = '/' + html_path.replace(os.path.sep, '/')

    return {"title": title, "url": url}

def main():
    job_files = glob.glob(f'{JOB_FOLDER}/*.html')
    jobs = []
    for job_file in job_files:
        if os.path.basename(job_file).lower() in ('index.html', 'jobs-list.json'):
            continue
        job_info = extract_job_info(job_file)
        jobs.append(job_info)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        json.dump(jobs, f_out, ensure_ascii=False, indent=2)

    print(f"Generated jobs list JSON with {len(jobs)} entries at: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
