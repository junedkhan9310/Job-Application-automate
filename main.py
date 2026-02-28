import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from AI_Action import ai_answer_these_questions


# =========================================================
# ===================== SETTINGS ==========================
# =========================================================

JOB_SEARCH_URL = "https://www.glassdoor.co.in/Job/index.htm"
WAIT_BETWEEN_APPS = 5
MAX_APPLICATIONS = 20

POSTAL_CODE = "560001"
CITY = "Bangalore"
JOB_TITLE = "Software Engineer"
COMPANY = "random"

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


# =========================================================
# ====================== UTILITIES ========================
# =========================================================

def switch_to_latest_tab(browser):
    """
    Switch focus to the newest opened tab
    """
    browser.switch_to.window(browser.window_handles[-1])


def close_current_tab_and_return(browser):
    """
    Close current tab and switch back to main tab
    """
    browser.close()
    browser.switch_to.window(browser.window_handles[0])


def check_and_fill_experience_page(browser):
    """
    Handles last experience page if detected
    Returns True if page handled, else False
    """
    try:
        if "Enter a job that shows relevant experience" in browser.page_source:
            browser.find_element(By.ID, "job-title-input").send_keys(JOB_TITLE)
            browser.find_element(By.ID, "company-name-input").send_keys(COMPANY)
            return True
        return False
    except:
        return False


def fill_contact_information(browser):
    """
    Fills postal code and city if contact form appears
    Returns True if handled
    """
    try:
        if "Postal code" in browser.page_source:
            browser.find_element(By.ID, "location-fields-postal-code-input").send_keys(POSTAL_CODE)
            browser.find_element(By.ID, "location-fields-locality-input").send_keys(CITY)

            # Click continue button
            browser.find_element(
                By.XPATH,
                '//*[@id="mosaic-provider-module-apply-contact-info"]//button'
            ).click()

            time.sleep(2)

            # Resume selection continue
            browser.find_element(
                By.XPATH,
                '//*[@id="mosaic-provider-module-apply-resume-selection"]//button[last()]'
            ).click()

            time.sleep(2)

            return True

        return False
    except:
        return False


def handle_ai_question_section(browser):
    """
    Detects question section and sends it to AI for answering
    Returns True if questions handled
    """
    try:
        if "Answer these questions" in browser.page_source:
            print("AI answering questions...")
            ai_answer_these_questions(browser)

            browser.find_element(
                By.XPATH,
                '//*[@id="mosaic-provider-module-apply-questions"]//button'
            ).click()

            time.sleep(2)

            return True

        return False
    except:
        return False



def apply_to_jobs(browser):
    """
    Main automation loop:
    - Loads job search page
    - Iterates through job cards
    - Applies using Easy Apply
    - Handles multi-step form
    """

    browser.get(JOB_SEARCH_URL)

    print("Loading job page...")
    time.sleep(5)

    # Scroll to load jobs
    browser.execute_script("window.scrollTo(0, 1000);")
    time.sleep(3)

    job_cards = browser.find_elements(
        By.XPATH,
        "//*[@id='left-column']/div[1]/ul/li"
    )

    print(f"Found {len(job_cards)} job cards")

    applications_done = 0

    for job in job_cards:

        if applications_done >= MAX_APPLICATIONS:
            print("Reached maximum applications limit")
            break

        # Process only Easy Apply jobs
        if "Easy Apply" not in job.text:
            continue

        try:
            job.click()
            time.sleep(3)

            # Click Easy Apply button
            easy_apply_button = browser.find_element(
                By.XPATH,
                '//*[@id="app-navigation"]/div[4]/div/div[2]/div/div[1]/header/div[3]/div/div/div/button'
            )
            easy_apply_button.click()

            time.sleep(3)

            # Switch tab if new tab opened
            if len(browser.window_handles) > 1:
                switch_to_latest_tab(browser)

            # Ensure correct domain
            if "smartapply.indeed.com" not in browser.current_url:
                close_current_tab_and_return(browser)
                continue

            print("Smart Apply page opened")

            # Step 1 - Contact Info
            fill_contact_information(browser)

            # Step 2 - AI Questions
            handle_ai_question_section(browser)

            # Step 3 - Final Experience Page
            check_and_fill_experience_page(browser)

            applications_done += 1
            print(f"Application #{applications_done} completed")

            time.sleep(WAIT_BETWEEN_APPS)

            # Close tab and return
            close_current_tab_and_return(browser)

        except Exception as e:
            print("Error while applying:", e)
            # Safety close
            if len(browser.window_handles) > 1:
                close_current_tab_and_return(browser)
            continue



def main():
    browser = init_driver()
    try:
        apply_to_jobs(browser)
    finally:
        print("Closing browser...")
        browser.quit()


if __name__ == "__main__":
    main()
