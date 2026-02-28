import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JOB_SEARCH_URL = os.getenv("JOB_SEARCH_URL")
    WAIT_BETWEEN_APPS = int(os.getenv("WAIT_BETWEEN_APPS", 5))
    MAX_APPLICATIONS = int(os.getenv("MAX_APPLICATIONS", 5))
    POSTAL_CODE = os.getenv("POSTAL_CODE")
    CITY = os.getenv("CITY")
    JOB_TITLE = os.getenv("JOB_TITLE")
    COMPANY = os.getenv("COMPANY")