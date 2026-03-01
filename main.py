from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from utils.driver import init_driver
from selenium.webdriver.support.ui import WebDriverWait
import time


from form_fill_action import check_and_fill_experience_page, fill_contact_information, handle_ai_question_section
from utils.print_exception import print_exception_details
from config import Config


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






def apply_to_jobs(browser):
    """
    Main automation loop:
    - Loads job search page
    - Iterates through job cards
    - Applies using Easy Apply
    - Handles multi-step form
    """
    try:
        wait = WebDriverWait(browser, 15)
        browser.get(Config.JOB_SEARCH_URL)
        print("Loading job page...")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='left-column']/div[1]/ul/li")
            )
        )
        # Count initial jobs
        initial_count = len(browser.find_elements(By.XPATH,"//*[@id='left-column']/div[1]/ul/li"))

        # Scroll to load more
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for more jobs to load
        wait.until(lambda d: len(d.find_elements(By.XPATH,"//*[@id='left-column']/div[1]/ul/li")) > initial_count)

        job_cards = browser.find_elements(By.XPATH,"//*[@id='left-column']/div[1]/ul/li")

        print(f"Found {len(job_cards)} job cards")
        applications_done = 0

        for job in job_cards:
            try:
                if applications_done >= Config.MAX_APPLICATIONS:
                    print("Reached maximum applications limit")
                    break

                # Process only Easy Apply jobs
                if "Easy Apply" not in job.text:
                    continue

                try:
                    job.click()
                    easy_apply_button = wait.until(EC.element_to_be_clickable((
                            By.XPATH,
                            '//*[@id="app-navigation"]/div[4]/div/div[2]/div/div[1]/header/div[3]/div/div/div/button'
                        ))
                    )
                    easy_apply_button.click()
                    time.sleep(10)

                    # Switch tab if new tab opened
                    if len(browser.window_handles) > 1:
                        switch_to_latest_tab(browser)

                    # Ensure correct domain
                    if "smartapply.indeed.com" not in browser.current_url:
                        close_current_tab_and_return(browser)
                        continue

                    print("Smart Apply page opened")

                    # Step 1 - Contact Info
                    filled_contact_info  = fill_contact_information(browser,Config.POSTAL_CODE,Config.CITY,wait)
                    if not filled_contact_info:
                        print("Failed to fill contact information")
                        close_current_tab_and_return(browser)
                        continue

                    # Step 2 - AI Questions
                    filled_ai_questions = handle_ai_question_section(browser,wait)
                    if not filled_ai_questions:
                        print("Failed to handle AI questions")
                        close_current_tab_and_return(browser)
                        continue

                    # Step 3 - Final Experience Page
                    experienced_page_filled = check_and_fill_experience_page(browser,Config.JOB_TITLE,Config.COMPANY)
                    if not experienced_page_filled:
                        print("Failed to handle experience page")
                        close_current_tab_and_return(browser)
                        continue

                    applications_done += 1
                    print(f"Application #{applications_done} completed")

                    time.sleep(Config.WAIT_BETWEEN_APPS)

                    # Close tab and return
                    close_current_tab_and_return(browser)

                except Exception as e:
                    print_exception_details(e)
                    # Safety close
                    if len(browser.window_handles) > 1:
                        close_current_tab_and_return(browser)
                    continue

            except Exception as e:
                print_exception_details(e)
                continue
    except Exception as e:
        print_exception_details(e)

def main():
    browser = init_driver()
    try:
        apply_to_jobs(browser)
    finally:
        print("Closing browser...")
        browser.quit()


if __name__ == "__main__":
    main()
