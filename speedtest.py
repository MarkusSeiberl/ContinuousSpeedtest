import os
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def startSpeedTest():
    print("Opening Speedtest")

    chrome_options = Options()
    driver = webdriver.Chrome(os.path.expanduser('/usr/lib/chromium-browser/chromedriver')) 



    try:
        driver.get("https://www.tarife.at/speedtest")


        # Start Speedtest
        driver.find_element_by_class_name("button-start").click()

        # Wait for test to finish
        time.sleep(25)

        # Get result elements
        results = driver.find_elements_by_class_name("speed-info")
        
        # Save results to variables
        ping = results[0].get_attribute("innerHTML")
        down = results[1].get_attribute("innerHTML")
        up = results[2].get_attribute("innerHTML")

        # Write results to file
        currTime = int(time.time())
        newLine = str(currTime) + "," + ping + "," + down + "," + up + "\n"

        f = open("speedtest_results.csv", "a")
        f.write(newLine)
        f.close()



        print("Logged into a1.net and accessed profile page")

    except Exception as e:
        print("An error occurred while trying to access a1.net!", e)
    finally:
        driver.close()


if __name__ == "__main__":
    startSpeedTest()