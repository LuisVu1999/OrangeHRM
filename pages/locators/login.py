class LoginLocator:
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    PAGE_TITLE = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6"

    FORGOT_PASSWORD = "//div[@class='orangehrm-login-forgot']//p"
    SUBMIT_BUTTON = "//button[@type='submit']"
    SUCCESSFULLY_RESET = "//*[@id='app']/div[1]/div[1]/div/h6"

    AVATAR = "//span[@class='oxd-userdropdown-tab']"
    LOGOUT_BUTTON = "//a[contains(text(),'Logout')]"
    SIGNIN_TEXT = "//div[@class='orangehrm-login-slot']//h5"

    INVALID_CREDENTIAL = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"

    ERROR_USER= "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span"
    ERROR_PASS = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span"