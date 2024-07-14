# Выполните следующие задания:
# Открыть браузер
# Загрузить файл "automation-practice-table"
# найти все ссылки
# поочередно перейти по ним
# в открывшихся сайтах проверить заголовки:
# 	"Бурдж-Халифа"
# 	"Абрадж аль-Бейт"
# 	"Тайбэй таун"
# 	"Шанхайский всемирный финансовый центр"
# закрыть браузер

# При выполнении задания используйте циклы, списки.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.maximize_window()


driver.get("file:///D:/Learning/GoIT/Python/My_Repo/QA_auto/QA_HW_01/automation-practice-table.html")


details_list = driver.find_elements(By.LINK_TEXT, "details")

details = ["Бурдж-Халифа", "Абрадж аль-Бейт", "Тайбэй таун", "Шанхайский всемирный финансовый центр"]

links_list = []

for item in details_list:
    link = item.get_attribute('href')
    # print("link =  ", link)
    links_list.append(link)

# print(links_list)

for link in links_list:
    driver.get(link)
    h1 = driver.find_element(By.TAG_NAME, 'h1')
    print("h1 = ", h1.text)
    sleep(2)


