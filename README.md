# A Scraper to Collect Daily # of Deaths in Istanbul

Currently the main HTML for retrieving the death numbers on a daily basis has a captcha. For that reason `app.py` cannot locate the selectors.

Please consider as an exercise project for using Selenium and PyInquiry within a Docker container.

## Scraper Installation and Re-use Instructions

A scraper and simple time series analysis example with Selenium and Seaborn.

To build the Selenium scraper:

```docker build . -t istanbul-covid```

To run it:

```docker run -it istanbul-covid```
