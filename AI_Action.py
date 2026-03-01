from selenium.webdriver.common.by import By

from utils.print_exception import print_exception_details
from gpt_main import new_chatgpt_chat_withID, new_chatgpt_chat_withID_for_drop_down

Question_Data = []
drop_down_data = []
radio_button_data = []   # ✅ NEW


def total_questions(browser):
    Question_Data.clear()
    drop_down_data.clear()
    radio_button_data.clear()   # ✅ NEW

    for i in range(0, 100):
        try:
            base_xpath = f'//*[@id="q_{i}"]'
            question_container = browser.find_element(By.XPATH, base_xpath)

            # Get question text
            try:
                q_text = browser.find_element(
                    By.XPATH, f'{base_xpath}/div/label'
                ).text.strip()
            except:
                q_text = question_container.text.strip()

            # -------------------------
            # ✅ CHECK DROPDOWN
            # -------------------------
            select_elements = browser.find_elements(
                By.XPATH, f'{base_xpath}//select'
            )

            if select_elements:
                select_element = select_elements[0]

                options = select_element.find_elements(By.TAG_NAME, "option")
                option_texts = [
                    opt.text.strip() for opt in options if opt.text.strip()
                ]

                drop_down_data.append({
                    "Q_text": q_text,
                    "Q_input": f'{base_xpath}//select',
                    "options": ",".join(option_texts)
                })

                continue  # skip other logic


            # -------------------------
            # ✅ CHECK RADIO BUTTON
            # -------------------------
            radio_elements = browser.find_elements(
                By.XPATH, f'{base_xpath}//input[@type="radio"]'
            )

            if radio_elements:

                option_labels = browser.find_elements(
                    By.XPATH,
                    f'{base_xpath}//input[@type="radio"]/following-sibling::span//span'
                )

                option_texts = [
                    opt.text.strip() for opt in option_labels if opt.text.strip()
                ]

                radio_button_data.append({
                    "Q_text": q_text,
                    "Q_input": f'{base_xpath}//input[@type="radio"]',
                    "options": ",".join(option_texts)
                })

                continue  # skip normal input logic


            # -------------------------
            # ✅ NORMAL TEXT INPUT
            # -------------------------
            try:
                text_limit = browser.find_element(
                    By.XPATH,
                    f'{base_xpath}/div/div[2]/span[1]/span'
                ).get_attribute('innerHTML')
            except:
                text_limit = ""

            Question_Data.append({
                "Q_text": q_text,
                "Q_input": f'{base_xpath}//input | {base_xpath}//textarea',
                "Q_text_limit": text_limit
            })

        except Exception as e:
            print_exception_details(e)
            break


def ai_answer_these_questions(browser):

    total_questions(browser)

    # -------------------------
    # ✅ ANSWER TEXT QUESTIONS
    # -------------------------
    for data in Question_Data:
        try:
            gpt_response = new_chatgpt_chat_withID(
                data['Q_text'],
                data['Q_text_limit']
            )

            if not gpt_response:
                continue

            answer_input = browser.find_element(By.XPATH, data['Q_input'])
            answer_input.clear()
            answer_input.send_keys(str(gpt_response).strip())

        except Exception as e:
            print_exception_details(e)

    # -------------------------
    # ✅ HANDLE DROPDOWNS
    # -------------------------
    for drop_down in drop_down_data:
        try:
            gpt_response = new_chatgpt_chat_withID_for_drop_down(
                drop_down['Q_text'],
                drop_down['options']
            )

            if not gpt_response:
                continue

            select_element = browser.find_element(By.XPATH, drop_down['Q_input'])
            options = select_element.find_elements(By.TAG_NAME, "option")

            for opt in options:
                if opt.text.strip().lower() == str(gpt_response).strip().lower():
                    opt.click()
                    break

        except Exception as e:
            print_exception_details(e)

    # -------------------------
    # ✅ HANDLE RADIO BUTTONS
    # -------------------------
    for radio in radio_button_data:
        try:
            gpt_response = new_chatgpt_chat_withID_for_drop_down(
                radio['Q_text'],
                radio['options']
            )

            if not gpt_response:
                continue

            radio_elements = browser.find_elements(By.XPATH, radio['Q_input'])

            for element in radio_elements:
                try:
                    label_text = element.find_element(
                        By.XPATH, './following-sibling::span//span'
                    ).text.strip()

                    if label_text.lower() == str(gpt_response).strip().lower():
                        element.click()
                        break
                except:
                    continue

        except Exception as e:
            print_exception_details(e)

    print("Question tab done")