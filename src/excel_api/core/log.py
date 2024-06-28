from loguru import logger
import os


def get_logger():
    os.makedirs("logs", exist_ok=True)
    logger.add("logs/excel_api.log", rotation="10 MB", retention="10 days")
    return logger


logger = get_logger()
