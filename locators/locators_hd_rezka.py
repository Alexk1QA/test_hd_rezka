
class BaseLocator:
    #  --- --- --- --- --- --- --- --- --- Selectors for firs TEST. Only XPATH --- --- --- --- --- --- --- --- ---

    FILMS = '//*[@id="topnav-menu"]/li[1]/a'
    SERIALS = '//*[@id="topnav-menu"]/li[2]/a'
    MULT = '//*[@id="topnav-menu"]/li[3]/a'
    ANIME = '//*[@id="topnav-menu"]/li[4]/a'
    NEW = '//*[@id="topnav-menu"]/li[5]/a'
    ANONS = '//*[@id="topnav-menu"]/li[6]/a'
    SELECTIONS = '//*[@id="topnav-menu"]/li[7]/a'

    AR_GROUPS_SELECTORS = [FILMS, SERIALS, MULT, ANIME, NEW, ANONS, SELECTIONS]
    ER_GROUPS_SELECTORS = ['Фильмы', 'Сериалы', 'Мультфильмы', 'Аниме', 'Новинки', 'Анонсы', 'Подборки']

    #  --- --- --- --- --- --- --- --- --- Selectors for second TEST. Only XPATH --- --- --- --- --- --- --- --- ---

    TEMPMAILIO = '//*[@id="email"]'

    REGISTRATION_BUTTON_ON_MAIN_PAGE = '//*[@id="top-head"]/div/div[2]/a[2]'
    POPUP_REG_EMAIL = '//*[@id="email"]'
    POPUP_REG_LOGIN = '//*[@id="name"]'
    POPUP_REG_PASS = '//*[@id="password1"]'
    POPUP_REGISTRATION_CONFIRM = '//*[@id="registration"]/div/div/button'

    AR_ACCEPT_REG = '//*[@id="top-head"]/div/div[2]/span'
    ER_ACCEPT_REG = "ПРОФИЛЬ"

    #  --- --- --- --- --- --- --- --- --- Selectors for third TEST. Only XPATH --- --- --- --- --- --- --- --- ---

    LOGIN_BUTTON_ON_MAIN_PAGE = '//*[@id="top-head"]/div/div[2]/a[1]'
    POPUP_LOG_EMAIL = '//*[@id="login_name"]'
    POPUP_LOG_PASS = '//*[@id="login_password"]'
    POPUP_LOG_CONFIRM = '//*[@id="login-popup"]/div[2]/div/div[1]/form/div[3]/div/button'

    LOGIN_AND_PASS = 'test_hd_rezka@gmail.com'

    AR_ACCEPT_LOG = '//*[@id="top-head"]/div/div[2]/span'
    ER_ACCEPT_LOG = "ПРОФИЛЬ"
