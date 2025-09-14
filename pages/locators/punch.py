class PunchLocator:
    #Navigate
    NAVIGATE_TO_TIME = "//a[contains(.,'Time')]"
    ATTENDENCE_DROPDOWN = "//nav[@aria-label='Topbar Menu']//ul//li[2]"
    CLICK_PUNCH = "//ul[@class='oxd-dropdown-menu']//li[2]"
    #Punch in
    PUNCH_IN_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6"
    CLICK_DATE = "//div[@class='oxd-date-input']//input"
    CLICK_YEAR = "//li[@class='oxd-calendar-selector-year']"
    SELECT_YEAR = "//li[contains(text(),'2025')]"
    CLICK_MONTH = "//li[@class='oxd-calendar-selector-month']"
    SELECT_MONTH = "//li[contains(text(),'November')]"
    SELECT_DATE = "//div[contains(text(),'18')]"

    CLICK_TIME = "//div[@class='oxd-time-input']//input"
    HOUR = "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']"
    MINUTE = "//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text']"
    SELECT_AM = "//input[@name='am']"
    SUBMIT_BUTTON = "//button[@type='submit']"

    # Punch out
    PUNCH_OUT_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6"
    PUNCH_IN_TIME = "//div[@class='oxd-input-group']//div//p"
    CLICK_DATE_OUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input"
    CLICK_TIME_OUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]/input"
    ENTER_NOTE = "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"

    #View Report
    CLICK_RECORD = "//ul[@class='oxd-dropdown-menu']//li[1]"
    VERIFY_TOTAL_HOUR = "//span[@class='oxd-text oxd-text--span orangehrm-header-total']"
    VERIFY_PUNCH_IN = "(//p[@class='oxd-text oxd-text--p'])[1]"
    VERIFY_PUNCH_OUT = "(//p[@class='oxd-text oxd-text--p'])[2]"
    VERIFY_DURATION = "//div[@class='oxd-table-card'][1]//div[6]//div"

    #Delete Record
    DELETE_BUTTON = "//i[@class='oxd-icon bi-trash']"
    CONFIRM_DELETE = "//button[contains(.,'Yes, Delete')]"
    NOTIFY_MESSAGE = "//div[@aria-live='assertive']"
