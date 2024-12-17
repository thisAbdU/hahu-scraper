from django.http import JsonResponse
from core.repository.job_scraper import JobScraperRepository
from core.usecase.job_usecase import JobUsecase

def job_list_view(request):
    # Initialize repository and usecase
    repository = JobScraperRepository()
    usecase = JobUsecase(repository)

    # Fetch jobs
    jobs = usecase.get_latest_jobs()

    # Convert JobPost objects to JSON
    job_data = [
        {
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "posted_date": job.posted_date,
            "job_url": job.job_url,
        }
        for job in jobs
    ]

    return JsonResponse({"jobs": job_data})
