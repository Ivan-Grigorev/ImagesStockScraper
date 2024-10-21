"""Run a website scraper."""

import os
import sys
from datetime import datetime

import pandas as pd

from src.logging_config import setup_logger
from src.stock_scraper import search_stock

# Initialize logger using the setup function
logger = setup_logger(__name__)


def main():
    """
    Run the stock images scraper and save the results to an Excel file.

    Return:
         holidays_image_count (xlsx): File containing the number of images for each holiday.
    """
    logger.info(
        "\n========== Images Stock Scraper ==========\n"
        "You are about to begin the process of adding metadata to your images.\n"
        "Please enter the path to an Excel file containing holiday names. "
        "The output file will be saved in the current file directory. "
        "Ensure the holiday names are listed in a column named 'Holiday Name':\n"
    )
    try:
        # Get the file path from user input
        source_path = input('>>> ')

        # Check if the file exists at the provided path
        if not os.path.exists(source_path):
            logger.error(f"The provided path does not exist: {source_path}")
            sys.exit(1)

        # Ensure the provided file is an Excel file
        if not os.path.isfile(source_path) or os.path.splitext(source_path)[1] not in ['.xls', '.xlsx']:
            logger.error("Provided file is not supported. Check file!")
            sys.exit(1)

        # Load the Excel file into a DataFrame
        all_holiday_data = pd.read_excel(source_path)

        # Check if the required column 'Holiday Name' exists
        if 'Holiday Name' not in all_holiday_data.columns:
            logger.error(
                "The Excel file does not contain a 'Holiday Name' column. Please check the file format."
            )
            sys.exit(1)

        # Initialize an empty lists to store image counts and links
        image_counts = []
        image_links = []

        for holiday in all_holiday_data['Holiday Name']:
            image_count, search_url = search_stock(holiday_name=holiday)
            image_counts.append(image_count)
            image_links.append(search_url)

        # Add the image counts and links to the DataFrame
        all_holiday_data['Image Count'] = image_counts
        all_holiday_data['Images URL'] = image_links

        # Format current date and time to append to output filename
        current_datetime = datetime.now().strftime('%d-%m-%Y--%H-%M-%S')
        output_file = f"holidays_image_count-{current_datetime}.xlsx"

        # Determine the directory of the source file to save the output in the same location
        output_folder = os.path.dirname(source_path)
        output_path = os.path.join(output_folder, output_file)

        # Save the updated DataFrame to a new Excel file
        all_holiday_data.to_excel(output_path, index=False)

        logger.info(f"Excel file created successfully at: {output_path}")

    except FileNotFoundError as fnf_error:
        logger.error(f"File not found: {fnf_error}")
        sys.exit(1)

    except pd.errors.EmptyDataError:
        logger.error(f"The Excel file at {source_path} is empty.")
        sys.exit(1)

    except Exception as err:
        logger.error(f"An error occurred during processing: {err}")
        sys.exit(1)


if __name__ == '__main__':
    main()
