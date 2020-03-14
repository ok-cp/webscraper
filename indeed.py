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

    # print(pages)
    max_page = pages[-1]
    # print(max_page)

    # for n in range(max_page):
    #     print(f"start={n*50}")

    return max_page

def extract_jobs(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    # company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company_anchor)

    company = company.strip()

    job_id = html['data-jk']

    # location = html.find("span",{"class": "location"}).string
    location = html.find("div",{"class": "recJobLoc"})["data-rc-loc"]

    return {
            'title': title, 
            'company': company, 
            'location': location,
            'link': f'https://www.indeed.com/jobs?q=python&limit=50&vjk={job_id}'
            }
    # print(company)



def extract_indeed_jobs(last_page):

    jobs = []

    for page in range(last_page):

        print(f"Scrapping page{page}")

        result = requests.get(f"{URL}&start={page*LIMIT}")    
        soup =  BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job =  extract_jobs(result)
            jobs.append(job)
            # print(job)

    return jobs

    
def  get_jobs():

    last_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_page)

    return  jobs