from datetime import datetime
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import Page, sync_playwright

from src.utils import config
from src.utils import pw_utils
from src.utils.logger import logger
from src.services.login_service import perform_login_to_leetcode
from src.services.problems_service import scrape_problems


def main() -> None:
    """
    Main function to orchestrate LeetCode login and problem scraping.
    """
    logger.info("Starting LeetCode processing")

    try:
        with sync_playwright() as p:
            logger.info("Connecting to the existing Chromium instance...")
            browser = p.chromium.connect_over_cdp(config.REMOTE_DEBUGGING_URL)
            context, page = pw_utils.initialize_browser_context(browser)
            
            # # playwright_instance, browser, context, page = pw_utils.initialize_browser()
            # context, page = pw_utils.initialize_browser()
            
            if not perform_login_to_leetcode(page):
                logger.error("Login failed. Aborting process.")
                return

            pw_utils.apply_random_delay()
            # Proceed to scrape problems after login
            scrape_problems(page)
            pw_utils.apply_random_delay(10, 12)

    except PlaywrightTimeoutError as e:
        logger.error(f"Timeout error occurred: {str(e)}", exc_info=True)
    except Exception as e:
        logger.error(f"An unexpected error occurred during processing: {str(e)}", exc_info=True)
    finally:
        logger.info("LeetCode processing completed.")


if __name__ == "__main__":
    try:
        script_start_time = datetime.now()
        logger.info(f"Script started at {script_start_time}")

        main()

        script_end_time = datetime.now()
        logger.info(f"Script completed at {script_end_time}")

        # Calculate script duration
        duration = script_end_time - script_start_time
        logger.info(f"Total Script Duration: {duration.total_seconds() / 60:.2f} minutes")
    except Exception as e:
        logger.error(f"Critical error in script execution: {str(e)}", exc_info=True)
