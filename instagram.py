import requests
from bs4 import BeautifulSoup

# Global variable
# Set URL 
LIMIT = 50
URL = "https://www.instagram.com/jobs?q=python&limit={LIMIT}}"


# Get Page Number in Navigator(html class)
def extract_indeed_pages(): 

    result = requests.get(URL)    
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})


    ## page numbers
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

# Get Job Info(title, company, location, link)
def extract_jobs(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company_anchor)

    company = company.strip()

    job_id = html['data-jk']
    location = html.find("div",{"class": "recJobLoc"})["data-rc-loc"]

    return {
            'title': title, 
            'company': company, 
            'location': location,
            'link': f'https://www.indeed.com/jobs?q=python&limit=50&vjk={job_id}'
            }


# Extract Job List
def extract_indeed_jobs(last_page):

    jobs = []
    print(f"Last Page is {last_page}")
    for page in range(last_page):

        print(f"Scrapping page{page}")

        result = requests.get(f"{URL}&start={page*LIMIT}")    
        soup =  BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job =  extract_jobs(result)
            jobs.append(job)

    return jobs




# Get Job Descriptions    
def  get_jobs_des():

    last_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(2)
    # jobs = extract_indeed_jobs(last_page)
    return  jobs