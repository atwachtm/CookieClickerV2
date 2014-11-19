# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import re
import signal


class Cookieclicker(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(0)
        self.base_url = "http://orteil.dashnet.org/cookieclicker/"
        self.verificationErrors = []
        self.accept_next_alert = True
        #signal.signal(signal.SIGINT, self.handler)

    def test_cookieclicker(self):
        driver = self.driver
        driver.get(self.base_url)
        """Cookie_string = driver.find_element_by_id("cookies").text
        Cookie_list = Cookie_string.split()
        numCookies = float(Cookie_list[0])
        total_cookies = driver.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/div")
        print total_cookies
        print Cookie_string
        print numCookies"""
<<<<<<< HEAD
        file_import = False
        product_count = 0
        ach_count = 0
        #import if the file is present
        try:
            with open("exportSave.txt"):
                self.Import_save()
                file_import = True
        except (IOError):
            print "The file could not be found for import. Starting a new game."
        stats = driver.find_element_by_id('statsButton')
        stats.click()
        #Tiny Cookie Achievement
        Small_cookie = driver.find_element_by_xpath("//div[@id='menu']/div[5]/div[4]/div[126]")
        if 'enabled' in Small_cookie.get_attribute('class'):
            pass
        else:
            Small_cookie = driver.find_element_by_class_name("tinyCookie")
            Small_cookie.click()
        #Name the Bakery achievement
        bakeName = driver.find_element_by_xpath("//div[@id='menu']/div[5]/div[4]/div[127]")
        if 'enabled' in bakeName.get_attribute('class'):
            pass
        else:
            if self.is_element_present(By.ID, "bakeryName"):
                Bake_Name = driver.find_element_by_id("bakeryName")
                Bake_Name.click()
                if self.is_element_present(By.ID, "promptOption1"):
                    driver.find_element_by_id("promptOption1").click()
                    driver.find_element_by_id("promptOption0").click()
=======
        if self.is_element_present(By.ID, "bakeryName"):
            Bake_Name = driver.find_element_by_id("bakeryName")
            Bake_Name.click()
            if self.is_element_present(By.ID, "promptOption1"):
                driver.find_element_by_id("promptOption1").click()
                driver.find_element_by_id("promptOption0").click()
>>>>>>> FETCH_HEAD
        #Products
        product_button0 = driver.find_element_by_id("product0")
        cursor_count = 0
        print str(cursor_count) + " cursors have been bought"
        #Grandma
        product_button1 = driver.find_element_by_id("product1")
        grandma_count1 = 0
        #farm
        product_button2 = driver.find_element_by_id("product2")
        farm_count2 = 0
        #factory
        product_button3 = driver.find_element_by_id("product3")
        factory_count3 = 0
        #mine
        product_button4 = driver.find_element_by_id("product4")
        mine_count4 = 0
        #shipment
        product_button5 = driver.find_element_by_id("product5")
        shipment_count5 = 0
        #Alchemy lab
        product_button6 = driver.find_element_by_id("product6")
        alchemy_count6 = 0
        #Portal
        product_button7 = driver.find_element_by_id("product7")
        portal_count7 = 0
        #Time machine
        product_button8 = driver.find_element_by_id("product8")
        tmachine_count8 = 0
        #Antimatter Condenser
        product_button9 = driver.find_element_by_id("product9")
        antimatter_count9 = 0
        #Prism
        product_button10 = driver.find_element_by_id("product10")
        prism_count10 = 0
<<<<<<< HEAD
        if file_import is True:
            cursor_count = driver.find_element_by_xpath("//div[@id='product0']/div[3]/div[3]").text
            grandma_count1 = driver.find_element_by_xpath("//div[@id='product1']/div[3]/div[3]").text
            farm_count2 = driver.find_element_by_xpath("//div[@id='product2']/div[3]/div[3]").text
            factory_count3 = driver.find_element_by_xpath("//div[@id='product3']/div[3]/div[3]").text
            mine_count4 = driver.find_element_by_xpath("//div[@id='product4']/div[3]/div[3]").text
            shipment_count5 = driver.find_element_by_xpath("//div[@id='product5']/div[3]/div[3]").text
            alchemy_count6 = driver.find_element_by_xpath("//div[@id='product6']/div[3]/div[3]").text
            portal_count7 = driver.find_element_by_xpath("//div[@id='product7']/div[3]/div[3]").text
            tmachine_count8 = driver.find_element_by_xpath("//div[@id='product8']/div[3]/div[3]").text
            antimatter_count9 = driver.find_element_by_xpath("//div[@id='product9']/div[3]/div[3]").text
            prism_count10 = driver.find_element_by_xpath("//div[@id='product10']/div[3]/div[3]").text
            countNumbers = [cursor_count, grandma_count1, farm_count2, factory_count3, mine_count4, shipment_count5,
                            alchemy_count6, portal_count7, tmachine_count8, antimatter_count9, prism_count10]
            countActual = []
            for i in countNumbers:
                if i == "":
                    i = '0'
                    countActual.append(int(i))
                    print "Product is not owned. " + i
                else:
                    countActual.append(int(i))
                    print "Number of owned product is " + i
                    product_count += int(i)
            print countActual
            cursor_count = countActual[0]
            grandma_count1 = countActual[1]
            farm_count2 = countActual[2]
            factory_count3 = countActual[3]
            mine_count4 = countActual[4]
            shipment_count5 = countActual[5]
            alchemy_count6 = countActual[6]
            portal_count7 = countActual[7]
            tmachine_count8 = countActual[8]
            antimatter_count9 = countActual[9]
            prism_count10 = countActual[10]
            print str(product_count) + " is the total number of buildings currently owned"
            ach_string = driver.find_element_by_xpath("//div[@id='menu']/div[5]/div[2]").text
            ach_list = ach_string.split(' ')
            ach_string2 = ach_list[2]
            ach_list2 = ach_string2.split('/')
            ach_count = int(ach_list2[0])
            print str(ach_count) + " achievements have already been unlocked"
        click_count = 0
        cursor_max = 10
        grandma_max = 10
        other_max = 10
        while product_count < 2500:
            driver.find_element_by_id("bigCookie").click()
            click_count += 1
            if click_count == 500:
                self.Export_save()
                click_count = 0
                stats.click()
            #Buying products
            if "enabled" in product_button0.get_attribute('class') and cursor_count < cursor_max:
=======
        #Upgrades
        #Upgrade_list = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
        #Upgrade_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        stats = driver.find_element_by_id('statsButton')
        stats.click()
        Small_cookie = driver.find_element_by_class_name("tinyCookie")
        Small_cookie.click()
        ach_count = 0
        product_count = 0
        click_count = 0
        while product_count < 10:
            driver.find_element_by_id("bigCookie").click()
            click_count += 1
            """Cookie_string = driver.find_element_by_id("cookies").text
            Cookie_list = Cookie_string.split(" ")
            Avail_cookies = str(Cookie_list[0])
            print Cookie_list[0]
            print Avail_cookies
            for i in Avail_cookies:
                if i == ',':
                    y = Avail_cookies.replace(',', "")
                    #print y
                    Cookie_list.insert(0, y)
                elif i == '.':
                    z = Avail_cookies.replace('.', "")
                    Cookie_list.insert(0, z)"""
                    #print Cookie_list
            #numCookies = float(Cookie_list[0])
            #Buying products Round 1
            if "enabled" in product_button0.get_attribute('class') and cursor_count < 10:
>>>>>>> FETCH_HEAD
                product_button0.click()
                cursor_count += 1
                product_count += 1
            if "enabled" in product_button1.get_attribute('class') and grandma_count1 < grandma_max:
                product_button1.click()
                grandma_count1 += 1
                product_count += 1
            if "enabled" in product_button2.get_attribute('class') and farm_count2 < other_max:
                product_button2.click()
                farm_count2 += 1
                product_count += 1
            if "enabled" in product_button3.get_attribute('class') and factory_count3 < other_max:
                product_button3.click()
                factory_count3 += 1
                product_count += 1
            if "enabled" in product_button4.get_attribute('class') and mine_count4 < other_max:
                product_button4.click()
                mine_count4 += 1
                product_count += 1
            if "enabled" in product_button5.get_attribute('class') and shipment_count5 < other_max:
                product_button5.click()
                shipment_count5 += 1
                product_count += 1
            if "enabled" in product_button6.get_attribute('class') and alchemy_count6 < other_max:
                product_button6.click()
                alchemy_count6 += 1
                product_count += 1
            if "enabled" in product_button7.get_attribute('class') and portal_count7 < other_max:
                product_button7.click()
                portal_count7 += 1
                product_count += 1
            if "enabled" in product_button8.get_attribute('class') and tmachine_count8 < other_max:
                product_button8.click()
                tmachine_count8 += 1
                product_count += 1
            if "enabled" in product_button9.get_attribute('class') and antimatter_count9 < other_max:
                product_button9.click()
                antimatter_count9 += 1
                product_count += 1
<<<<<<< HEAD
            if "enabled" in product_button10.get_attribute('class') and prism_count10 < other_max:
                product_button10.click()
                prism_count10 += 1
                product_count += 1
            if product_count == 110:
                cursor_max = 400
                grandma_max = 250
                other_max = 200
=======
            if "enabled" in product_button10.get_attribute('class') and prism_count10 < 10:
                product_button10.click()
                prism_count10 += 1
                product_count += 1
>>>>>>> FETCH_HEAD
            """
            #Selling
            if grandma_count1 == 11:
                grandma_count1 -= 1
                product_count -= 1
                hover = ActionChains(self).move_to_element(product_button1)
                hover.perform()
                if self.is_element_present(By.ID, 'buttonSell-1'):
                    driver.find_elements_by_id('buttonSell-1').click()
                    print "Grandma is out of business"
                    """
            #Buying upgrades
            if self.is_element_present(By.XPATH, "//div[@id='upgrades']/div[contains(@class, 'enabled')]"):
                print "Checking for Upgrades... "
                driver.find_element_by_xpath("//div[@id='upgrades']/div[contains(@class, 'upgrade enabled')]").click()
            try:
                #total number of achievements
                ach_string = driver.find_element_by_xpath("//div[@id='menu']/div[5]/div[2]").text
                ach_list = ach_string.split(' ')
                ach_string2 = ach_list[2]
                ach_list2 = ach_string2.split('/')
                #clean up of achievements
                if ach_count < int(ach_list2[0]):
                    driver.find_element_by_xpath("//div[contains(@class, 'note')]/div[contains(@class, 'close')]").click()
                    ach_count += 1
            except (StaleElementReferenceException, NoSuchElementException):
                print "Caught stale element--skippin'!"
        while product_count >= 10 and product_count <= 2500:
            driver.find_element_by_id("bigCookie").click()
            if "enabled" in product_button0.get_attribute('class') and cursor_count < 400:
                product_button0.click()
                cursor_count += 1
                product_count += 1
            if "enabled" in product_button1.get_attribute('class') and grandma_count1 < 250:
                product_button1.click()
                grandma_count1 += 1
                product_count += 1
            if "enabled" in product_button2.get_attribute('class') and farm_count2 < 200:
                product_button2.click()
                farm_count2 += 1
                product_count += 1
            if "enabled" in product_button3.get_attribute('class') and factory_count3 < 200:
                product_button3.click()
                factory_count3 += 1
                product_count += 1
            if "enabled" in product_button4.get_attribute('class') and mine_count4 < 200:
                product_button4.click()
                mine_count4 += 1
                product_count += 1
            if "enabled" in product_button5.get_attribute('class') and shipment_count5 < 200:
                product_button5.click()
                shipment_count5 += 1
                product_count += 1
            if "enabled" in product_button6.get_attribute('class') and alchemy_count6 < 200:
                product_button6.click()
                alchemy_count6 += 1
                product_count += 1
            if "enabled" in product_button7.get_attribute('class') and portal_count7 < 200:
                product_button7.click()
                portal_count7 += 1
                product_count += 1
            if "enabled" in product_button8.get_attribute('class') and tmachine_count8 < 200:
                product_button8.click()
                tmachine_count8 += 1
                product_count += 1
            if "enabled" in product_button9.get_attribute('class') and antimatter_count9 < 200:
                product_button9.click()
                antimatter_count9 += 1
                product_count += 1
            if "enabled" in product_button10.get_attribute('class') and prism_count10 < 200:
                product_button10.click()
                prism_count10 += 1
                product_count += 1
            if self.is_element_present(By.XPATH, "//div[@id='upgrades']/div[contains(@class, 'enabled')]"):
                print "Checking for Upgrades... "
                driver.find_element_by_xpath("//div[@id='upgrades']/div[contains(@class, 'upgrade enabled')]").click()
            #perform the export
            if product_count % 10 == 0:
                self.Export_save()
            try:
                #total number of achievements
                ach_string = driver.find_element_by_xpath("//div[@id='menu']/div[5]/div[2]").text
                ach_list = ach_string.split(' ')
                ach_string2 = ach_list[2]
                ach_list2 = ach_string2.split('/')
                #clean up of achievements
                if ach_count < int(ach_list2[0]):
                    driver.find_element_by_xpath("//div[contains(@class, 'note')]/div[contains(@class, 'close')]").click()
                    ach_count += 1
            except (StaleElementReferenceException, NoSuchElementException):
                print "Caught stale element--skippin'!"

    """def handler(signum, frame):
        menu_save = self.driver.find_element_by_id('prefsButton')
        menu_save.click()
        self.driver.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/a").click()
        with open("exportSave.txt", "w+") as save_data:
            export_code = self.driver.find_element_by_xpath("//div[@id='promptContent']/div[2]/textarea").text
            save_data.write(str(export_code))
            menu_save.click()
        self.driver.find_element_by_id("promptOption0").click()
        raise KeyboardInterrupt"""

<<<<<<< HEAD
    """def handler(signum, frame):
=======
    def Export_save(self):
>>>>>>> FETCH_HEAD
        menu_save = self.driver.find_element_by_id('prefsButton')
        menu_save.click()
        self.driver.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/a").click()
        with open("exportSave.txt", "w+") as save_data:
            export_code = self.driver.find_element_by_xpath("//div[@id='promptContent']/div[2]/textarea").text
            save_data.write(str(export_code))
            menu_save.click()
<<<<<<< HEAD
        self.driver.find_element_by_id("promptOption0").click()
        raise KeyboardInterrupt"""

    def Export_save(self):
        menu_save = self.driver.find_element_by_id('prefsButton')
        menu_save.click()
        self.driver.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/a").click()
        with open("exportSave.txt", "w+") as save_data:
            export_code = self.driver.find_element_by_xpath("//div[@id='promptContent']/div[2]/textarea").text
            save_data.write(str(export_code))
            menu_save.click()
            self.driver.find_element_by_id("promptOption0").click()
        print "An export occurred but may not be what you wanted, hur hur hur!"

    def Import_save(self):
        print "Importing data. Please Wait..."
=======
            self.driver.find_element_by_id("promptOption0").click()
        print "An export occurred but may not be what you wanted, hur hur hur!"

    def Import_save(self):
>>>>>>> FETCH_HEAD
        menu_save = self.driver.find_element_by_id('prefsButton')
        menu_save.click()
        self.driver.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/a[2]").click()
        with open("exportSave.txt", "r") as import_data:
            import_box = self.driver.find_element_by_xpath("//div[@id='promptContent']/div[2]/textarea")
            save_code = import_data.read()
            import_box.send_keys(save_code)
<<<<<<< HEAD
            self.driver.find_element_by_id("promptOption0").click()
=======
>>>>>>> FETCH_HEAD
            menu_save.click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.Export_save()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
