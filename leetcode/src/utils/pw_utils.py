import time
import random
from playwright.sync_api import Page, sync_playwright

from src.utils import config
from src.utils.logger import logger

# Constants for default delays
MIN_TYPING_DELAY = 0.05  # seconds
MAX_TYPING_DELAY = 0.2  # seconds
MIN_RANDOM_DELAY = 0.05  # seconds
MAX_RANDOM_DELAY = 0.2  # seconds


def apply_random_delay(min_seconds: float = MIN_RANDOM_DELAY, max_seconds: float = MAX_RANDOM_DELAY):
    """
    Pause execution for a random duration between the given range.

    Args:
        min_seconds (float): Minimum delay in seconds.
        max_seconds (float): Maximum delay in seconds.

    Raises:
        ValueError: If min_seconds is greater than max_seconds.
    """
    if min_seconds > max_seconds:
        raise ValueError("min_seconds cannot be greater than max_seconds.")

    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def move_mouse_randomly(page: Page):
    """
    Move the mouse to a random position within the viewport.

    Args:
        page (Page): The Playwright page instance.

    Raises:
        ValueError: If the viewport size is not available.
    """
    if not page.viewport_size:
        raise ValueError("Viewport size is not available on the page.")

    target_x = random.randint(0, page.viewport_size["width"])
    target_y = random.randint(0, page.viewport_size["height"])

    page.mouse.move(target_x, target_y)


def human_like_typing(page: Page, selector: str, text: str, delay_range: tuple = (50, 200)):
    """
    Simulate human-like typing on the specified element.

    Args:
        page (Page): The Playwright page instance.
        selector (str): The selector for the target element.
        text (str): The text to type.
        delay_range (tuple): A tuple containing the min and max delay (in ms) between keystrokes.

    Raises:
        ValueError: If delay_range is not valid.
    """
    min_delay, max_delay = delay_range

    if min_delay > max_delay:
        raise ValueError("min_delay cannot be greater than max_delay.")

    # Ensure the element is interactable
    page.click(selector)

    for char in text:
        page.type(selector, char, delay=random.uniform(min_delay, max_delay))
        apply_random_delay()


# def close_previous_playwright_instances():
#     import psutil

#     for proc in psutil.process_iter():
#         if proc.name() in ["playwright", "chromium", "chrome"]:
#             try:
#                 proc.terminate()
#             except Exception as e:
#                 logger.warning(f"Could not terminate process {proc.name()}: {e}")


def reset_playwright():
    try:
        logger.info("Resetting Playwright...")
        sync_playwright().start().stop()
    except Exception as e:
        logger.warning(f"Error resetting Playwright: {e}")


# def initialize_browser_context(browser):
#     """
#     Initializes the browser context and page.
#     """
#     try:
#         context = browser.new_context()
#         page = context.new_page()
#         logger.info("Browser context and page initialized.")
#         return context, page
#     except Exception as e:
#         logger.error(f"Failed to initialize browser context: {e}")
#         raise


def initialize_browser_context(browser):
    """
    Initializes the browser context and page.
    """
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    logger.info("Browser context and page initialized.")
    return context, page


def initialize_browser() -> tuple:
    """
    Initialize and connect to a Chromium browser instance.

    Returns:
        tuple: A tuple containing the browser instance and a new page.
    """
    # logger.info("Ensuring Proper Shutdown of Previous Sessions...")
    # # close_previous_playwright_instances()
    # logger.info("Reseting the Playwright Between Runs...")
    # reset_playwright()
    # logger.info("Connecting to the existing Chromium instance...")
    # playwright_instance = sync_playwright().start()
    # try:
    #     browser = playwright_instance.chromium.connect_over_cdp(config.REMOTE_DEBUGGING_URL)
    #     context, page = initialize_browser_context(browser)
    #     return playwright_instance, browser, context, page
    # except Exception as e:
    #     logger.error(f"Error during browser initialization: {e}")
    #     playwright_instance.stop()
    #     raise
    with sync_playwright() as p:
        logger.info("Connecting to the existing Chromium instance...")
        browser = p.chromium.connect_over_cdp(config.REMOTE_DEBUGGING_URL)
        context, page = initialize_browser_context(browser)
        return context, page
