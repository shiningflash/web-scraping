import time
from collections import Counter

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from src.utils.logger import logger


fallback_counter = Counter()
retry_counter = Counter()


def wait_for_network_idle_with_fallback(page, timeout=10000, fallback_timeout=3000):
    try:
        logger.info(f"Waiting for network idle state (timeout: {timeout}ms)")
        page.wait_for_load_state("networkidle", timeout=timeout)
        logger.info("Network idle state achieved")
    except PlaywrightTimeoutError:
        fallback_counter['network_idle'] += 1
        logger.warning(
            f"Network did not reach idle state within {timeout}ms. "
            f"Proceeding after {fallback_timeout}ms delay."
        )
        time.sleep(fallback_timeout / 1000)


def navigate_with_retry(page, url, max_retries=3):
    """Navigates to the specified URL with retry logic."""
    logger.info(f"Navigating to URL: {url}")
    for attempt in range(max_retries):
        try:
            page.goto(url)
            wait_for_network_idle_with_fallback(page)
            logger.info(f"Successfully navigated to: {url}")
            return
        except PlaywrightTimeoutError:
            retry_counter['navigation'] += 1
            logger.warning(f"Navigation attempt {attempt + 1} failed for URL: {url}")
            if attempt == max_retries - 1:
                logger.error(f"Maximum retries reached for URL: {url}. Navigation failed.")
                raise
            logger.info(f"Retrying navigation to {url} in 10 seconds...")
            time.sleep(10)  # Wait 10 seconds before retrying
