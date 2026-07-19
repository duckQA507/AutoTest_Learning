from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 1. Открываем Википедию
driver.get("https://ru.wikipedia.org")

# 2. Находим поле поиска (у него id="searchInput")
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Автоматизация тестирования")

# 3. Находим кнопку "Найти" (у неё класс "searchButton")
#    Ждем, пока кнопка станет кликабельной
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "searchButton"))
)
search_button.click()

# 4. Проверяем, что мы попали на страницу Selenium
#    Ждем, пока в заголовке появится слово "Selenium"
WebDriverWait(driver, 10).until(
    EC.title_contains("Автоматизация")
)

print("✅ Тест пройден! Мы на странице про Автоматизация.")
driver.quit()