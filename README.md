# CodeAlpha Web Scraping Project

My first practical Data Analytics project — a web scraping project built with Python.

## About the Project

This project extracts product information from the Scraping Sandbox website and organizes the collected data into a structured dataset.

The project started with `Requests` and `BeautifulSoup` for understanding how webpages can be accessed and parsed. However, because the website uses dynamic, client-side pagination, I introduced `Selenium` to automate browser interaction.

The final script automatically:

- Opens the website using Selenium
- Navigates through all 21 product pages
- Extracts product names, prices, and ratings
- Uses BeautifulSoup to parse the rendered HTML
- Stores the extracted information in Python data structures
- Converts the collected data into a Pandas DataFrame
- Exports the final dataset to Excel

## Tools Used

- Python
- Selenium
- BeautifulSoup
- Pandas
- OpenPyXL

## What I Learned

One of the most exciting parts of this project was discovering browser automation with Selenium. Seeing Python control the browser, navigate through multiple pages, and collect data automatically made the connection between programming and automation much clearer to me.

This project also helped me understand when `Requests` and BeautifulSoup are sufficient and when a browser automation tool such as Selenium becomes necessary for dynamically rendered websites.

## Output

The script generates an Excel file containing the scraped product data.

## Author

**Andrew Iretomiwa Obed (TomAndy)**
