import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}}"
# print(URL)

def extract_indeed_pages():

    result = requests.get(URL)    
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})


    ## page numbers
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    print(pages)
    max_page = pages[-1]
    print(max_page)

    # for n in range(max_page):
    #     print(f"start={n*50}")

    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
        # print(f"&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={0*LIMIT}")    
    soup =  BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for result in results:
        title = result.find("div", {"class": "title"}).find("a")["title"]
        company_anchor = result.find("span", {"class": "company"}).find("a")
        # company_anchor = company.find("a")

        if company_anchor is not None:
            cp_a = str(company_anchor.string)
        else:
            cp_a = str(company_anchor)

        company = cp_a.strip()
        print(company)
    return jobs

    #test