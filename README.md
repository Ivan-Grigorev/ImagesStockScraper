# Images Stock Scraper

This project is a web scraper that retrieves the number of images available for specific holidays from Adobe Stock. It reads holiday names from an Excel file, performs web searches for each holiday, retrieves the image count and the link to the search results, and outputs the data into a new Excel file.

## Features
- Scrapes stock images for various holidays from Adobe Stock.
- Retrieves and records both the **number of images** and the **URL** for each holiday.
- Supports multiple languages in the results.
- Outputs image counts and URLs to a new Excel file.
- Utilizes logging for tracking progress and errors.
- File format validation to ensure the input is an Excel file.

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
3. When prompted, enter the path to your Excel file. Ensure that the file is in `.xls` or `.xlsx` format.
   
The scraper will search for each holiday on Adobe Stock, retrieve the image count, and the search result URL for the images. The output file will be saved in the same directory as the input file, with a timestamp appended to the filename.

## Logging
The script logs important information and errors to help with troubleshooting. You can track the progress in the console during execution, and the logs will provide insight into any issues encountered.

## Example
### Input Excel File:
```
| Holiday Name             |
|--------------------------|
| New Year's Day           |
| Independence Day         |
| Polar Bear Plunge Day    |
```

### Output Excel File:
```
| Holiday Name             | Image Count | Image URL                          |
|--------------------------|-------------|------------------------------------|
| New Year's Day           | 8839672     | https://stock.adobe.com/...        |
| Independence Day         | 1668424     | https://stock.adobe.com/...        |
| Polar Bear Plunge Day    | 293         | https://stock.adobe.com/...        |
```

### Note:
- The **Image Count** represents the total number of images found on Adobe Stock for the holiday.
- The **Image URL** provides a direct link to the search results for that holiday on Adobe Stock.

## Image Source and Usage Rights

The images referenced by this scraper are sourced from [Adobe Stock](https://stock.adobe.com/), a public resource for stock images. This application only fetches publicly available search result data and does not download or manipulate any images. Users must ensure they comply with Adobe Stock's [terms of service](https://www.adobe.com/legal/terms.html) when using the links and data provided by the scraper.

## License

This project is licensed under the terms of the [LICENSE](./LICENSE).

## Author

This repository was built and is maintained by [Ivan Grigorev](https://github.com/Ivan-Grigorev).
