# Stock Image Scraper

This project is a web scraper that retrieves the number of images available for specific holidays from a stock image website. It reads holiday names from an Excel file, performs web searches for each holiday, and outputs the results into a new Excel file.

## Features
- Scrapes stock images for various holidays.
- Supports multiple languages in results.
- Outputs image counts to a new Excel file.
- Utilizes logging for tracking progress and errors.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Ivan-Grigorev/ImagesStockScraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ImagesStockScraper
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Prepare an Excel file with a column named **"Holiday Name"** containing the holiday names you want to search for.
2. Run the scraper:
    ```bash
    python run_app.py
    ```
3. When prompted, enter the path to your Excel file.

The output file will be saved in the same directory as the input file, with a timestamp appended to the filename.

## Logging
The script logs important information and errors to help with troubleshooting. Check the console for logs during execution.

## Example
Input Excel File:
```
| Holiday Name             |
|--------------------------|
| New Year's Day           |
| Independence Day         |
| Polar Bear Plunge Day    |
```

Output Excel File:
```
| Holiday Name             | Image Count |
|--------------------------|-------------|
| New Year's Day           | 8839672     |
| Independence Day         | 1668424     |
| Polar Bear Plunge Day    | 293         |
```

## License

This project is licensed under the terms of the [LICENSE](./LICENSE).

## Author

This repository was built and is maintained by [Ivan Grigorev](https://github.com/Ivan-Grigorev).
