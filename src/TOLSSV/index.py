# Import driver and browser configurations
import config
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

prodURL = 'https://truesuperfiber.truecorp.co.th'
testURL = ''

# Open the browser
config.driver.get(prodURL)

def getHomePackage():

    # Click on the home packages tile/button
    config.driver.find_element_by_class_name('house-bg').click()
    config.driver.implicitly_wait(3)

    # Find the 50/20 package and select it
    # config.driver.find_element_by_xpath('/box/btn-package-privilege[5]').click()
    config.driver.find_element_by_class_name('btn-package-privilege').click() # Just have to select first package right now
    config.driver.implicitly_wait(3)

    # Confirm the selection of the package
    # config.driver.find_element_by_class_name('btn-package-apply').click()
    # config.driver.find_element_by_css_selector(".container > .d-none > .btn-package-apply").click()
    config.driver.find_element_by_xpath("//a[@class='btn-package-apply']").click()
    config.driver.implicitly_wait(3)

    # Insert sample address into the coverage map and check coverage
    address = config.driver.find_element_by_id('gmap-address')
    address.send_keys("186 ซอย รามคําแหง 62 แขวง หัวหมาก เขตบางกะปิ กรุงเทพมหานคร ประเทศไทย")
    config.driver.find_element_by_class_name('btn-confirm-address').click()
    config.driver.find_element_by_xpath('input[@type="submit"]')
    # Address not have speed, so go on short list
    config.driver.find_element_by_xpath('/packages/btn-package-privilege[5]').click()
    # Fill in the notification form

# Close the testing
# config.driver.close()

# Start Test 1
getHomePackage()