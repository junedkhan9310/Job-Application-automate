from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.print_exception import print_exception_details
from AI_Action import ai_answer_these_questions
import time

def fill_contact_information(browser,POSTAL_CODE,CITY,wait):
    """
    Fills postal code and city if contact form appears
    Returns True if handled
    """
    try:

        if "Postal code" in browser.page_source:
            # i wanna check if thsoe fields are filled before clicking continue, if not then return False
            postal_code_field = browser.find_element(By.ID, "location-fields-postal-code-input")
            city_field = browser.find_element(By.ID, "location-fields-locality-input")

            if not postal_code_field.get_attribute("value"):
                postal_code_field.send_keys(POSTAL_CODE)
            if not city_field.get_attribute("value"):
                city_field.send_keys(CITY)

            # Click continue button 
            continue_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='continue-button']"))
            )
            continue_button.click()


            time.sleep(10)  # wait for next step to load
            # select already uploaded resumse and continue
            radio = browser.find_element(By.XPATH, '//*[@id=":rf:-input"]')
            browser.execute_script("arguments[0].click();", radio) 

            continue_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='continue-button']"))
            )
            continue_button.click()
            time.sleep(5)
            # You send the file path directly to the file input.
            # file_input = driver.find_element(
            #     By.CSS_SELECTOR,
            #     '[data-testid="resume-selection-file-resume-radio-card-file-input"]'
            # )

            # file_input.send_keys(r"C:\Users\YourName\Desktop\resume.pdf")
            return True

        return False
    except Exception as e:
        print_exception_details(e)
        return False


def handle_ai_question_section(browser,wait):
    """
    Detects question section and sends it to AI for answering
    Returns True if questions handled
    """
    try:
        if "Answer these questions" in browser.page_source:
            print("AI answering questions...")
            ai_answer_these_questions(browser)

            continue_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[data-testid='continue-button']")
                )
            )
            continue_button.click()

            # Wait for the next page step to load
            wait.until(EC.staleness_of(continue_button))

            return True
        else:
            return True  # No AI questions, but still a successful handling

    except Exception as e:
        print_exception_details(e)
        return False



def check_and_fill_experience_page(browser,JOB_TITLE,COMPANY):
    """
    Handles last experience page if detected
    Returns True if page handled, else False
    """
    try:
        time.sleep(10)
        if "Enter a job that shows relevant experience" in browser.page_source:
            browser.find_element(By.ID, "job-title-input").send_keys(JOB_TITLE)
            browser.find_element(By.ID, "company-name-input").send_keys(COMPANY)
            return True
        return False
    except Exception as e:
        print_exception_details(e)
        return False
