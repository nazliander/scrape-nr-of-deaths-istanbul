# Visualize # of Deaths in Istanbul to Understand Shock Effects of COVID-19

## Scraper Installation and Re-use Instructions

A scraper and simple time series analysis example with Selenium and Seaborn.

To build the Selenium scraper:

```docker build . -t istanbul-covid```

To run it:

```docker run istanbul-covid```

Requirements:

`./data/` must contain a .csv file with days and number of deaths with `\t` separated and without a header. From this repository, we do not share the dataset.

`./__logger/` folder must be created before running the docker commands.

