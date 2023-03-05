
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
