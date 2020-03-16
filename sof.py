import requests
from bs4 import BeautifulSoup


URL = "https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages =  soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    # print(last_page)
    return int(last_page)

def extract_job(html):
    return


def extract_jobs(last_page):
    jobs = []
    for page in last_page:
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
        return jobs
            

def get_jobs():
    last_page = get_last_page()
    return last_page


