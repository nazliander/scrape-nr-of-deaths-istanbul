from copy import deepcopy
import time

from helpers import get_dates, set_chrome_options, take_death_number, get_death_from_record
from custom_logger import set_logger

URL = "https://www.turkiye.gov.tr/istanbul-buyuksehir-belediyesi-vefat-sorgulama"
LOGGER = set_logger("istanbul_stats_app")

dates = get_dates(date_path="./data/dates_deaths.csv")
missing_dates = dates.loc[dates.numbers == "None", "dates"].values


def app() -> None:
    process_finished = False
    dates_deaths_dict = {}
    chrome_options = set_chrome_options()
    batch = deepcopy(missing_dates[100:150])
    while process_finished is False:
        for d in batch:
            time.sleep(1)
            LOGGER.info(d)
            dates_deaths_dict[d] = take_death_number(
                date_str=d,
                chrome_options=chrome_options,
                url=URL)
        missed_vals_in_batch = [
            vals for vals in dates_deaths_dict.values() if vals is None]
        if len(missed_vals_in_batch) == 0:
            process_finished = True
            LOGGER.info("Breaking the loop...")
        else:
            batch = deepcopy(missed_vals_in_batch)
            LOGGER.info("Restarting the loop...")
    for d, record in dates_deaths_dict.items():
        LOGGER.info(f"{get_death_from_record(record)}")


if __name__ == "__main__":
    app()
