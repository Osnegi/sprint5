from selenium.webdriver.common.by import By

class Locators:
    #Регистрация
    REG_LINK = (By.XPATH, ".//a[text() = 'Зарегистрироваться']") # ссылка 'Зарегистрироваться" на форму регистрации,
    REG_NAME = (By.XPATH, ".//label[text() = 'Имя']/parent::*/input") #Поле «Имя» (как вариант надежного локатора - //label[text() = 'Имя']/following-sibling::input)
    REG_EMAIL = (By.XPATH,".//label[text() = 'Email']/parent::*/input") #Поле email
    REG_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']") #Поле пароль
    REG_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") #кнопка 'Зарегистрироваться"
    INCORRECT_PASSWORD = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #ошибка для некорректного пароля

    #Вход
    HEADER_ENTER = (By.XPATH, ".//h2[text() = 'Вход']")
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #вход через кнопку «Войти в аккаунт» на главной странице,
    ENTER_CABINET_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #вход через кнопку «Личный кабинет» на главной странице,
    ENTER_LINK_IN_REG = (By.XPATH, ".//a[text() = 'Войти']") #вход через ссылку «Войти" в форме регистрации,
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']") #ссылка 'Восстановить пароль' на форму восстановления пароля.
    ENTER_LINK_IN_RESTORE_PASSWORD = (By.XPATH, ".//a[text() = 'Войти']") #вход через ссылку 'Войти' в форме восстановления пароля.

    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']") #поля ввода email в форме входа в личный аккаунт
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']") #поля ввода password в форме входа в личный аккаунт
    ENTER_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") # вход в личный кабинет (кнопка Войти)

    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")

    #Переход в личный кабинет (проверено во всех тестах на вход)
    PASS_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #переход в личный кабинет

    #Переход из личного кабинета в конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']") #переход через кнопку «Конструктор»
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # через логотип Stellar Burgers
    GET_BURGER_HEADER = (By.XPATH, ".//h1[text() = 'Соберите бургер']") #надпись - заголовок конструктора "Соберите бургер"

    #Выход из аккаунт
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']") #кнопка «Выйти» в личном кабинете

    #Раздел «Конструктор»
    BUNS_TO_SELECT = (By.XPATH, ".//span[text() = 'Булки']") #«Булки» заголовок
    BUNS_HEADER_SELECTED = (By.XPATH, ".//span[text() = 'Булки']/parent::*[contains(@class,'current')]")  # «Булки» выбранный заголовок
    BUNS_IMAGE = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']") #картинка булки

    SAUCES_TO_SELECT = (By.XPATH, ".//span[text() = 'Соусы']") #«Соусы» заголовок
    SAUCES_IMAGE = (By.XPATH, ".//img[@alt = 'Соус с шипами Антарианского плоскоходца']") #картинка соуса
    SAUCES_HEADER_SELECTED = (By.XPATH, ".//span[text() = 'Соусы']/parent::*[contains(@class,'current')]")  # «Соусы» выбранный заголовок

    STUFFING_TO_SELECT = (By.XPATH, ".//span[text() = 'Начинки']") #«Начинки» заголовок
    STUFFING_HEADER = (By.XPATH, ".//h2[text() = 'Начинки']")  #header начинки
    STUFFING_HEADER_SELECTED = (By.XPATH, ".//span[text() = 'Начинки']/parent::*[contains(@class,'current')]")  # «Начинки» выбранный заголовок