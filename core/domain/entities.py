from dataclasses import dataclass

@dataclass
class JobPost:
    title: str
    company: str
    location: str
    posted_date: str
    job_url: str
