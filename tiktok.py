import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

def setup_driver():
    """Initialize and configure the Chrome driver"""
    options = uc.ChromeOptions()
    #options.add_argument("--headless=new")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver

def inject_cookies(driver, raw_cookie):
    driver.set_page_load_timeout(60)
    """Inject cookies into the browser session"""
    driver.get("https://www.tiktok.com")
    time.sleep(3)  # Wait for initial page load

    # Convert raw cookie string to dictionary
    cookies = {}
    for c in raw_cookie.split(";"):
        if "=" in c:
            name, value = c.split("=", 1)
            cookies[name.strip()] = value.strip()

    # Add each cookie to the driver
    for name, value in cookies.items():
        try:
            driver.add_cookie({
                "name": name,
                "value": value,
                "domain": ".tiktok.com"
            })
        except Exception as e:
            print(f"Failed to add cookie {name}: {e}")

    driver.refresh()  # Refresh to apply cookies
    time.sleep(3)

def safe_find_element(driver, by, value, timeout=10):
    """Safely find an element with explicit wait"""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value)))
    except TimeoutException:
        print(f"Element not found: {value}")
        return None

def scroll_container(driver, container_xpath, scrolls=10, scroll_amount=400, delay=1):
    """Scroll inside a container element"""
    container = safe_find_element(driver, By.XPATH, container_xpath)
    if container:
        for _ in range(scrolls):
            driver.execute_script(f"arguments[0].scrollTop += {scroll_amount};", container)
            time.sleep(delay)

def follow_and_message_user(driver, username):
    """Follow a user and send them a message"""
    try:
        # Navigate to user profile
        driver.get(f"https://www.tiktok.com/@{username}?lang=en")
        time.sleep(3)


        # Follow the user
        follow_btn = safe_find_element(driver, By.XPATH,
            '//button[@class="TUXButton TUXButton--default TUXButton--medium TUXButton--primary"]')
        if follow_btn:
            follow_btn.click()
            time.sleep(2)
        else:
            print(f"Already following {username} or follow button not found")

        # Open message dialog
        msg_btn = safe_find_element(driver, By.XPATH, '//button[@data-e2e="message-button"]')
        if msg_btn:
            msg_btn.click()
            time.sleep(3)

            # Find message input and send message
            msg_input = safe_find_element(driver, By.XPATH,
                '//div[@data-e2e="message-input-area"]//div[@contenteditable="true"]')
            if msg_input:
                msg_input.send_keys("Hello, I am following you for a test")
                msg_input.send_keys(Keys.ENTER)
                time.sleep(2)
                print(f"Message sent to {username}")
            else:
                print("Message input not found")
        else:
            print("Message button not found")

    except Exception as e:
        print(f"Error processing {username}: {e}")

def main():
    # Your raw cookie string
    raw_cookie = """"""

    # Initialize driver
    driver = setup_driver()

    try:
        # Inject cookies
        inject_cookies(driver, raw_cookie)

        # Navigate to target profile
        target_profile = "datascience7"
        driver.get(f"https://www.tiktok.com/@{target_profile}?lang=en")
        time.sleep(5)

        # Click on followers count
        followers_element = safe_find_element(driver, By.XPATH,
            '(//div[@class="css-mgke3u-DivNumber e1457k4r1"])[2]')
        if followers_element:
            followers_element.click()
            time.sleep(5)

            # Scroll through followers list
            scroll_container(driver,
                '//div[contains(@class, "css-wq5jjc-DivUserListContainer")]',
                scrolls=10, scroll_amount=400, delay=1)

            # Get follower usernames
            follower_elements = driver.find_elements(By.XPATH,
                '//div/p[@class="css-swczgi-PUniqueId ex4st9p8"]')
            follower_usernames = [elem.text for elem in follower_elements if elem.text]

            print(f"Found {len(follower_usernames)} followers:")
            for username in follower_usernames:
                print(username)

                # Follow and message each follower
                follow_and_message_user(driver, username)

        else:
            print("Followers element not found")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        driver.quit()

if __name__ == "__main__":
    main()
