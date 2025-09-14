class PimLocator:
    #Create Employee  
    NAVIGATE_TO_PIM = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    ADD_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    PAGE_TITLE = "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"
    UPLOAD_BUTTON = "input[type='file']"
    FIRST_NAME = "//input[@name='firstName']"
    LAST_NAME = "//input[@name='lastName']"
    MIDDLE_NAME = "//input[@name='middleName']"
    EMPLOYEE_ID = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    ENABLE_PASSWORD = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label"
    USER_NAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"
    PASSWORD = "(//input[@type='password'])[1]"
    CONFIRM_PASSWORD = "(//input[@type='password'])[2]"
    STATUS_ENABLE= "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label"
    SAVE_BUTTON = "//button[@type='submit']"
    NOTIFY_MESSAGE = "//div[@aria-live='assertive']"

    #View Employee
    VERIFY_FIRST_MIDDLE_NAME = "//div[@class='oxd-table-card']//div//div[3]"
    VERIFY_ID = "//div[@class='oxd-table-card'][1]//div//div[2]"
    VERIFY_LAST_NAME = "//div[@class='oxd-table-card'][1]//div//div[4]"
    VERIFY_JOB_TITLE = "//div[@class='oxd-table-card'][1]//div//div[5]"
    VERIFY_EMPLOYEE_STATUS = "//div[@class='oxd-table-card'][1]//div//div[6]"
    VERIFY_SUB_UNIT = "//div[@class='oxd-table-card'][1]//div//div[7]"
    VERIFY_SUPPERVISOR = "//div[@class='oxd-table-card'][1]//div//div[8]"
    VERIFY_ACTION_DELETE = "//i[@class='oxd-icon bi-trash']"
    VERIFY_ACTION_EDIT = "//i[@class='oxd-icon bi-pencil-fill']"
    CLICK_LIST = "//nav[@aria-label='Topbar Menu']//ul//li[2]"

    #Edit Employee
    EDIT_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6"
    EDIT_EMP_ID = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"
    #Job title
    CLICK_JOB = "//div[@role='tablist']//div[6]"
    CLICK_JOB_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    SELECT_TESTER = "//span[contains(text(),'QA Engineer')]"
    CLICK_STATUS = "(//div[@class='oxd-select-text oxd-select-text--active'])[5]"
    SELECT_FULLTIME = "//span[contains(text(),'Full-Time Contract')]"
    CLICK_SUBUNIT = "(//div[@class='oxd-select-text oxd-select-text--active'])[3]"
    SELECT_ENGINEERING = "//span[contains(text(),'Engineering')]"
    #Report to
    CLICK_REPORT_TO = "//div[@role='tablist']//div[8]"
    CLICK_ADD_BUTTON = "(//button[@type='button'])[4]"
    SUPERVISOR_NAME = "//input[@placeholder='Type for hints...']"
    SELECT_USER = "//div[@role='option'][1]"
    CLICK_METHOD = "//div[@class='oxd-select-text oxd-select-text--active']"
    SELECT_DIRECT = "//div[@role='option'][2]"
    SAVE_BUTTON_EDITED = "(//button[@type='submit'])[1]"

    #Delete Employe
    CONFIRM_DELETE = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"

    # Search Employee
    INVALID_USERNAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span"
    SEARCH_BOX = "(//input[@placeholder='Type for hints...'])[1]"
    SELECT_EMP = "//div[@role='option'][1]"
    SEARCH_BUTTON = "//button[@type='submit']"