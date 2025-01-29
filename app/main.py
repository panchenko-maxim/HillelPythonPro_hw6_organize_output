import logging

from app.loggers.init_logging import init_logging
from app.services import get_formatted_output, organize_data
from app.services.classes import DataProvider


def main() -> None:
    init_logging()
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    logging.info(get_formatted_output(data=organized_data))
