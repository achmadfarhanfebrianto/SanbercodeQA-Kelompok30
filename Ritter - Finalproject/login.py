import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
# steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(3)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]').click()
        time.sleep(3)

# validasi
        response_data = driver.find_element(By.XPATH,"//header/div[1]/div[1]/span[1]/h6[1]"
).text
        self.assertIn('Dashboard', response_data)

    def test_username_password_invalid (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep (3)
        driver.find_element(By.NAME,"username").send_keys("Adm") # isi invalid username
        time.sleep(3)
        driver.find_element(By.NAME,"password").send_keys("123") # isi invalid password
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]').click()
        time.sleep(3)
        # Validasi 
        response_data = driver.find_element( 
            By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]").text 
        self.assertIn('Invalid credentials', response_data) 

    def test_All_blank (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3) 
        driver.find_element(By.NAME, "username").send_keys("") 
        time.sleep(3) 
        driver.find_element(By.NAME, "password").send_keys("") 
        time.sleep(3) 
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]').click()
        time.sleep(3)
 
        # Validasi 
        response_data = driver.find_element( 
        By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]").text 
        self.assertIn('Login', response_data)


    def test_Logout (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3) 
        driver.find_element(By.NAME, "username").send_keys("Admin") 
        time.sleep(3) 
        driver.find_element(By.NAME, "password").send_keys("admin123") 
        time.sleep(3) 
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//header/div[1]/div[2]/ul[1]/li[1]/span[1]/i[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        time.sleep(3)
        # Validasi 
        response_data = driver.find_element( 
        By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]").text 
        self.assertIn('Login', response_data)

    def test_forgot_password (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3) 
        driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[4]/p[1]").click() 
        time.sleep(3) 
        driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin") 
        time.sleep(3) 
        driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/form[1]/div[2]/button[2]").click()
        time.sleep(3)
 
        # Validasi 
        response_data = driver.find_element( 
        By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/h6[1]").text 
        self.assertIn('Reset Password link sent successfully', response_data)

    def tearDown(self):
                self.browser.close()

if __name__ == "__main__":
    unittest.main()








     