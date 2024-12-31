from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from src.utils import config, pw_utils
from src.utils.logger import logger


def perform_login_to_leetcode(page):
    """
    Logs into Leetcode. Returns True if successful, False otherwise.

    Args:
        page: Playwright page instance for browser automation.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    logger.info("Navigating to Leetcode login page.")
    page.goto(config.LEETCODE_LOGIN_URL)

    if "login" not in page.url:
        logger.info("Already logged into Leetcode!")
        return True

    try:
        logger.info("Entering login credentials...")
        pw_utils.human_like_typing(page, "input[name='login']", config.LEETCODE_LOGIN_USERNAME)
        pw_utils.apply_random_delay(1, 3)
        pw_utils.human_like_typing(page, "input[name='password']", config.LEETCODE_LOGIN_PASSWORD)
        pw_utils.apply_random_delay(1, 3)
        
        # # Check the human verification checkbox
        # logger.info("Checking if the human verification checkbox is available...")
        # checkbox_input = page.query_selector("input[type='checkbox']")
        # checkbox_indicator = page.query_selector("label.cb-lb > span.cb-i")
        # if checkbox_input:
        #     logger.info("Checkbox found. Attempting to check it...")
        #     page.check("input[type='checkbox']")
        #     pw_utils.apply_random_delay(3, 4)
        #     logger.info("Successfully checked the human verification checkbox.")
        # elif checkbox_indicator:
        #     logger.info("Checkbox indicator found. Attempting to click...")
        #     page.click("label.cb-lb > span.cb-i")
        #     pw_utils.apply_random_delay(2, 3)
        #     logger.info("Successfully clicked on the human verification checkbox indicator.")
        # else:
        #     pw_utils.apply_random_delay(7, 8)
        #     logger.warning("Checkbox not found. Skipping the human verification step.")
    
        page.click('.btn-content-container__2HVS')

        logger.info("Waiting for homepage URL to confirm login...")
        page.wait_for_url(config.LEETCODE_HOMEPAGE_URL, timeout=300000)  # 5 minutes
        logger.info("Login successful!")
        return True
    except PlaywrightTimeoutError:
        logger.error("Timeout waiting for dashboard URL.")
        _handle_login_failure(page)
        return False


def _handle_login_failure(page):
    """
    Handles login failure by capturing a screenshot and logging the error.

    Args:
        page: Playwright page instance.
    """
    screenshot_path = "logs/screenshots/login_timeout.png"
    page.screenshot(path=screenshot_path)
    logger.error(f"Screenshot saved at {screenshot_path} for debugging.")
