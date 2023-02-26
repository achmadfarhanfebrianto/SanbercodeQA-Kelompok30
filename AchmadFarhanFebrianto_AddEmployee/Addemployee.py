import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAddemployee(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
 
    def test_positive_add_employee(self):
# steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys("Udin")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys("Sedunia")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]//input[@name='lastName']").send_keys("Sutisno") 
        time.sleep(1)
        # driver.find_element(By.CLASS_NAME,"oxd-file-div oxd-file-div--active").send_keys('C:/Picture/17de85a54f0800cbc3512922a28218c1.jpg')
        # time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click() 
        time.sleep(1)
       
# validasi
        response_data = driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").text
        self.assertIn('Add Employee', response_data)

    def test_negative_add_employee(self):
# steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]//input[@name='lastName']").send_keys("") 
        time.sleep(1)
        # driver.find_element(By.CLASS_NAME,"oxd-file-div oxd-file-div--active").send_keys('C:/Picture/17de85a54f0800cbc3512922a28218c1.jpg')
        # time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click() 
        time.sleep(1)
       
# validasi
        response_data = driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").text
        self.assertIn('Add Employee Field Empty', response_data)

    def test_positive_add_employee_login_detail(self):
# steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys("Udin")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys("Sedunia")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]//input[@name='lastName']").send_keys("Sutisno") 
        time.sleep(1)
        # driver.find_element(By.CLASS_NAME,"oxd-file-div oxd-file-div--active").send_keys('C:/Picture/17de85a54f0800cbc3512922a28218c1.jpg')
        # time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input").send_keys("udin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']").send_keys("Udin1234@") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']").send_keys("Udin1234@") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click() 
        time.sleep(1)
       
# validasi
        response_data = driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").text
        self.assertIn('Add Employee Login Detail', response_data)
        
    def test_negative_add_employee_login_detail(self):
# steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row']/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]//input[@name='lastName']").send_keys("") 
        time.sleep(1)
        # driver.find_element(By.CLASS_NAME,"oxd-file-div oxd-file-div--active").send_keys('C:/Picture/17de85a54f0800cbc3512922a28218c1.jpg')
        # time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input").send_keys("") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']").send_keys("") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']").send_keys("") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click() 
        time.sleep(1)
       
# validasi
        response_data = driver.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/a[@href='#']").text
        self.assertIn('Add Employee Login Detail Empty', response_data)

    def tearDown(self):
        self.browser.close()
if __name__ == "__main__":
        unittest.main()