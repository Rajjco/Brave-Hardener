import tkinter.messagebox
import os
import sys
import pathlib
import wmi
import psutil
from os import system
from pyautogui import press, alert, keyDown, keyUp
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager
from toascii import ConverterOptions, Image, gradients, ColorConverter

logo_path = 'Resources\\brave.png'
options = ConverterOptions(gradient=gradients.BLOCK, width=50, y_stretch=0.45, saturation=0.50)
converter = ColorConverter(options)
image = Image(logo_path, converter)

print(image.to_ascii())
print('''  ____                        _    _               _                             __  __  __ 
 |  _ \                      | |  | |             | |                           /_ |/_ |/_ |
 | |_) |_ __ __ ___   _____  | |__| | __ _ _ __ __| | ___ _ __   ___ _ __  __   _| | | | | |
 |  _ <| '__/ _` \ \ / / _ \ |  __  |/ _` | '__/ _` |/ _ \ '_ \ / _ \ '__| \ \ / / | | | | |
 | |_) | | | (_| |\ V /  __/ | |  | | (_| | | | (_| |  __/ | | |  __/ |     \ V /| |_| |_| |
 |____/|_|  \__,_| \_/ \___| |_|  |_|\__,_|_|  \__,_|\___|_| |_|\___|_|      \_/ |_(_)_(_)_|
                                                                                            
                                                                                            ''')
print('Downloading Latest Chrome Webdriver....')
print('------------------------------------')

webdriver_installer = ChromeDriverManager()
path, path2 = webdriver_installer.download_and_install()

script_path = pathlib.Path(__file__).parent.absolute()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


k = resource_path(script_path)

path = os.getenv('APPDATA')
i = path.split("\Roaming")
z = i[0]

while True:
    brave_running = "brave.exe" in (i.name() for i in psutil.process_iter())
    if brave_running == True:
        print("Closing Brave Browser...")
        os.system("TASKKILL /F /IM brave.exe")

    print("Clearing Previous Output")
    sleep(3)
    system('cls')

    print("------------------------------------\nApply Brave Hardening Settings\nEnter 1 for Security\n"
          "Enter 2 for Privacy\nEnter 3 for Performance\nEnter 0 to exit\n"
          "Notice: Make sure brave.exe is not running and all tabs are closed.\n------------------------------------")

    prompt = input("Select Hardening option: ")

    if prompt == str(1):
        chromedriver = f"{path2}"

        option = webdriver.ChromeOptions()
        option.add_argument(fr'--user-data-dir={z}\Local\BraveSoftware\Brave-Browser\User Data')
        option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        s = Service(chromedriver)

        driver = webdriver.Chrome(service=s, options=option)

        driver.get("brave://flags/")
        try:
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                "#block-insecure-private-network-requests")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="block-insecure-private-network-requests_name"]').send_keys('en')
            sleep(1)
            sleep(1)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                "#brave-domain-block")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-domain-block_name"]').send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                "#brave-ephemeral-storage")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-ephemeral-storage_name"]').send_keys('en')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                "#disallow-doc-written-script-loads")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="disallow-doc-written-script-loads_name"]').send_keys('en')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                "#enable-isolated-sandboxed-iframes")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="enable-isolated-sandboxed-iframes_name"]').send_keys('en')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                '#origin-agent-cluster-default')  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="origin-agent-cluster-default_name"]').send_keys(
                'en')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                '#strict-origin-isolation')  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="strict-origin-isolation_name"]').send_keys('dis')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                '#sync-trusted-vault-passphrase-recovery')  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="sync-trusted-vault-passphrase-recovery_name"]').send_keys('dis')
            sleep(1)

            sleep(1)

            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]').send_keys(
                '#u2f-security-key-api')  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="u2f-security-key-api_name"]').send_keys('dis')
            sleep(1)

            sleep(1)

            sleep(1)
            keyDown('ctrl')
            press('w')
            keyUp('ctrl')
            sleep(2)
        except Exception as e:
            tkinter.messagebox.showerror(title='Error', message=f'{e}')

        f = wmi.WMI()
        name = 'chromedriver.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
        alert(text='Security Hardening Settings Applied', title='Done', button='OK')

    if prompt == str(2):
        chromedriver = f"{path2}"

        option = webdriver.ChromeOptions()
        option.add_argument(fr'--user-data-dir={z}\Local\BraveSoftware\Brave-Browser\User Data')
        option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        s = Service(chromedriver)

        driver = webdriver.Chrome(service=s, options=option)

        driver.get("brave://flags/")

        try:
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#autofill-enable-sending-bcn-in-get-upload-details")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="autofill-enable-sending-bcn-in-get-upload-details_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#autofill-fill-merchant-promo-code-fields")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="autofill-fill-merchant-promo-code-fields_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#autofill-parse-merchant-promo-code-fields")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="autofill-parse-merchant-promo-code-fields_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-dark-mode-block")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-dark-mode-block_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-debounce")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-debounce_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-domain-block-1pes")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-domain-block-1pes_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-extension-network-blocking")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-extension-network-blocking_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-reduce-language")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="brave-reduce-language_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#device-posture")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="device-posture_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#disable-process-reuse")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="disable-process-reuse_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#edit-context")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="edit-context_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-accessibility-live-caption")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-accessibility-live-caption_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-autofill-credit-card-authentication")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-autofill-credit-card-authentication_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-fenced-frames")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-fenced-frames_name"]') \
                .send_keys('Enabled with Shadow')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-generic-sensor-extra-classes")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-generic-sensor-extra-classes_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-quic")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-quic_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-webusb-device-detection")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="enable-webusb-device-detection_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#extensions-menu-access-control")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="extensions-menu-access-control_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#font-access")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="font-access_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#omnibox-dynamic-max-autocomplete")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="omnibox-dynamic-max-autocomplete_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#omnibox-rich-autocompletion-promisin")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="omnibox-rich-autocompletion-promising_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#partitioned-cookies")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="partitioned-cookies_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#reduce-user-agent")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="reduce-user-agent_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#system-keyboard-lock")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="system-keyboard-lock_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#webxr-incubations")  # searchwindow
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="webxr-incubations_name"]') \
                .send_keys('dis')
            sleep(1)
        except Exception as e:
            tkinter.messagebox.showerror(title='Error', message=f'{e}')

        keyDown('ctrl')
        press('w')
        keyUp('ctrl')
        sleep(2)
        f = wmi.WMI()
        name = 'chromedriver.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
        alert(text='Privacy Hardening Settings Applied', title='Done', button='OK')

    if prompt == str(3):
        chromedriver = f"{path2}"

        option = webdriver.ChromeOptions()
        option.add_argument(fr'--user-data-dir={z}\Local\BraveSoftware\Brave-Browser\User Data')
        option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        s = Service(chromedriver)

        driver = webdriver.Chrome(service=s, options=option)

        driver.get("brave://flags/")
        try:
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#back-forward-cache")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="back-forward-cache_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-adblock-cookie-list-default")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="brave-adblock-cookie-list-default_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#brave-rewards-verbose-logging")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="brave-rewards-verbose-logging_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#durable-client-hints-cache")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="durable-client-hints-cache_name"]') \
                .send_keys('dis')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-parallel-downloading")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="enable-parallel-downloading_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-prerender2")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="enable-prerender2_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#enable-throttle-display-none-and-visibility-hidden-cross-origin-iframes")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="enable-throttle-display-none-and-visibility-hidden-cross-origin-iframes_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Search flags"]') \
                .send_keys("#restrict-websockets-pool")  # searchwindow
            sleep(1.5)
            driver.find_element(By.CSS_SELECTOR,
                                '[aria-labelledby="restrict-websockets-pool_name"]') \
                .send_keys('en')
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[class="clear-search"]').click()  # clearbtn
            sleep(1)
        except Exception as e:
            tkinter.messagebox.showerror(title='Error', message=f'{e}')
        sleep(1)
        keyDown('ctrl')
        press('w')
        keyUp('ctrl')
        sleep(2)
        f = wmi.WMI()
        name = 'chromedriver.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
        alert(text='Performance Settings Applied', title='Done', button='OK')

    if prompt == str(0):
        try:
            f = wmi.WMI()
            name = 'chromedriver.exe'
            for process in f.Win32_Process():
                if process.name == name:
                    process.Terminate()
            exit(0)
        except:
            break
