"""Scrapes a stock image website."""

import re

import requests
from bs4 import BeautifulSoup

from src.logging_config import setup_logger

# Initialize logger using the setup function
logger = setup_logger(__name__)


def search_stock(holiday_name):
    """
    Scrapes stock.adobe.com for the number of images available for a given holiday.

    Args:
        holiday_name (str): The holiday name to search for.

    Returns:
        image_count (int): The number of images found for the holiday. If no images are found,
                           or an error occurs, returns 0.
        search_url (str): The URL used to perform the search.
    """
    try:
        # Simulate a search request on Adobe Stock with the holiday name as a query parameter
        search_url = f"https://stock.adobe.com/search?k={holiday_name}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url=search_url, headers=headers)

        # Ensure the request was successful (status code 200)
        if response.status_code != 200:
            logger.error(
                f"Failed to retrieve data for {holiday_name}, "
                f"HTTP status code: {response.status_code}"
            )
            return 0, search_url

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML element containing the image count using its class attributes
        count_tag = soup.find('strong', {'class': 'text-sregular grey gravel-text'})

        if count_tag:
            # Use a regular expression to extract all numeric parts from the text
            count_text = count_tag.text.strip()
            match = re.search(r'[\d\u00A0,\.]+', count_text)
            if match:
                # Remove non-numeric characters (spaces, commas, dots)
                image_count_str = re.sub(r'[\s\u00A0,\.]', '', match.group(0))
                if image_count_str.isdigit():
                    image_count = int(image_count_str)
                    logger.info(f"Holiday: {holiday_name} | Image count: {image_count}")
                else:
                    image_count = 0
                    logger.warning(f"Unable to parse image count from the text: {count_text}")
            else:
                image_count = 0
                logger.warning(f"Unable to find numeric value in the text: {count_text}")
        else:
            image_count = 0
            logger.warning(f"No image count found on the page for '{holiday_name}'.")

        return image_count, search_url

    except Exception as err:
        logger.error(f"Error occurred while searching for '{holiday_name}': {err}")
        return 0, search_url
