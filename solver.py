import pyautogui
import pynput
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# document.getElementById("AREA_BOLIVIA").dispatchEvent(new Event("mousedown"));

o = webdriver.ChromeOptions()
o.add_extension("uBlock-Origin.crx")
o.add_argument("--log-level=3")
o.add_experimental_option("useAutomationExtension", False)
o.add_experimental_option("excludeSwitches",["enable-automation"])
s = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=o)
driver.get("https://www.geoguessr.com/vgp/3016")
try:
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "onetrust-group-container"))
    )
except:
    driver.refresh()
finally:
    driver.maximize_window()
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.refresh()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "game-header_wrapper__82t4V"))
    )

# driver.find_element(By.CLASS_NAME, "game-footer_settingsButton__6xv0w").click()
# WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "modal_content__mrR0Q modal_colorWhite__4hqsv modal_sizeSmall__uwO3n")))
# driver.find_elements(By.CLASS_NAME, "checkbox_input__na3pr")[1].click()
# driver.find_element(By.CSS_SELECTOR, "button.button__CnARx.button_variantPrimary__xc8Hp").click()
# print("Speedrun Mode enabled")

countryList = driver.find_element(By.CLASS_NAME, "area-list_section__fh0Nc").get_attribute("data-area-labels").split(",")

#Check if collected array length doesn match total countries
print(countryList)
print(len(countryList))
print(driver.find_element(By.CLASS_NAME, "game-header_withDivider__MmW9n").text.split("/")[1])
if len(countryList)!= int(driver.find_element(By.CLASS_NAME, "game-header_withDivider__MmW9n").text.split("/")[1]):
    print("COUNTRY LENGTH AND GAME COUNTRY LENGTH MISMATCH")
    exit()


while input("Enter \"Y\" to go again.").lower()=="y":
    tempCountryList = countryList.copy()
    driver.find_elements(By.CSS_SELECTOR, "button.button_sizeSmall__POheY.button_variantSecondaryInverted__9kX_w.button_button__CnARx")[1].click()
    print("Restarted game")
    currentCountryName = driver.find_element(By.CLASS_NAME, "game-header_wrapper__82t4V").get_attribute("data-current-question-text")
    done = 0
    while done < len(countryList):
        print(currentCountryName)
        WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "AREA_" + currentCountryName.upper())))
        driver.execute_script('document.getElementById(\"AREA_' + currentCountryName.upper() + '\").dispatchEvent(new Event("click"));')
        # driver.execute_script('document.getElementById(\"AREA_' + currentCountryName.upper() + '\").dispatchEvent(new Event("mousedown"));')
        driver.execute_script('console.log("hello");')
        while currentCountryName !=driver.find_element(By.CLASS_NAME, "game-header_wrapper__82t4V").get_attribute("data-current-question-text"):
            currentCountryName = driver.find_element(By.CLASS_NAME, "game-header_wrapper__82t4V").get_attribute("data-current-question-text")
            done+=1



