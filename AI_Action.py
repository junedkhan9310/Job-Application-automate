from selenium.webdriver.common.by import By

from gpt_main import new_chatgpt_chat_withID, new_chatgpt_chat_withID_for_drop_down

Question_Data = []
drop_down_data = []

def total_questions(browser):
    Question_Data.clear()
    drop_down_data.clear()

    for i in range(0, 100):
        try:
            base_xpath = f'//*[@id="q_{i}"]'
            question_container = browser.find_element(By.XPATH, base_xpath)

            # Get question text (label)
            try:
                q_text = browser.find_element(
                    By.XPATH, f'{base_xpath}/div/label'
                ).text.strip()
            except:
                q_text = question_container.text.strip()

            # ✅ Check if dropdown exists
            select_elements = browser.find_elements(
                By.XPATH, f'{base_xpath}//select'
            )

            if select_elements:
                select_element = select_elements[0]

                # Extract dropdown options
                options = select_element.find_elements(By.TAG_NAME, "option")
                option_texts = [
                    opt.text.strip() for opt in options if opt.text.strip()
                ]

                drop_down_data.append({
                    "Q_text": q_text,
                    "Q_input": f'{base_xpath}//select',
                    "options": ",".join(option_texts)
                })

                continue  # Skip normal question logic if dropdown

            # ✅ Normal text input question
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
            print(e)
            break


def ai_answer_these_questions(browser):

    total_questions(browser)
    print("Questions extracted:", Question_Data)
    print("Dropdown extracted:", drop_down_data)

    # ✅ Answer normal text questions
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
            print("Text Question Error:", e)

    # ✅ Handle dropdown questions
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
            print("Dropdown Error:", e)

    print("Question tab done")
