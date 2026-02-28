
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException





def init_driver():
    """
    Initialize undetected Chrome driver
    Returns: browser instance
    """
    options = uc.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")

    # Use persistent profile (optional but useful)
    options.add_argument(r"--user-data-dir=C:\profiledata")

    browser = uc.Chrome(
        version_main=144,
        options=options
    )

    return browser


browser = init_driver()


