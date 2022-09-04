import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestEmployeeTimesheet(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Melihat detail timesheets karyawan
    def test_a_see_detail_emploee_timesheet(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu Time
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button").click() # klik tombol View
        time.sleep(5)

        # validasi
        text = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/h6").text
        # sidebar_menu_title = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertIn("Timesheet for", text)

    # Menambahkan project kerja pada timesheet karyawan ketika field project dan activity kosong
    def test_b_invalid_addProject_activity_empty(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu Time
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button").click() # klik tombol View
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() # klik tombol Edit
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[6]/td/button").click() # klik tombol Add Row
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click() # klik tombol Save
        time.sleep(5)


        # validasi
        text_project = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[6]/td[1]/div/span").text
        text_activity = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[6]/td[2]/div/span").text

        self.assertIn("Project", text_project)
        self.assertIn("Activity", text_activity)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()