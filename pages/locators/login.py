class LoginLocator:
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    PAGE_TITLE = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6"

    FORGOT_PASSWORD = "//div[@class='orangehrm-login-forgot']//p"
    SUBMIT_BUTTON = "//button[@type='submit']"
    SUCCESSFULLY_RESET = "//div[@class='orangehrm-card-container']//h6"

    AVATAR = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/span"
    LOGOUT_BUTTON = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a"
    SIGNIN_TEXT = "//div[@class='orangehrm-login-slot']//h5"

    INVALID_CREDENTIAL = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"