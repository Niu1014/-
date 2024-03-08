from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import sys


if len(sys.argv) != 3:
    print("Usage: python3 yourcode.py <date> <currency_code>")
    sys.exit(1)

date = sys.argv[1]
currency_code = sys.argv[2]


driver = webdriver.Chrome(service=Service(r'/Users/nhd2002828/Downloads/chromedriver-mac-arm64 2/chromedriver'))
driver.get("https://www.boc.cn/sourcedb/whpj/")
driver.implicitly_wait(100)

def create_currency_dict(filename):
    currency_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                currency_name = parts[0]
                currency_code = parts[1]
                currency_dict[currency_code] = currency_name
    return currency_dict

currency = create_currency_dict("currency_symbols_filtered.txt")


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pjname"))
    )

    date_input = driver.find_element(By.NAME, "erectDate")
    date_input.clear()
    date_input.send_keys(date)

    date_input1 = driver.find_element(By.NAME, "nothing")
    date_input1.clear()
    date_input1.send_keys(date)

    select = Select(driver.find_element(By.ID, "pjname"))
    select.select_by_visible_text(currency[currency_code])

    search_button = driver.find_elements(By.CLASS_NAME, 'search_btn')[1].click()


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table"]/tbody/tr[2]'))
    )

    buying_rate_first_digit = driver.find_element(By.XPATH, '//table[@class="table"]/tbody/tr[2]/td[5]').text[0]

    with open("result.txt", "w") as file:
        file.write(f"Buying Rate First Digit: {buying_rate_first_digit}")

    print(
         "The first digit of the buying rate is {buying_rate_first_digit}")


except Exception as e:
    print(f"Error occurred")

finally:
    driver.quit()



