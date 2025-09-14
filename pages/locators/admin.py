# Access Projects
class AdminLocator:  
    #Create User  
    NAVIGATE_TO_ADMIN = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    ADD_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    PAGE_TITLE = "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"
    ROLE_DROPDOWN = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
    ESS_ROLE = "(//div[@role='option'])[3]"
    ADMIN_ROLE = "(//div[@role='option'])[2]"
    STATUS_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    ENABLE_STATUS = "(//div[@role='option'])[2]"
    USER_NAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    PASSWORD = "(//input[@type='password'])[1]"
    CONFIRM_PASSWORD = "(//input[@type='password'])[2]"
    EMPLOYEE_NAME = "//input[@placeholder='Type for hints...']"
    SELECT_EMPLOYEE = "(//div[@role='option'])[1]"
    SAVE_BUTTON = "//button[@type='submit']"
    NOTIFY_MESSAGE = "//div[@aria-live='assertive']"

    #Search and check user
    SEARCH_BOX = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
    SEARCH_BUTTON = "//button[@type='submit']"
    VERIFY_USERNAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]"
    VERIFY_ROLE = "//div[@class='oxd-table-card'][1]//div//div[3]"
    VERIFY_EMPLOYEE_NAME = "//div[@class='oxd-table-card'][1]//div//div[4]"
    VERIFY_STATUS = "//div[@class='oxd-table-card'][1]//div//div[5]"
    VERIFY_ACTION_DELETE = "//i[@class='oxd-icon bi-trash']"
    VERIFY_ACTION_EDIT = "//i[@class='oxd-icon bi-pencil-fill']"
    CLICK_LIST = "//nav[@aria-label='Topbar Menu']//ul//li[2]"

    #Search and edit role
    EDIT_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6"

    #Delete role
    CONFIRM_DELETE = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"

    #Invalid username
    INVALID_USERNAME = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span"