from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 30)

# Open the website
driver.get("https://authorized-partner.vercel.app/")
time.sleep(3)

# Click Get Started
get_started = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Get Started']")))
get_started.click()
time.sleep(2)

# Accept terms and conditions
checkbox = wait.until(EC.element_to_be_clickable((By.ID, "remember")))
checkbox.click()
time.sleep(1)

# Click Continue
continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']")))
continue_btn.click()
time.sleep(2)

# Fill in personal details
wait.until(EC.presence_of_element_located((By.ID, "_r_0_-form-item"))).send_keys("Test")
time.sleep(0.5)
driver.find_element(By.ID, "_r_1_-form-item").send_keys("User")
time.sleep(0.5)
driver.find_element(By.ID, "_r_2_-form-item").send_keys("swetaniroula123+test101@gmail.com")
time.sleep(0.5)
driver.find_element(By.ID, "_r_4_-form-item").send_keys("9822225555")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Test@1234")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Test@1234")
time.sleep(1)

# Click Next to proceed
next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
next_btn.click()
time.sleep(5)

# OTP verification
print("OTP has been sent to your email: swetaniroula123+test67@gmail.com")
otp_code = input("Enter the 6-digit OTP: ").strip()
time.sleep(2)

# Enter OTP - try individual boxes first, then a single field
otp_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
if len(otp_fields) == 6:
    for i, digit in enumerate(otp_code):
        otp_fields[i].click()
        otp_fields[i].send_keys(digit)
        time.sleep(0.3)
else:
    try:
        otp_field = driver.find_element(By.XPATH, "//input[@maxlength='6']")
        otp_field.click()
        otp_field.clear()
        otp_field.send_keys(otp_code)
    except Exception:
        driver.find_element(By.XPATH, "//input").send_keys(otp_code)

time.sleep(2)

# Click verify if the button exists
try:
    verify_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Verify')]")))
    driver.execute_script("arguments[0].click();", verify_btn)
except Exception:
    pass

time.sleep(5)


try:
    wait.until(EC.url_contains("step=details"))
except Exception:
    try:
        next_after_otp = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
        driver.execute_script("arguments[0].click();", next_after_otp)
        time.sleep(5)
    except Exception:
        pass

time.sleep(3)

# Agency details
agency_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Agency Name']")))
driver.execute_script("arguments[0].scrollIntoView();", agency_name)
agency_name.click()
agency_name.send_keys("Test Agency")
time.sleep(0.5)

role = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Role in Agency']")
role.click()
role.send_keys("Manager")
time.sleep(0.5)

agency_email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Agency Email Address']")
agency_email.click()
agency_email.send_keys("swetaniroula123+test69@gmail.com")
time.sleep(0.5)

agency_website = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Agency Website']")
agency_website.click()
agency_website.send_keys("www.testagency.com")
time.sleep(0.5)

agency_address = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Agency Address']")
agency_address.click()
agency_address.send_keys("Kathmandu, Nepal")
time.sleep(1)

region_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
driver.execute_script("arguments[0].scrollIntoView(true);", region_dropdown)
time.sleep(1)
driver.execute_script("arguments[0].click();", region_dropdown)
time.sleep(2)

driver.execute_script("""
    var containers = document.querySelectorAll('[data-radix-popper-content-wrapper], [role="listbox"]');
    for (var i = 0; i < containers.length; i++) {
        var items = containers[i].querySelectorAll('[role="option"]');
        if (items.length > 0) { items[0].click(); return; }
    }
    var options = document.querySelectorAll('[role="option"]');
    if (options.length > 0) options[0].click();
""")
time.sleep(2)

next_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
driver.execute_script("arguments[0].click();", next_btn2)
time.sleep(3)

# Professional experience
experience_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
driver.execute_script("arguments[0].scrollIntoView(true);", experience_dropdown)
time.sleep(1)
driver.execute_script("arguments[0].click();", experience_dropdown)
time.sleep(2)

driver.execute_script("""
    var containers = document.querySelectorAll('[data-radix-popper-content-wrapper], [role="listbox"]');
    for (var i = 0; i < containers.length; i++) {
        var items = containers[i].querySelectorAll('[role="option"]');
        if (items.length > 0) { items[0].click(); return; }
    }
    var options = document.querySelectorAll('[role="option"]');
    if (options.length > 0) options[0].click();
""")
time.sleep(2)


try:
    students = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter an approximate number.']")))
except Exception:
    students = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]")))
students.click()
students.send_keys("50")
time.sleep(0.5)

try:
    focus = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., Undergraduate admissions to Canada.']")))
except Exception:
    focus = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., Undergraduate admissions to Canada']")))
focus.click()
focus.send_keys("Undergraduate admissions to Canada")
time.sleep(0.5)

# Success metrics
try:
    metrics = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., 90%']")))
except Exception:
    try:
        metrics = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., 90% ']")))
    except Exception:
        metrics = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[2]")))
metrics.click()
metrics.send_keys("90")
time.sleep(0.5)

# Select services offered
driver.find_element(By.XPATH, "//label[normalize-space()='Career Counseling']").click()
time.sleep(0.3)
driver.find_element(By.XPATH, "//label[normalize-space()='Admission Applications']").click()
time.sleep(0.3)
driver.find_element(By.XPATH, "//label[normalize-space()='Visa Processing']").click()
time.sleep(0.3)
driver.find_element(By.XPATH, "//label[normalize-space()='Test Prepration']").click()
time.sleep(1)

next_btn3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
driver.execute_script("arguments[0].scrollIntoView(true);", next_btn3)
driver.execute_script("arguments[0].click();", next_btn3)
time.sleep(3)

# Verification and preferences
try:
    biz_reg = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your registration number']")))
except Exception:
    biz_reg = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Registration Number']")))
biz_reg.click()
biz_reg.send_keys("REG-12345-TEST")
time.sleep(1)

# Countries multi-select
try:
    countries_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'flex flex-wrap items-center gap-1')]")))
    driver.execute_script("arguments[0].click();", countries_dropdown)
    time.sleep(2)

    options = driver.find_elements(By.XPATH, "//*[@role='option']")
    if options:
        driver.execute_script("arguments[0].click();", options[0])
    else:
        driver.execute_script("""
            var selectors = ['[data-radix-popper-content-wrapper]', '[role="listbox"]', '[data-state="open"]'];
            for (var i = 0; i < selectors.length; i++) {
                var el = document.querySelector(selectors[i]);
                if (el) {
                    var items = el.querySelectorAll('[role="option"], li');
                    if (items.length > 0) { items[0].click(); return; }
                }
            }
        """)
except Exception:
    try:
        country_input = driver.find_element(By.XPATH, "//input[@placeholder='Search' or @placeholder='search' or @placeholder='Select country']")
        country_input.send_keys("Canada")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@role='option']").click()
    except Exception:
        pass

time.sleep(1)

# Select institution types
try:
    universities_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='checkbox' and (following-sibling::*[contains(text(),'Universit')] or preceding-sibling::*[contains(text(),'Universit')])]")))
    driver.execute_script("arguments[0].click();", universities_btn)
except Exception:
    try:
        universities_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Universit')]//button | //button[contains(@aria-label,'Universit')]")))
        driver.execute_script("arguments[0].click();", universities_btn)
    except Exception:
        pass

time.sleep(0.5)

try:
    colleges_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='checkbox' and (following-sibling::*[contains(text(),'College')] or preceding-sibling::*[contains(text(),'College')])]")))
    driver.execute_script("arguments[0].click();", colleges_btn)
except Exception:
    try:
        colleges_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'College')]//button | //button[contains(@aria-label,'College')]")))
        driver.execute_script("arguments[0].click();", colleges_btn)
    except Exception:
        pass

time.sleep(0.5)

# Certification
cert = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., ICEF Certified Education Agent']")))
cert.click()
cert.send_keys("ICEF Certified Education Agent")
time.sleep(1)

# Upload document
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(r"C:\Users\sweta\Downloads\test_document.pdf")
time.sleep(2)

# Submit form
submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
driver.execute_script("arguments[0].click();", submit_btn)
time.sleep(5)

print("Signup process completed.")
driver.quit()
