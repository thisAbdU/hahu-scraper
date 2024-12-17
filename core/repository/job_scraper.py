import requests
from bs4 import BeautifulSoup
from core.domain.entities import JobPost

class JobScraperRepository:
    BASE_URL = "https://hahu.jobs/"

    def fetch_jobs(self) -> list[JobPost]:
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            job_posts = []
    
            for job in soup.find_all('div', class_='job-card'):  
                title = job.find('h2').text.strip()
                company = job.find('span', class_='company').text.strip()
                location = job.find('span', class_='location').text.strip()
                posted_date = job.find('span', class_='date').text.strip()
                job_url = job.find('a')['href']

                job_posts.append(
                    JobPost(title, company, location, posted_date, self.BASE_URL + job_url)
                )

            return job_posts

        except requests.RequestException as e:
            print(f"Error fetching jobs: {e}")
            return []
