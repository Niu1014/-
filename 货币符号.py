from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r'/Users/nhd2002828/Downloads/chromedriver-mac-arm64 2/chromedriver'))

try:
    driver.get('https://www.11meigui.com/tools/currency')

    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    with open('currency_symbols_filtered.txt', 'w', encoding='utf-8') as file:
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 5:
                currency_name = cols[1].text.strip()
                currency_symbol = cols[4].text.strip()
                file.write(f"{currency_name} {currency_symbol}\n")

    print("Filtered currency symbols have been successfully saved to currency_symbols_filtered.txt")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


