from time import sleep

import undetected_chromedriver as uc

# ==================================================================================================

log_path = "/tmp/chromedriver.log"
url = "https://check.torproject.org/"

# ==================================================================================================


options = uc.ChromeOptions()
options.add_argument("--disable-application-cache")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--no-sandbox")
# options.add_argument("--headless")
options.add_argument("--start_maximized")

print("Creating driver")
chrome_driver = uc.Chrome(
    service_log_path=log_path,
    options=options,
)
print("Created driver")
chrome_driver.get(url)
sleep(5)
scraped_page = chrome_driver.page_source
chrome_driver.quit()
print(scraped_page)
