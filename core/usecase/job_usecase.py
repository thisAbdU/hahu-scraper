from core.repository.job_scraper import JobScraperRepository

class JobUsecase:
    def __init__(self, repository: JobScraperRepository):
        self.repository = repository

    def get_latest_jobs(self):
        return self.repository.fetch_jobs()
