import time
# webdriver - это набор команд для управления браузером
from selenium import webdriver
# импорт класса, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# импорт класса, который позволяет имитировать мышь
from selenium.webdriver.common.action_chains import ActionChains

# Открыть браузер 
driver = webdriver.Chrome()
actions = ActionChains(driver)

# Развернуть на весь экран
driver.maximize_window()

# Зайти на ya.ru
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://ya.ru")
driver.implicitly_wait(15)
assert driver.current_url == 'https://ya.ru/', ('URL не соотвтествует https://ya.ru/')
print('Переход на ya.ru - Успешно')

# Кликнуть на поисковую строку "найдется все"
driver.find_element(by=By.CLASS_NAME,value="search3__input").click()
print('Клик на Поисковую строку - Успешно')

# В появившемся меню выбрать Маркет
driver.find_element(by=By.CLASS_NAME,value="services-suggest").find_element(by=By.CSS_SELECTOR,value='ul > li > a[aria-label=Маркет]').click()
print(driver.current_url)
# Переключаем driver на новую страницу
driver.switch_to.window(driver.window_handles[1])
assert "https://market.yandex.ru" in driver.current_url, ('Переход на Маркет - Не успешно')
print('Переход на Маркет - Успешно')

# Нажать на Каталог
catalog = driver.find_element(by=By.CSS_SELECTOR,value="div[data-zone-name=catalog] > button")
catalog.click()
assert catalog.is_selected() == False, ('Открыть каталог - Не успешно')
print('Открыть каталог - Успешно')

# В левой части меню навести курсор на раздел "Электроника"
electr = driver.find_element(by=By.CSS_SELECTOR,value="div[data-zone-name=catalog-content] > div > div > ul[role=tablist] > li:nth-child(5) > a")
actions.move_to_element(electr)
actions.perform()
print('Переход в Электронику - Успешно')

# В появившемся расширенном меню в разделе "Электроника" кликнуть на раздел "Смартфоны"
smartphones = driver.find_element(by=By.CSS_SELECTOR,value="ul[data-autotest-id=subItems]").find_element(by=By.LINK_TEXT,value="Смартфоны")
smartphones.click() 
assert 'https://market.yandex.ru/catalog--smartfony' in driver.current_url, ('Переход в Смартфоны - Не успешно')
print('Переход в Смартфоны - Успешно')

# В левой части экрана задать параметр поиска в поле "Цена" - до 20000 рублей
price = driver.find_element(by=By.CSS_SELECTOR, value="span[data-auto=filter-range-max] > div > div > input")
price.send_keys(20000)

# В левой части экрана задать параметр поиска в поле "Диагональ" - проставить все чек-боксы от 3,5 дюймов
driver.find_element(by=By.CSS_SELECTOR, value="#\/content\/page\/fancyPage\/cms\/4\/SearchFilters-SearchFilters > div > div > div > div > div:nth-child(10) > div > fieldset > div > div > div:nth-child(2) > div > div > div > div:nth-child(2) > label").click()
driver.find_element(by=By.CSS_SELECTOR, value="#\/content\/page\/fancyPage\/cms\/4\/SearchFilters-SearchFilters > div > div > div > div > div:nth-child(10) > div > fieldset > div > div > div:nth-child(2) > div > div > div > div:nth-child(3) > label").click()
driver.find_element(by=By.CSS_SELECTOR, value="#\/content\/page\/fancyPage\/cms\/4\/SearchFilters-SearchFilters > div > div > div > div > div:nth-child(10) > div > fieldset > div > div > div:nth-child(2) > div > div > div > div:nth-child(4) > label").click()
driver.find_element(by=By.CSS_SELECTOR, value="#\/content\/page\/fancyPage\/cms\/4\/SearchFilters-SearchFilters > div > div > div > div > div:nth-child(10) > div > fieldset > div > div > div:nth-child(2) > div > div > div > div:nth-child(5) > label").click()
driver.find_element(by=By.CSS_SELECTOR, value="#\/content\/page\/fancyPage\/cms\/4\/SearchFilters-SearchFilters > div > div > div > div > div:nth-child(10) > div > fieldset > div > div > div:nth-child(2) > div > div > div > div:nth-child(6) > label").click()
print('Выставлены все параметры для поиска')

#Скролл на начало страницы
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(1)

# Запомнить первый смартфон в списке
first_phone = driver.find_element(by=By.ID,value="/content/page/fancyPage/cms/4/SearchSerp-SearchSerp/serpSearch/content/lazyGenerator/initialContent").find_element(by=By.CSS_SELECTOR,value="div[data-cs-name=navigate]>a >span[data-auto=snippet-title]")
first_phone_text = first_phone.text

# Изменить сортировку на "подороже"
sort = driver.find_element(by=By.CSS_SELECTOR,value="button[data-autotest-id=dprice]")
sort.click()
print('Выбрана сортировка "подороже" - Успешно')

# Ввести в строке "Поиск" наименование запомненного смартфона
driver.find_element(by=By.ID,value="header-search").send_keys(first_phone_text)
print('Ввести наименование запомненного смартфона - Успешно')

# Нажать на кнопку "Найти"
driver.find_element(by=By.CSS_SELECTOR,value="button[data-auto=search-button]").submit()

# Нажать на наименование запомненного смартфона
new_first_phone = driver.find_element(by=By.ID,value="/content/page/fancyPage/cms/4/SearchSerp-SearchSerp/serpSearch/content/lazyGenerator/initialContent").find_element(by=By.CSS_SELECTOR,value="div[data-cs-name=navigate]>a")
new_first_phone.click()

# Переключаем driver на новую страницу
driver.switch_to.window(driver.window_handles[2])
print('Перейти в карточку смартфона - Успешно')

# Вывести цифровое значение оценки смартфона
raiting = driver.find_element(by=By.CSS_SELECTOR,value='div[data-zone-name=Stars] > div > a > span')
print('Рейтинг товара' , raiting.text)

# Закрыть браузер
driver.quit()
