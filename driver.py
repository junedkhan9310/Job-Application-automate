import undetected_chromedriver as uc

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

    browser.maximize_window()
    return browser

