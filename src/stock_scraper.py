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
            return 0

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML element containing the image count using its class attributes
        count_tag = soup.find('strong', {'class': 'text-sregular grey gravel-text'})

        if count_tag:
            match = re.search(r'(\d{1,3}(?:[.,]\d{3})*)', count_tag.text)
            if match:
                image_count = int(match.group(1).replace('.', '').replace(',', ''))
                logger.info(f"Holiday: {holiday_name} | Image count: {image_count}")
            else:
                image_count = 0
                logger.warning(f"Could not extract image count for '{holiday_name}'.")
        else:
            image_count = 0
            logger.warning(f"No image count found on the page for '{holiday_name}'.")

        return image_count

    except Exception as err:
        logger.error(f"Error occurred while searching for '{holiday_name}': {err}")
        return 0
