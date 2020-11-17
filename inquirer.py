
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
import regex
import pandas as pd


class DateValidator(Validator):
    def validate(self, document):
        ok = regex.match(
            "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid date -> Format: 2020-10-10 (Year-Month-Day',
                cursor_position=len(document.text))  # Move cursor to end


questions = [
    {
        "type": "input",
        "name": "start_date",
        "message": "What is the start date for scraping? Format: 2020-10-10 (Year-Month-Day)",
        "validate": DateValidator
    },
    {
        "type": "input",
        "name": "end_date",
        "message": "What is the end date for scraping? Format: 2020-10-10 (Year-Month-Day)",
        "validate": DateValidator
    }
]


def question_the_user() -> dict:
    """Questions the user for start and end dates for scraping batch.
    """
    dates_dict = prompt(questions)
    dates = dates_dict.values()
    start_date, end_date = min(dates), max(dates)
    return pd.period_range(start_date, end_date).strftime("%d/%m/%Y").values
